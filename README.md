# Vendor Management System with Performance Metrics
## Project Setup Instructions

### 1. follow these instructions to run the application
```bash
# First you need to clone the repository
step-1. git clone https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment.git

step-2.  Go to the directory FatMug-Django-Developer-Assignment

step-3. Open terminal and run python -m venv venv
# Now you need to activate a virtula invornment using the following command
step-3   source venv/bin/activate
#  Your Virtual is now activated
step-5. now open the project using vs code or just write code . in the terminal, open in the directory of the project

step-6. now open a new terminal and write pip install -r requirements.txt

# Now you are all set to runing the application 
step-4  (i) # First you need to run the migration commands
            i.  -> python manage.py makemigrations 
            ii. -> python manage.py migrate
            
#  creating a superuser
step-6 python manage.py createsuperuser 
#  Enter  your details once it says superuser created successfully .. You are done
# now you can run the application using the following command
step-5 python manage.py runserver
# Now you need to be a logged in user to view the project
step-7 go to the admin url and login http://127.0.0.1:8000/admin/

step-8 Once logged in You can Navigate through all the endpoints

```

# Introduction
This Django project implements a Vendor Management System with performance metrics tracking, I have used the Django Rest Framework to Create Apis .

## Main Features

### Vendor Profile Management
  Here pk is the vendor_id
- **Model Design:** Vendor information, including name, contact details, address, and a unique vendor code.
- **API Endpoints:**
  - `GET /api/vendors/`: List all vendors.
  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/{pk}/`: Retrieve a specific vendor's details.
  - `PUT /api/vendors/{pk}/`: Update a vendor's details.
  - `DELETE /api/vendors/{pk}/`: Delete a vendor.

### Purchase Order Tracking
  Here pk is the Puchase Order id , <h4>Both Vendor and Purchase Have pk value of their own<h4>
- **Model Design:** Purchase order details, including PO number, vendor reference, order date, items, quantity, and status.
- **API Endpoints:**
  - `GET /api/purchase_orders/`: List all the Purchase Order
  - `GET /api/purchase_orders/?vendor=pk`: List all purchase orders with an option to filter by vendor.
  - `POST /api/purchase_orders/`: Create a purchase order.
  - `GET /api/purchase_orders/{pk}/`: Retrieve details of a specific purchase order.
  - `PUT /api/purchase_orders/{pk}/`: Update a purchase order.
  - `DELETE /api/purchase_orders/{pk}/`: Delete a purchase order.

### Vendor Performance Calculations
- **Metrics:** On-Time Delivery Rate, Quality Rating, Response Time, Fulfillment Rate.
- **Model Design:** Vendor model includes fields for performance metrics.
- **API Endpoints:**
  - `GET /api/vendors/{pk}/performance/`: Retrieve a vendor's performance metrics.

## Data Models
1. **Vendor Model:**
   - Fields: name, ,contact_details, ,address ,vendor_code ,on_time_delivery_rate ,quality_rating_avg ,average_respose_time ,fulfillment_rate

2. **Purchase Model:**
    - Fields:  po_number ,vendor ,order_date ,delivery_date ,quantity ,status ,items ,quality_rating ,issue_date ,acknowledgement_date

3. **Historical Performance Model:**
   - Fields: vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate.

## Backend Logic
- **On-Time Delivery Rate:** Calculated on Purchase status change to 'completed'.
- **Quality Rating Average:** Updated upon completion of each Purchase with a provided quality rating by the customer.
- **Average Response Time:** Calculated on PO acknowledgment by the vendor by going through the endpoint of acknowledege purchase order.
- **Fulfillment Rate:** Calculated on any change in Purchase status.

## API Endpoint Implementation
- `GET /api/vendors/{pk}/performance`: Retrieves calculated performance metrics for a specific vendor.
- `POST /api/purchase_orders/{pk}/acknowledge`: Endpoint for vendors to acknowledge POs.


<h3>Some ScreenShots</h3>
<h4>Purchase Api</h4>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/1.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/2.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/3.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/4.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/5.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/6.png
<br>
<br>
<h4> Vendor Api </h4>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Vendor/1.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Vendor/2.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Vendor/3.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Vendor/4.png
<br>
https://github.com/Pravin-Kumar-21/FatMug-Django-Developer-Assignment/blob/master/Live%20Pictures/Purchase/7.png
<br>
