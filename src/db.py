import psycopg
from contextlib import contextmanager

@contextmanager
def db_connect():
    conn = psycopg.connect(
        dbname='mini_project',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    try:
        yield conn
    finally:
        conn.close()

def view_appointments():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.AppointmentID, m.FirstName || ' ' || m.LastName AS Midwife, 
                       c.FirstName || ' ' || c.LastName AS Client, s.ServiceName, 
                       l.LocationName, a.Date, a.Time
                FROM appointments a
                JOIN midwives m ON a.MidwifeID = m.MidwifeID
                JOIN clients c ON a.ClientID = c.ClientID
                JOIN services s ON a.ServiceID = s.ServiceID
                JOIN locations l ON a.LocationID = l.LocationID
            """)
            rows = cur.fetchall()
            for row in rows:
                print(row)

def add_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO appointments (AppointmentID, MidwifeID, ClientID, ServiceID, LocationID, Date, Time)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (appointment_id, midwife_id, client_id, service_id, location_id, date, time))
            conn.commit()

def update_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE appointments
                SET MidwifeID = %s, ClientID = %s, ServiceID = %s, LocationID = %s, Date = %s, Time = %s
                WHERE AppointmentID = %s
            """, (midwife_id, client_id, service_id, location_id, date, time, appointment_id))
            conn.commit()

def delete_appointment(appointment_id):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM appointments WHERE AppointmentID = %s", (appointment_id,))
            conn.commit()

def view_midwife_schedule(midwife_id):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.AppointmentID, c.FirstName || ' ' || c.LastName AS Client, 
                       s.ServiceName, l.LocationName, a.Date, a.Time
                FROM appointments a
                JOIN clients c ON a.ClientID = c.ClientID
                JOIN services s ON a.ServiceID = s.ServiceID
                JOIN locations l ON a.LocationID = l.LocationID
                WHERE a.MidwifeID = %s
                ORDER BY a.Date, a.Time
            """, (midwife_id,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
