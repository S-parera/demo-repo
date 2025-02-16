CREATE TABLE Persons (
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL
);


INSERT INTO Persons (Name, Age) VALUES
('Alice Johnson', 28),
('Bob Smith', 35),
('Charlie Brown', 22),
('Diana White', 40);


SELECT *
FROM Persons;