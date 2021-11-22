<center>  <h1> 🚘 Car Hire System 🚘 </h1></center>
## FULL ERD
![img.png](img.png)

### Invoice
![img_1.png](img_1.png)
>    CREATE TABLE Invoice (id int PRIMARY KEY, booking_id int , created_at date , is_paied BOOLEAN, FOREIGN KEY (booking_id) REFERENCES Booking (id) )

### Booking
![img_2.png](img_2.png)
> CREATE TABLE Booking (id int PRIMARY KEY AUTO_INCREMENT, customer_id int , car_id int, hier_date date, return_date date, FOREIGN KEY (customer_id) REFERENCES Customer (id), FOREIGN KEY (car_id) REFERENCES Car (car_id) );

### Car
![img_3.png](img_3.png)
>CREATE TABLE Car (car_id int PRIMARY key AUTO_INCREMENT , car_model varchar(30) NOT null, car_type ENUM('samll','family','van') not null , car_price FLOAT not null )

### Customer
![img_4.png](img_4.png)
> CREATE TABLE Customer (id int PRIMARY key AUTO_INCREMENT, full_name varchar(255) not null UNIQUE, phone varchar(255) , address varchar(255))

---------------------------------------------------------
# Postman result
![img_5.png](img_5.png)
> add customer

![img_6.png](img_6.png)
> get all customer

![img_8.png](img_8.png)
> get one customer

![img_7.png](img_7.png)
> delete customer

![img_9.png](img_9.png)
> edit customer data

<center>Thank you</center>


