# -*- coding: utf-8 -*-
# module_playground/models/playground_rate.py

from odoo import models, fields, api, _
import requests


class PlaygroundRate(models.Model):
    """
    Model to store and manage Playground Rate data fetched from external API.
    This includes standard and other rates, and is equipped with chatter support.
    """
    _name = 'playground.rate'
    _description = 'Playground Rate'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Adds chatter & activity support

    # === Fields ===

    name = fields.Char(
        string="Rate Name",
        compute="_compute_rate_name",
        store=True,
        translate=True,
        help="Computed field: Description - Country Name (Country Code)"
    )

    country_code = fields.Char(
        string="Country Code",
        tracking=True,
        translate=True
    )

    country_name = fields.Char(
        string="Country Name",
        tracking=True,
        translate=True
    )

    eu = fields.Boolean(
        string=_("EU Member"),
        tracking=True,
        help="True if the country is part of the EU"
    )

    success = fields.Boolean(
        string=_("Success"),
        tracking=True,
        help="Indicates whether the API returned the rate successfully"
    )

    # === Standard Rate Fields ===

    standard_rate = fields.Float(
        string=_("Standard Rate"),
        tracking=True
    )

    standard_class = fields.Char(
        string="Standard Class",
        tracking=True,
        translate=True
    )

    standard_description = fields.Char(
        string="Standard Description",
        tracking=True,
        translate=True
    )

    standard_types = fields.Char(
        string="Standard Types",
        tracking=True,
        translate=True
    )

    # === Related Other Rates ===

    other_rate_ids = fields.One2many(
        'playground.other.rate',
        'rate_id',
        string="Other Rates",
        help="List of other applicable tax rates"
    )

    # === Compute Rate Name ===

    @api.depends('country_name', 'country_code', 'standard_description')
    def _compute_rate_name(self):
        """
        Computes the 'name' field as a combination of standard description,
        country name, and country code.
        """
        for record in self:
            record.name = f"{record.standard_description or ''} - {record.country_name} ({record.country_code})"

    # === Fetch Playground Rates from API ===

    @api.model
    def fetch_playground_rates(self):
        """
        Fetches rate data from an external API, clears existing records,
        and populates new records with standard and other rate details.
        """
        url = 'https://api.apilayer.com/tax_data/rate_list'
        headers = {'apikey': 'LV91HgGpb85DwlSbCl9QF7FahtvW7J9G'}

        response = requests.get(url, headers=headers)

    # Handle API failure silently
        if response.status_code != 200:
            print(f"[PlaygroundRate] API Error: {response.status_code} - {response.text}")
            return

        # Parse response
        data = response.json()
        if 'data' not in data:
            print("[PlaygroundRate] No 'data' key found in the API response.")
            return

        # Clear all existing records before refetching
        self.search([]).unlink()

        for item in data.get('data', []):
            # Create the main rate record
            rate_record = self.create({
                'country_code': item.get('country_code'),
                'country_name': item.get('country_name'),
                'eu': item.get('eu'),
                'success': item.get('success'),
                'standard_rate': item.get('standard_rate', {}).get('rate'),
                'standard_class': item.get('standard_rate', {}).get('class'),
                'standard_description': item.get('standard_rate', {}).get('description'),
                'standard_types': item.get('standard_rate', {}).get('types') or "null",
            })

            # Create related other rates
            for other in item.get('other_rates', []):
                self.env['playground.other.rate'].create({
                    'rate_id': rate_record.id,
                    'rate': other.get('rate'),
                    'tax_class': other.get('class'),
                    'description': other.get('description'),
                    'types': other.get('types'),
                    'types_array': ', '.join(other.get('types_array', [])),
                })