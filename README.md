# 📚 Odoo Library Management System

A comprehensive, full-stack Odoo module designed to manage modern library operations. This project demonstrates advanced Odoo development capabilities, ranging from core data modeling to API integrations and frontend customization using the OWL framework.

**Compatible with:** 18.0

---

## 🚀 Technical Features

This module was built following strict Odoo best practices and covers the following technical areas:

### 🔹 1. Core Architecture & Backend
- **Advanced Data Modeling:** Implemented complex relationships (`One2many`, `Many2one`) between Books and Authors.
- **Inheritance:** Extended the standard `res.partner` model to include library member details without altering core files.
- **Computed Fields:** Automated logic for tracking book counts and statuses using `@api.depends`.
- **Access Rights (ACL):** Granular security implementation with distinct roles for `Librarians` (Full Access) and `Users` (Read-only).

### 🔹 2. Business Logic & Automation
- **Wizards (Transient Models):** Created a "Rent Book" popup wizard to handle lending logic and date tracking seamlessly.
- **Cron Jobs (Automation):** Automated daily scheduled actions to check for overdue books and log alerts.
- **Smart Buttons & Active Archive:** Implemented UX best practices for record management.

### 🔹 3. Reporting & Analytics
- **QWeb PDF Reports:** Professional, printable PDF catalogue for selected books using custom layouts.
- **SQL Views & Dashboards:** Bypassed the ORM for high-performance reporting, using direct SQL queries to generate a statistics dashboard (Book count per author, Average ratings).

### 🔹 4. Connectivity & Frontend
- **REST API Integration:** Developed a custom `Controller` exposing a JSON endpoint (`/library/books`) for external mobile/web app integration.
- **OWL Framework (JS):** Built a custom **Star Rating Widget** from scratch using Odoo's modern JavaScript framework to enhance the UI.

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/pitiky0/odoo-library-management.git](https://github.com/pitiky0/odoo-library-management.git)
    ```

2. **Add to Odoo addons path:** Move the folder to your `custom_addons` directory.

3. **Install:**
    - Update App List.
    - Search for "Library Management".
    - Click **Activate.**

## 📸 Screenshots

👨‍💻 Author
Ayoub Karret Odoo Developer