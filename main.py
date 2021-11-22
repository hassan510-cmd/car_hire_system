from flask import Flask
from flask import  request

from mysql import connector
from datetime import datetime

app = Flask(__name__)

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'Car_Hire',
    'raise_on_warnings': True
}

def open_connection():
    connection = connector.connect(**config)
    return connection


def close_connection(connection):
    connection.close()


@app.route('/get-customer/<int:pk>', methods=['GET'])
def get_customer(pk):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT id,full_name, phone,address FROM Customer where id = {pk}''')
    result = cursor.fetchall()
    close_connection(connection)
    print(result)
    return {"get": result}


@app.route('/add-customer', methods=['POST'])
def add_customer():
    fullname = request.form.get('full_name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(
        f'''insert into Customer (`full_name`, `phone`, `address`)     values(    '{fullname}',    '{phone}','    {address}')''')
    connection.commit()
    close_connection(connection)
    return "add"


@app.route('/edit-customer/<int:pk>', methods=['PATCH'])
def edit_customer(pk):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(
        f'''
        update  Customer set full_name ='{request.form.get("full_name")}',        phone='{request.form.get('phone')}',
         address='{request.form.get('address')}'        where id = {pk}
            ''')
    connection.commit()
    close_connection(connection)
    return "edit"


@app.route('/del-customer/<int:pk>', methods=['DELETE'])
def del_customer(pk):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(f'''DELETE  FROM Customer where id = {pk}''')
    connection.commit()
    close_connection(connection)
    return "del"


@app.route('/all', methods=['GET'])
def get_all():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT id,full_name, phone,address FROM Customer ''')
    result = cursor.fetchall()
    close_connection(connection)
    print(result)
    return {"all": result}


@app.route('/book-car', methods=['POST'])
def create_booking():
    # print(request.form.get('hire_date'))
    hire_date = datetime.strptime(request.form.get('hire_date'), '%Y-%m-%d')
    return_date = datetime.strptime(request.form.get('return_date'), '%Y-%m-%d')
    # return_date=datetime(request.form.get('return_date'))
    if (return_date - hire_date).days > 7:
        return {'error': "can't rent car for more than 7 days"}
    elif (return_date - hire_date).days < 0:
        return {'error': "invalid rent date must be after hire"}

    connection = open_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f'''INSERT INTO Booking(customer_id, car_id, hire_date, return_date)
                VALUES('{request.form.get('customer_id')}',
                '{request.form.get('car_id')}',
                '{request.form.get('hire_date')}',
                '{request.form.get('return_date')}')
                   ''')
        connection.commit()

    except Exception as ex:
        return {"message": "it seem to be that this customer already rent this car"}
    close_connection(connection)
    return {"message": "yes"}

@app.route('/save-invoice',methods=['POST'])
def create_invoice():
    connection=open_connection()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        insert into Invoice(booking_id,created_at,is_paied)
         values (
         '{request.form.get('booking_id')}',
        '{request.form.get('created_at')}',
         '{request.form.get('is_paied')}')""")
    connection.commit()
    close_connection(connection)
    return {"message":"created successfully"}

if __name__ == '__main__':
    app.run(debug=True)
