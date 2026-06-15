# MediCare Hospital Website

A full-stack hospital website built with **Python (Flask)**, **HTML/CSS**, and **SQLite**.

---

## Project Structure

```
hospital_website/
├── app.py              # Main Flask application (all routes)
├── database.py         # DB initialisation & helpers
├── requirements.txt    # Python dependencies
├── hospital.sql        # Database dump (schema + sample data)
├── instance/
│   └── hospital.db     # SQLite database (auto-created on first run)
├── static/
│   └── css/
│       ├── style.css   # Public site styles
│       └── admin.css   # Admin panel styles
└── templates/
    ├── base.html       # Shared navbar + footer
    ├── index.html      # Home page
    ├── doctors.html    # Doctors list
    ├── appointment.html# Appointment booking form
    ├── contact.html    # Contact page
    └── admin/
        ├── base.html       # Admin shell (sidebar + header)
        ├── login.html      # Admin login
        ├── dashboard.html  # Stats + recent appointments
        ├── doctors.html    # Doctors list (CRUD)
        ├── doctor_form.html# Add / Edit doctor form
        └── appointments.html # All appointments
```

---

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

The app starts at **http://127.0.0.1:5000**

> The database is created automatically with 6 sample doctors on first run.

### 4. (Optional) Load from SQL dump instead
```bash
sqlite3 instance/hospital.db < hospital.sql
```

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Home page – intro, services, why us |
| `/doctors` | Doctor listing with specializations |
| `/appointment` | Appointment booking form |
| `/contact` | Contact info + message form |
| `/admin/login` | Admin login |
| `/admin` | Admin dashboard |
| `/admin/doctors` | Manage doctors (Add/Edit/Delete) |
| `/admin/appointments` | View & delete appointments |

---

## Admin Login

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |

---

## Database Tables

### `doctors`
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Auto-increment ID |
| name | TEXT | Doctor's full name |
| specialization | TEXT | Medical specialty |
| available_days | TEXT | e.g. "Mon, Wed, Fri" |

### `appointments`
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Auto-increment ID |
| patient_name | TEXT | Patient's full name |
| phone | TEXT | Contact number |
| email | TEXT | Email address |
| doctor_id | INTEGER FK | References doctors(id) |
| appointment_date | TEXT | Chosen date |
| message | TEXT | Symptoms / notes |
| created_at | TEXT | Booking timestamp |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3 (custom), Font Awesome icons |
| Backend | Python 3, Flask |
| Database | SQLite (via Python's built-in sqlite3 module) |
| Admin | Flask sessions (cookie-based auth) |

---

## Features

- ✅ Responsive design (mobile-friendly)
- ✅ Appointment booking with server-side validation
- ✅ Admin login with session-based authentication
- ✅ Admin CRUD for doctors
- ✅ Admin view & delete appointments
- ✅ Dashboard statistics (total doctors & appointments)
- ✅ Success / error flash messages
- ✅ Pre-loaded sample doctor data
