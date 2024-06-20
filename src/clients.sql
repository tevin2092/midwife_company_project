-- connect
\c project_db

-- Create the clients table
CREATE TABLE clients (
    ClientID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(100)
);

-- Insert data into the clients table
INSERT INTO clients (ClientID, FirstName, LastName, Phone, Email, Address) VALUES
(211, 'Alice', 'Burder', '255-4321', 'alice.b@googlemail.com', '1237 Maple St'),
(212, 'Mary', 'Williams', '865-8765', 'mary.williams@gmail.com', '456 Oak St'),
(213, 'Laura', 'Lopez', '344-6789', 'laura.lo@gmail.com', '789 Pine St'),
(214, 'Bjarne', 'Baum', '875-6419', 'bj@yahoo.com', '19 Lincoln ave'),
(215, 'Theo', 'Igor', '732-4178', 'Igorfam@gmail.com', '5122 Flen St');
