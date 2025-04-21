# -*- coding: utf-8 -*-
# module_playground/models/playground_other_rate.py

from odoo import models, fields, _


class PlaygroundOtherRate(models.Model):
    """
    Model to represent additional tax rates (other than the standard rate)
    associated with each playground rate.
    """
    _name = 'playground.other.rate'
    _description = 'Playground Other Tax Rates'

    # === Relationships ===

    rate_id = fields.Many2one(
        'playground.rate',
        string='Parent Rate',
        required=True,
        ondelete='cascade',
        help="Reference to the main playground rate"
    )

    # === Other Rate Fields ===

    rate = fields.Float(
        string='Rate',
        help="Other applicable tax rate"
    )

    tax_class = fields.Char(
        string=_('Class'),
        translate=True,
        help="Classification of the tax"
    )

    description = fields.Text(
        string=_('Description'),
        translate=True,
        help="Description of the tax type"
    )

    types = fields.Char(
        string=_('Types'),
        translate=True,
        help="Types of goods or services the rate applies to"
    )

    types_array = fields.Char(
        string=_('Types Array'),
        translate=True,
        help="Comma-separated list of types from the API"
    )
