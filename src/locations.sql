\c project_db;

-- Create the table
CREATE TABLE locations (
    LocationID VARCHAR(3) PRIMARY KEY,
    LocationName VARCHAR(50)
);


-- Insert data into the table
INSERT INTO Locations (LocationID, LocationName) VALUES 
('NRC', 'North Office'),
('ERC', 'East Office'),
('MRC', 'Main Office');
