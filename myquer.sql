-- Step 1: Create the database
CREATE DATABASE Track_Phone_Location;

-- Step 2: Use the newly created database
USE Track_Phone_Location;

-- Step 3: Create the table
CREATE TABLE Phone_Data (
    mob_no VARCHAR(15) NOT NULL,            -- Mobile number, with a max length of 15
    country VARCHAR(50),                    -- Country name
    service_provider VARCHAR(100),          -- Service provider name
    latitude_longitude VARCHAR(50),         -- Coordinates in latitude,longitude format
    current_date_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- Current date and time with default value
    PRIMARY KEY (mob_no)                    -- Setting mob_no as the primary key
);