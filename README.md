# 📚 Odoo Library Management System

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple?style=for-the-badge&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Maintained-green?style=for-the-badge)

A comprehensive, **full-stack Odoo 18 module** designed to manage modern library operations. This project serves as an advanced technical demonstration of Odoo development, bridging the gap between backend logic, database optimization, and modern frontend customization using the **OWL framework**.

---

## 📸 Screenshots

| **Dashboard (SQL View)** | **Rent Wizard** |
|:---:|:---:|
| ![Dashboard](https://placehold.co/600x400) | ![Wizard](https://placehold.co/600x400) |
| *High-performance SQL-based statistics* | *Transient model for lending logic* |

| **OWL Star Rating** | **PDF Report** |
|:---:|:---:|
| ![OWL](https://placehold.co/600x400) | ![Report](https://placehold.co/600x400) |
| *Custom JavaScript Component* | *QWeb PDF Catalogue* |

---

## 🚀 Technical Architecture

This module follows strict **Odoo 18 best practices** and covers the full development spectrum:

### 🔹 1. Core Backend & DB Optimization
- **Data Modeling:** Complex relations (`One2many`, `Many2one`) with standard naming conventions.
- **Smart Inheritance:** Extended `res.partner` using `_inherit` to add library member data without breaking the core.
- **SQL Views:** Bypassed the ORM for the dashboard to solve the **N+1 Query Problem**.
  - *Tech Stack:* Direct PostgreSQL queries, `tools.drop_view_if_exists`.
- **Security:** Granular ACLs (CSV) and Row-level security for `Librarians` vs `Users`.

### 🔹 2. Frontend & UX (JavaScript/OWL)
- **Custom Widget:** Built a reactive **Star Rating** component from scratch.
- **Framework:** Odoo Web Library (OWL) 2.0.
- **Integration:** Registered via `registry.category("fields")` and extended `standardFieldProps` (Odoo 18 compliant).

### 🔹 3. Automation & Business Logic
- **Transient Models:** "Rent Book" wizard for temporary data handling.
- **Cron Jobs:** Automated daily checks for overdue books (`ir.cron`).
- **QWeb Reports:** Custom HTML/CSS layouts for generating professional PDF catalogues.

---

## 🔌 API Reference

The module exposes a public REST API for external integrations (Mobile Apps/Websites).

### Get Available Books
**Endpoint:** `POST /library/books`
**Auth:** Public (None required for demo)

**Request (JSON-RPC):**
```js
fetch('/library/books',{
  method: 'POST',
  headers: {
      'content-Type': 'application/json'
  },
  body: JSON.stringify({
      jsonrpc: "2.0",
      method: "call",
      params: {}
  })
})
.then(response => response.json())
.then(data => console.log(data.result));
```
**Response:**
```json
{
  "status": "success",
  "total": 3,
  "data": [
    {
      "author": "Paulo Coelho",
      "id": 7,
      "isbn": "978-0062315007",
      "title": "The Alchemist",
      "year": 1988
    },
    {
      "author": "Ray Bradbury",
      "id": 9,
      "isbn": "0-394-54702-0",
      "title": "Death Is a Lonely Business",
      "year": 1985
    },
    {
      "author": "Horace Walpole",
      "id": 11,
      "isbn": "9788831964067",
      "title": "The Castle of Otranto",
      "year": 1764
    }
  ]
}
```
**📂 Project Structure**
```
library_app/
├── controllers/      # REST API Endpoints
├── data/             # Cron Jobs & Automated Actions
├── models/           # Python Backend (SQL Views & Logic)
├── report/           # QWeb PDF Templates
├── security/         # Access Rights (ACLs & Groups)
├── static/           # JS (OWL), CSS, and Images
├── views/            # XML Views (Form, List, Graph)
└── wizard/           # Pop-up Logic (Transient Models)
```

### 🛠️ Installation
**1. Clone the repository:**
```
git clone https://github.com/pitiky0/odoo-library-management.git
```
**2. Add to Addons:** Move the `library_app` folder to your Odoo `custom_addons` directory.

**3. Restart Odoo Service:**
```
sudo systemctl restart odoo18.service
```
**4. Activate:**

- Go to **Apps → Update App List.**

- Search for **"Library Management".**

- Click **Activate.**

### 👨‍💻 Author
**Ayoub Karret** Odoo Developer
