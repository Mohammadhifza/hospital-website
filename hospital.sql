-- MediCare Hospital Database
-- Generated automatically

BEGIN TRANSACTION;
CREATE TABLE appointments (
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
CREATE TABLE doctors (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT NOT NULL,
            specialization   TEXT NOT NULL,
            available_days   TEXT NOT NULL
        );
INSERT INTO "doctors" VALUES(1,'Dr. Priya Sharma','Cardiologist','Mon, Wed, Fri');
INSERT INTO "doctors" VALUES(2,'Dr. Rajan Mehta','Neurologist','Tue, Thu, Sat');
INSERT INTO "doctors" VALUES(3,'Dr. Anita Reddy','Pediatrician','Mon, Tue, Wed');
INSERT INTO "doctors" VALUES(4,'Dr. Suresh Kumar','Orthopedic Surgeon','Wed, Thu, Fri');
INSERT INTO "doctors" VALUES(5,'Dr. Kavitha Nair','Dermatologist','Mon, Thu, Sat');
INSERT INTO "doctors" VALUES(6,'Dr. Vikram Patel','General Physician','Mon, Tue, Wed, Thu, Fri');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('doctors',6);
COMMIT;
