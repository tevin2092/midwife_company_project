from db import view_appointments, add_appointment, update_appointment, delete_appointment, view_midwife_schedule
from validation import get_correct_input, correct_date, correct_time

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
            date = get_correct_input("Enter Date (YYYY-MM-DD): ", correct_date)
            time = get_correct_input("Enter Time (HH:MM): ", correct_time)
            add_appointment(appointment_id, midwife_id, client_id, service_id, location_id, date, time)
        elif choice == '3':
            appointment_id = input("Enter Appointment ID: ")
            midwife_id = input("Enter Midwife ID: ")
            client_id = input("Enter Client ID: ")
            service_id = input("Enter Service ID: ")
            location_id = input("Enter Location ID: ")
            date = get_correct_input("Enter Date (YYYY-MM-DD): ", correct_date)
            time = get_correct_input("Enter Time (HH:MM): ", correct_time)
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
