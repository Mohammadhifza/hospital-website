from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from database import init_db, get_db
import sqlite3
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'hospital_secret_key_2024'

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

# ─── PUBLIC PAGES ────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctors')
def doctors():
    db = get_db()
    doctors = db.execute('SELECT * FROM doctors ORDER BY name').fetchall()
    return render_template('doctors.html', doctors=doctors)

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    db = get_db()
    doctors = db.execute('SELECT * FROM doctors ORDER BY name').fetchall()

    if request.method == 'POST':
        name    = request.form.get('patient_name', '').strip()
        phone   = request.form.get('phone', '').strip()
        email   = request.form.get('email', '').strip()
        doc_id  = request.form.get('doctor_id', '').strip()
        appt_dt = request.form.get('appointment_date', '').strip()
        message = request.form.get('message', '').strip()

        errors = []
        if not name:    errors.append('Patient name is required.')
        if not phone:   errors.append('Phone number is required.')
        if not email:   errors.append('Email is required.')
        if not doc_id:  errors.append('Please select a doctor.')
        if not appt_dt: errors.append('Appointment date is required.')

        if errors:
            return render_template('appointment.html', doctors=doctors, errors=errors,
                                   form=request.form)

        db.execute(
            '''INSERT INTO appointments (patient_name, phone, email, doctor_id,
               appointment_date, message, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (name, phone, email, doc_id, appt_dt, message,
             datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
        db.commit()
        return render_template('appointment.html', doctors=doctors, success=True)

    return render_template('appointment.html', doctors=doctors)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    sent = False
    if request.method == 'POST':
        sent = True
    return render_template('contact.html', sent=sent)

# ─── ADMIN ───────────────────────────────────────────────────────────────────

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if (request.form.get('username') == ADMIN_USERNAME and
                request.form.get('password') == ADMIN_PASSWORD):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials. Please try again.', 'error')
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
def admin_dashboard():
    db = get_db()
    total_doctors      = db.execute('SELECT COUNT(*) FROM doctors').fetchone()[0]
    total_appointments = db.execute('SELECT COUNT(*) FROM appointments').fetchone()[0]
    recent_appts = db.execute(
        '''SELECT a.*, d.name as doctor_name FROM appointments a
           JOIN doctors d ON a.doctor_id = d.id
           ORDER BY a.created_at DESC LIMIT 5'''
    ).fetchall()
    return render_template('admin/dashboard.html',
                           total_doctors=total_doctors,
                           total_appointments=total_appointments,
                           recent_appts=recent_appts)

# --- Doctors CRUD ---

@app.route('/admin/doctors')
@login_required
def admin_doctors():
    db = get_db()
    doctors = db.execute('SELECT * FROM doctors ORDER BY name').fetchall()
    return render_template('admin/doctors.html', doctors=doctors)

@app.route('/admin/doctors/add', methods=['GET', 'POST'])
@login_required
def admin_add_doctor():
    if request.method == 'POST':
        name  = request.form.get('name', '').strip()
        spec  = request.form.get('specialization', '').strip()
        days  = request.form.get('available_days', '').strip()
        if name and spec and days:
            db = get_db()
            db.execute('INSERT INTO doctors (name, specialization, available_days) VALUES (?,?,?)',
                       (name, spec, days))
            db.commit()
            flash('Doctor added successfully!', 'success')
            return redirect(url_for('admin_doctors'))
        flash('All fields are required.', 'error')
    return render_template('admin/doctor_form.html', doctor=None)

@app.route('/admin/doctors/edit/<int:doc_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_doctor(doc_id):
    db = get_db()
    doctor = db.execute('SELECT * FROM doctors WHERE id=?', (doc_id,)).fetchone()
    if not doctor:
        flash('Doctor not found.', 'error')
        return redirect(url_for('admin_doctors'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        spec = request.form.get('specialization', '').strip()
        days = request.form.get('available_days', '').strip()
        if name and spec and days:
            db.execute('UPDATE doctors SET name=?, specialization=?, available_days=? WHERE id=?',
                       (name, spec, days, doc_id))
            db.commit()
            flash('Doctor updated successfully!', 'success')
            return redirect(url_for('admin_doctors'))
        flash('All fields are required.', 'error')
    return render_template('admin/doctor_form.html', doctor=doctor)

@app.route('/admin/doctors/delete/<int:doc_id>', methods=['POST'])
@login_required
def admin_delete_doctor(doc_id):
    db = get_db()
    db.execute('DELETE FROM doctors WHERE id=?', (doc_id,))
    db.commit()
    flash('Doctor deleted successfully!', 'success')
    return redirect(url_for('admin_doctors'))

# --- Appointments ---

@app.route('/admin/appointments')
@login_required
def admin_appointments():
    db = get_db()
    appts = db.execute(
        '''SELECT a.*, d.name as doctor_name FROM appointments a
           JOIN doctors d ON a.doctor_id = d.id
           ORDER BY a.appointment_date DESC'''
    ).fetchall()
    return render_template('admin/appointments.html', appointments=appts)

@app.route('/admin/appointments/delete/<int:appt_id>', methods=['POST'])
@login_required
def admin_delete_appointment(appt_id):
    db = get_db()
    db.execute('DELETE FROM appointments WHERE id=?', (appt_id,))
    db.commit()
    flash('Appointment deleted successfully!', 'success')
    return redirect(url_for('admin_appointments'))

# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
