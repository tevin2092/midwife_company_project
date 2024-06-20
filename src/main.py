import psycopg
import sys

conn = psycopg.connect(
    dbname='mini_project',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

def view_appointments():
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
    cur.execute("""
        INSERT INTO appointments (AppointmentID, MidwifeID, ClientID, ServiceID, LocationID, Date, Time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (appointment_id, midwife_id, client_id, service_id, location_id, date, time))
    conn.commit()

def update_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time):
    cur.execute("""
        UPDATE appointments
        SET MidwifeID = %s, ClientID = %s, ServiceID = %s, LocationID = %s, Date = %s, Time = %s
        WHERE AppointmentID = %s
    """, (midwife_id, client_id, service_id, location_id, date, time, appointment_id))
    conn.commit()

def delete_appointment(appointment_id):
    cur.execute("DELETE FROM appointments WHERE AppointmentID = %s", (appointment_id,))
    conn.commit()

def view_midwife_schedule(midwife_id):
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

def main():
    while True:
        print("Menu:")
        print("1. View Appointments")
        print("2. Add Appointment")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. View Midwife Schedule")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            view_appointments()
        elif choice == '2':
            appointment_id = input("Enter Appointment ID: ")
            midwife_id = input("Enter Midwife ID: ")
            client_id = input("Enter Client ID: ")
            service_id = input("Enter Service ID: ")
            location_id = input("Enter Location ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            add_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time)
        elif choice == '3':
            appointment_id = input("Enter Appointment ID: ")
            midwife_id = input("Enter Midwife ID: ")
            client_id = input("Enter Client ID: ")
            service_id = input("Enter Service ID: ")
            location_id = input("Enter Location ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            update_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time)
        elif choice == '4':
            appointment_id = input("Enter Appointment ID: ")
            delete_appointment(appointment_id)
        elif choice == '5':
            midwife_id = input("Enter Midwife ID: ")
            view_midwife_schedule(midwife_id)
            
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


cur.close()
conn.close()