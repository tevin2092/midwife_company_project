CREATE DATABASE project_db;

-- \c project_db;

CREATE SCHEMA company_data;

-- Create the appointments table
CREATE TABLE appointments (
    AppointmentID VARCHAR(20) PRIMARY KEY,
    MidwifeID INT,
    ClientID INT,
    ServiceID INT,
    LocationID VARCHAR(10),
    Date DATE,
    Time TIME
);

-- Insert data into the appointments table
INSERT INTO appointments (AppointmentID, MidwifeID, ClientID, ServiceID, LocationID, Date, Time) VALUES
('appt11', 123, 212, 2000, 'NRC', '2024-07-01', '09:00'),
('appt24', 122, 215, 5000, 'ERC', '2024-08-01', '10:30'),
('appt30', 125, 211, 3100, 'MRC', '2024-09-02', '14:00');
