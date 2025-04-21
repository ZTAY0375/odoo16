# 🎠 Playground Rates - Odoo Module

The **Playground Rates** module for Odoo allows users to manage and monitor playground rate data, fetched automatically via a Cron job from an external API. It supports full CRUD operations, multiple views, reporting, translation in German (CH), and adheres to best coding practices.

---

## 📦 Features

- List, Form, Kanban, and Search views for managing playground rate records.
- Chatter integration for discussion, tracking changes, and attachments.
- Automatically fetches playground rates from an external API using a scheduled Cron job.
- Record name is computed from `description`, `country_name`, and `country_code`.
- Users can manually Add, Update, and Delete data.
- A PDF Report is available for each playground rate record.
- Fully translated into German (Switzerland).
- Custom icon included in the menu.
- Clean and well-documented codebase following Odoo best practices.

---

## 🛠️ Installation

1. Clone this repository or copy the `playground_rates` folder into your Odoo `addons` directory.
2. Restart the Odoo server:
    ```bash
    ./odoo-bin -d your_database -u playground_rates
    ```
3. Activate **Developer Mode** in Odoo.
4. Go to **Apps**, search for **Playground Rates**, and install the module.

---

## 🔐 Access Rights

| Role   | Permissions            |
|--------|------------------------|
| User   | View, Add, Edit, Delete |
| Admin  | Full Access             |

---

## 🧭 Navigation

- **Main Menu**: `Playground > Playground Rates`

---

## 📋 Views

| View Type   | Description                                              |
|-------------|----------------------------------------------------------|
| List View   | Displays all records in a tabular format.                |
| Form View   | Detailed view with chatter support.                      |
| Kanban View | Card-style layout for quick insights.                    |
| Search View | Enables search by fields like country, rate, etc.        |

---

## 🧾 Report

- PDF report available for each record.
- Access via **Print Report** button on the form view.

---

## 🔁 Cron Job: Auto Fetch Data

- Automatically fetches playground rate data from an external API.
- Can be triggered manually or runs on a schedule.
- Configurable in:  
  `Settings > Technical > Automation > Scheduled Actions > Fetch Playground Rates`

---

## 📝 Fields


- `Rate Name`
- `Country Name`
- `Country Code`
- `Currency`
- `EU Member`
- `Success`
- `Standard Rate`
- `Standard Class`
- `Standard Discription`
- `Standard Types`
- `Rate`
- `Class`
- `Discription`
- `Types`
- `Types Array`

---

## 🌐 Translations

- German (CH) translation included in `/i18n/` directory.
- Language auto-applies based on user preference.

---

## 📷 Module Icon

Custom icon is applied to the main menu entry.

---

## 💬 Chatter Integration

- Users can log messages, add attachments, and see change logs in the form view.

---

## 🧰 How to Use

### ➕ Add a Rate
1. Go to `Playground > Playground Rates`
2. Click **Create**
3. Fill in the fields and **Save**

### 🔄 Sync with API
- Ensure the Cron job is active to fetch data on schedule.
- Or trigger manually from Scheduled Actions.

### 🖨️ Print Report
- Open any rate record.
- Click on **Print Report** to generate a PDF.

---

## 🧑‍💻 Developer Notes

- `_rec_name` is set to use the computed `name` field.
- Organized folder structure: `models/`, `views/`, `report/`, `data/`
- Cleanly separated logic, reusable functions, and Odoo best practices followed.

---

## 🧪 Testing

Tested on:
- **Odoo 16**
- **Python version 3.8.10**
- **Ubuntu / Windows**
- **PostgreSQL 12+**

---

## 📄 License

This module is released under the [Odoo Proprietary License v1.0](https://www.odoo.com/documentation/user/16.0/legal/licenses/licenses.html).

---

## 📞 Support

For issues, suggestions, or contributions, feel free to open an issue or contact the maintainer.

---

