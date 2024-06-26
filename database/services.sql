-- Create the table
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100),
    Description VARCHAR(255)
);

-- Insert data into the table
INSERT INTO Services (ServiceID, ServiceName, Description) VALUES 
(5000, 'Prenatal Checkup', 'Regular checkup during pregnancy'),
(2000, 'Delivery', 'Assistance during childbirth'),
(3100, 'Postnatal Care', 'Care after childbirth');
