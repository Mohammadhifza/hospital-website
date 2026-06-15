import sqlite3
from flask import g, current_app
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'instance', 'hospital.db')

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    db = get_db()
    db.executescript('''
        CREATE TABLE IF NOT EXISTS doctors (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT NOT NULL,
            specialization   TEXT NOT NULL,
            available_days   TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS appointments (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name     TEXT NOT NULL,
            phone            TEXT NOT NULL,
            email            TEXT NOT NULL,
            doctor_id        INTEGER NOT NULL,
            appointment_date TEXT NOT NULL,
            message          TEXT,
            created_at       TEXT NOT NULL,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
        );

        INSERT OR IGNORE INTO doctors (id, name, specialization, available_days) VALUES
            (1, 'Dr. Priya Sharma',    'Cardiologist',       'Mon, Wed, Fri'),
            (2, 'Dr. Rajan Mehta',     'Neurologist',        'Tue, Thu, Sat'),
            (3, 'Dr. Anita Reddy',     'Pediatrician',       'Mon, Tue, Wed'),
            (4, 'Dr. Suresh Kumar',    'Orthopedic Surgeon', 'Wed, Thu, Fri'),
            (5, 'Dr. Kavitha Nair',    'Dermatologist',      'Mon, Thu, Sat'),
            (6, 'Dr. Vikram Patel',    'General Physician',  'Mon, Tue, Wed, Thu, Fri');
    ''')
    db.commit()
    db.close()
    print("Database initialised with sample data.")
