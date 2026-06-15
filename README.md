# 🏥 MediCare Hospital Website

A full-stack hospital website where patients can view doctor information and book appointments. Built with Python (Flask), HTML, CSS, and SQLite.

---

## 🔗 Live Demo

**Website:** https://hospital-website-yw23.onrender.com

**Admin Panel:** https://hospital-website-yw23.onrender.com/admin
- Username: `admin`
- Password: `admin123`

> Note: Hosted on a free server — first load may take up to 50 seconds if inactive.

---

## 📋 Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Hospital intro, services, banner |
| Doctors | `/doctors` | List of doctors with specialization and available days |
| Appointment | `/appointment` | Book an appointment with form validation |
| Contact | `/contact` | Hospital contact info and message form |
| Admin | `/admin` | Admin dashboard (login required) |

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Font Awesome Icons |
| Backend | Python 3, Flask |
| Database | SQLite (via Python's built-in sqlite3) |
| Hosting | Render.com (free tier) |

---

## 🗄️ Database Structure

### Doctors Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key, auto-increment |
| name | TEXT | Doctor's full name |
| specialization | TEXT | Medical specialty |
| available_days | TEXT | e.g. Mon, Wed, Fri |

### Appointments Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key, auto-increment |
| patient_name | TEXT | Patient's full name |
| phone | TEXT | Contact number |
| email | TEXT | Email address |
| doctor_id | INTEGER | Foreign key → doctors(id) |
| appointment_date | TEXT | Chosen appointment date |
| message | TEXT | Symptoms or notes |
| created_at | TEXT | Booking timestamp |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Mohammadhifza/hospital-website.git
cd hospital-website
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:
```bash
venv\Scripts\activate
```

On Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

The database is created automatically with 6 sample doctors on first run.

---

## ✨ Features

- ✅ Responsive design — works on mobile and desktop
- ✅ Appointment booking with server-side validation
- ✅ Success message after booking
- ✅ Admin login with session-based authentication
- ✅ Admin can Add / Edit / Delete doctors
- ✅ Admin can view and delete appointments
- ✅ Dashboard showing total doctors and appointments
- ✅ Pre-loaded with 6 sample doctors

---

## 📁 Project Structure

```
hospital_website/
├── app.py                  # Main Flask app (all routes)
├── database.py             # Database setup and helpers
├── requirements.txt        # Python dependencies
├── hospital.sql            # Database SQL dump
├── Procfile                # Render deployment config
├── README.md               # Project documentation
├── instance/
│   └── hospital.db         # SQLite database (auto-created)
├── static/
│   └── css/
│       ├── style.css       # Public site styles
│       └── admin.css       # Admin panel styles
└── templates/
    ├── base.html           # Shared navbar and footer
    ├── index.html          # Home page
    ├── doctors.html        # Doctors listing
    ├── appointment.html    # Appointment booking form
    ├── contact.html        # Contact page
    └── admin/
        ├── base.html       # Admin layout
        ├── login.html      # Admin login page
        ├── dashboard.html  # Stats dashboard
        ├── doctors.html    # Manage doctors
        ├── doctor_form.html# Add/Edit doctor form
        └── appointments.html # View appointments
```

---

## 👨‍💻 Admin Panel Features

- **Dashboard** — Total doctors and appointments count with recent bookings
- **Doctors** — Add new doctors, edit existing ones, delete doctors
- **Appointments** — View all patient appointments, delete appointments

---

## 🛠️ Built By

Mohammad Hifza — Fresher Developer
