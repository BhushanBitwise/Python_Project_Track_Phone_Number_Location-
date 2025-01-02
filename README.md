Creating the project step-by-step involves several tasks, including setting up the database, implementing the Python script, and configuring external libraries. Below are the steps to create this project:

Step 1: Setup MySQL Database
1.Install MySQL (if not already installed):
On Ubuntu: sudo apt update && sudo apt install mysql-server
On Windows: Download and install from the MySQL website.

2.Create a Database:
.sql
CREATE DATABASE Track_Phone_Location;

3.Create a Table:
.sql
USE Track_Phone_Location;

CREATE TABLE Phone_Data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mob_no VARCHAR(15),
    country VARCHAR(50),
    service_provider VARCHAR(100),
    latitude_longitude VARCHAR(50),
    current_date_time DATETIME
);

Step 2: Python Script Setup
1.Install required Python libraries: 
pip install phonenumbers folium opencage-python mysql-connector-python

2.Create Python script: go to GitHub and copy the code of the main.py file and create main.py file in your code editor and main.py in it paste the file code.

Step 3: Running the Script
1.Run the script:
 python main.py
 
2.Enter the mobile number in the specified format, and the script will execute, saving the data to the database and generating a map.



