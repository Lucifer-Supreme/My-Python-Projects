Hotel Paradise - README

Welcome to Hotel Paradise, a simple hotel management system designed to manage customer details and stay information.

1. Setting up the database:
    - (All database setup queries are listed in the bottom of this file)
    - Make sure you have MySQL installed on your system.
    - Execute the following SQL queries to set up the database:
        - Create the database: `CREATE DATABASE Hotel_Paradise;`
        - Use the database: `USE Hotel_Paradise;`
        - Create tables for customer personal info and stay info (see SQL queries in the file `setup_database.sql`).

2. Running the program:
    - Make sure you have Python installed on your system.
    - Open the file `hotel_paradise.py` in your preferred Python IDE or text editor.
    - Update the database connection details (host, user, password) in the code if necessary.
    - Run the program. You will be presented with a menu to perform various tasks such as inserting new entries, updating existing data, deleting data, and showing particular room info.

3. Usage:
    - To insert a new entry, choose option 1 and follow the prompts to enter customer details and preferences.
    - To update existing customer data, choose option 2 and follow the prompts to specify the field to update and the new value.
    - To delete existing data, choose option 3 and enter the room number to be deleted.
    - To show particular room info, choose option 4 and enter the room number.
    - To end the task, choose option 5.

4. Note:
    - This program is intended for educational purposes and may require further enhancements for real-world usage.
    - Feel free to modify and expand the program according to your requirements.



-- QUERIES TO SET UP DATABASE --

-- Create the database
CREATE DATABASE Hotel_Paradise;

-- Use the database
USE Hotel_Paradise;

-- Create table for customer personal info
CREATE TABLE customer_personal_info (
    Name VARCHAR(255),
    Address VARCHAR(255),
    Room_Number INT,
    Age INT,
    Arrival DATE,
    Booking DATE,
    Departure DATE
);

-- Create table for customer stay info
CREATE TABLE customer_stay_info (
    Room_Number INT,
    No_Of_Days INT,
    Hotel_Price INT,
    Food_Price INT,
    Service_Cost INT,
    Total_Cost INT
);

