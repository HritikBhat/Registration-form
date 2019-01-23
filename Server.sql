Create database Server;
Use Server;
CREATE TABLE Person (
    PersonID int primary key,
    Name varchar(255) UNIQUE,
	Email varchar(255) UNIQUE,
    Phone  varchar(255),
    Address varchar(255),
    Password varchar(255) NOT NULL UNIQUE 
);
