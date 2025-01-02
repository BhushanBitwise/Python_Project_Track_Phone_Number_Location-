# from test import number

from datetime import datetime
import phonenumbers
from phonenumbers import geocoder
import folium
import mysql.connector 
#  connecter ek class ahe  ani mysql ha module ahe 

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Track_Phone_Location"
        )
#  connect() method hi connector class chi method ahe 
#   connect(host_name , use_name , password, database_name) aase 4parameter ahe 
#               4th parameter optional ahe.
 
    cursor= mydb.cursor() 



    key="65e0fc7ee763476288445288bf9d41f3"

    number=input("enter a Mobile Number with contry code :")
    check_number=phonenumbers.parse(number)
    number_location=geocoder.description_for_number(check_number,"en")
    print("mobile no: "+number)
    print(number_location)

    from phonenumbers import carrier
    service_provider= phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider,"en"))
    serv_pro_name   = carrier.name_for_number(service_provider,"en")
    # serv_pro_name --> ha service provider ch name ahe. 

    from opencage.geocoder import OpenCageGeocode

    geocoder=OpenCageGeocode(key)

    query= str(number_location)
    result=geocoder.geocode(query)
    lat=result[0]['geometry']['lat']
    lng=result[0]['geometry']['lng']

    lat1=str(result[0]['geometry']['lat'])# str madhe conver kel latitude
    lng1=str(result[0]['geometry']['lng'])# str madhe conver kel longitude

    print(lat,lng)

    map_location=folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=number_location).add_to(map_location)
    map_location.save("mylocation.html")



 # Step 2: Prepare the SQL INSERT statement
    insert_query = """
    INSERT INTO Phone_Data (mob_no, country, service_provider, latitude_longitude, current_date_time)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Step 3: Provide the data to insert
    data_to_insert = (
        number,                # Mobile number
        number_location,       # Country
        serv_pro_name,         # Service provider
         lat1 +"  "+ lng1 ,    # Latitude and longitude
        datetime.now()       # Current date and time
    )

# Step 4: Execute the query
    cursor.execute(insert_query, data_to_insert)
    
    # Commit the transaction
    mydb.commit()
    print("Data inserted successfully!")
    
except mysql.connector.Error as error:
    print(f"Failed to insert data: {error}")
    
finally:
    # Step 5: Close the connection
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed.")




# +60 123456789 (Malaysia)

# +62 8123456789 (Indonesia)

# +63 9123456789 (Philippines)

# +65 81234567 (Singapore)

# +64 212345678 (New Zealand)

# +52 5512345678 (Mexico)...

# +66 812345678 (Thailand)...

# +90 5321234567 (Turkey)

# +31 612345678 (Netherlands)

# +41 791234567 (Switzerland)

# +32 491234567 (Belgium)

# +30 6912345678 (Greece)

# +48 501234567 (Poland)

# +353 851234567 (Ireland)

# +372 51234567 (Estonia)

# +1 8761234567 (Jamaica)

# +974 50123456 (Qatar)

# +971 501234567 (UAE)

# +961 71234567 (Lebanon)

# +218 912345678 (Libya)

# +964 7812345678 (Iraq)

# +98 9123456789 (Iran)

# +880 1712345678 (Bangladesh)

# +92 3012345678 (Pakistan)

# +54 91123456789 (Argentina)

# +56 912345678 (Chile)

# +57 3112345678 (Colombia)

# +58 4123456789 (Venezuela)

# +94 712345678 (Sri Lanka)

# +82 1023456789 (South Korea)

# +1 2421234567 (Bahamas)

# +1 8091234567 (Dominican Republic)

# +505 81234567 (Nicaragua)

# +591 71234567 (Bolivia)

# +593 991234567 (Ecuador)

# +599 951234567 (Curaçao)

# +975 17123456 (Bhutan)

# +676 7712345 (Tonga)

# +675 71234567 (Papua New Guinea)

# +1 7211234567 (Sint Maarten)

# +376 312345 (Andorra)

# +850 1912345678 (North Korea)

# +420 601234567 (Czech Republic)

# +356 99123456 (Malta)

# +212 612345678 (Morocco)

# +216 20123456 (Tunisia)

# +62 82123456789 (Indonesia)

# +501 61234567 (Belize)

# +503 70123456 (El Salvador)

# +505 84234567 (Nicaragua)

# +509 37123456 (Haiti)

# +672 312345 (Norfolk Island)

# +679 7012345 (Fiji)

# +678 5912345 (Vanuatu)

# +692 7012345 (Marshall Islands)

# +960 7312345 (Maldives)

# +853 66123456 (Macau)

# +880 1912345678 (Bangladesh)

# +267 71123456 (Botswana)

# +233 501234567 (Ghana)

# +225 70123456 (Ivory Coast)

# +244 912345678 (Angola)

# +255 621234567 (Tanzania)

# +258 821234567 (Mozambique)

# +263 771234567 (Zimbabwe)

# +675 79123456 (Papua New Guinea)

# +689 89123456 (French Polynesia)

# +93 701234567 (Afghanistan)

# +95 921234567 (Myanmar)

# +880 1712345679 (Bangladesh)

# +237 671234567 (Cameroon)

# +250 781234567 (Rwanda)

# +256 701234567 (Uganda)

# +960 99123456 (Maldives)

# +597 8312345 (Suriname)

# +592 6212345 (Guyana)

# +675 75123456 (Papua New Guinea)

# +690 7912345 (Tokelau)

# +1 7841234567 (Saint Vincent and the Grenadines)

# +676 8912345 (Tonga)

# +1 3451234567 (Cayman Islands)

# +670 78123456 (Timor-Leste)

# +681 7212345 (Wallis and Futuna)

# +682 5612345 (Cook Islands)