
# Python Project Track Phone Number Location

"This project is aimed at tracking the location of a phone number using Python 
programming. It integrates tools and APIs to determine the approximate location, country, 
and carrier details associated with a given phone number."




## Step 1: Setup the Environment

1.Install Required Python Libraries



```bash
  pip install phonenumbers folium mysql-connector-python opencage

```
2.Setup MySQL Database
```bash
CREATE DATABASE Track_Phone_Location;

```
3: Use the newly created database
```bash
USE Track_Phone_Location;
```

4.Create the table
```bash
CREATE TABLE Phone_Data (
    mob_no VARCHAR(15) NOT NULL,  
    country VARCHAR(50),                  
    service_provider VARCHAR(100),          
    latitude_longitude VARCHAR(50),        
    current_date_time DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (mob_no)                   
);
```
## Step 2: Create Python script:
go to GitHub and copy the code of the main.py file and create main.py file in your code editor and main.py in it paste the file code.





## 🔗 Links
click this link and go to main.py file 

https://github.com/BhushanBitwise/Python_Project_Track_Phone_Number_Location-/blob/3eb2c6c023185e4bccd57fabb6fcde9576418b4d/main.py

# Step 3: Running the Script
1.Run the script:
```bash
python main.py
```

2.Enter the mobile number in the specified format, and the script will execute, saving the data to the database and generating a map.
