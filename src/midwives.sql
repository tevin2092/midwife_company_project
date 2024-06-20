\c project_db

-- Create the table
CREATE TABLE Midwives (
    MidwifeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Phone VARCHAR(15),
    Email VARCHAR(100)
);

-- Insert data into the table
INSERT INTO Midwives (MidwifeID, FirstName, LastName, Phone, Email) VALUES 
(121, 'Jennifer', 'Smith', '225-1234', 'jsmith@gmail.com'),
(122, 'Emily', 'Lee', '412-5678', 'emily54@yahoo.com'),
(123, 'Sarah', 'Tufu', '773-8765', 'sarah.tufu@aol.com'),
(124, 'Lena', 'Schwartz', '425-1234', 'L.S@gmail.com'),
(125, 'Patricia', 'Black', '155-1444', 'pablack568@gmail.com');
