CREATE TABLE Contact(
    ID INT PRIMARY KEY,
    First_Name VARCHAR,
    LastName VARCHAR,
    Kategorie_ID INTEGER,
    FOREIGN KEY(Kategorie_ID) REFERENCES Kategorie(ID)
);

CREATE TABLE Adress(
    ID INT PRIMARY KEY,
    Street VARCHAR,
    PostCode VARCHAR,
    City VARCHAR,
    HouseNumber NVARCHAR,
    Contact_ID INT,
    FOREIGN KEY(Contact_ID) REFERENCES Contact(ID)

);

CREATE TABLE PhoneNumber(
    ID INT PRIMARY KEY,
    PhoneNumber VARCHAR,
    Contact_ID INT,
    FOREIGN KEY(Contact_ID) REFERENCES Contact(ID)

);

CREATE TABLE Kategorie(
    ID INT PRIMARY KEY,
    Kategorie VARCHAR
);