Create database Server;
Use Server;
CREATE TABLE record (
    Name varchar(255) UNIQUE,
	Email varchar(255) UNIQUE,
    Phone  varchar(255),
    Address1 varchar(255),
    Address2 varchar(255),
    Password varchar(255) NOT NULL UNIQUE 
);
