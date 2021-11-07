from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flipbot.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance_left = db.Column(db.Integer)
    spending_done= db.Column(db.Integer)
    last_order_id= db.Column(db.Integer) # this get updated with the last ordered product
    
    
class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    shipping_address = db.Column(db.String(120),nullable=False) #shipping address
    last_checkpoint_of_ordered_product = db.Column(db.String(120)) # used for tracking order
    #last_order_id= db.Column(db.Integer) # this get updated with the last ordered product
    

# this model is used for establishing a realtionship between user and its orders
class Mapping_orders_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email=db.Column(db.String(120))
    order_id = db.Column(db.Integer, unique=True)
    
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer)

# this model is used for establishing a realtionship between user and its prducts in his cart
class Mapping_cart_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email=db.Column(db.String(120))
    product_id = db.Column(db.Integer)


# ecommerce 

class Product_categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120), unique=True, nullable=False)
    category_desc =  db.Column(db.String(120), unique=True)
    category_count= db.Column(db.Integer)
    
class Product_clothing(db.Model):
    cloth_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    desc =  db.Column(db.String(120), unique=True)
    price= db.Column(db.Integer)
    discount_percentage=db.Column(db.Integer) 
    
class Product_gadgets(db.Model):
    gadget_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    desc =  db.Column(db.String(120), unique=True)
    price= db.Column(db.Integer)
    discount_percentage=db.Column(db.Integer) 

class Product_shoes(db.Model):
    shoe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    desc =  db.Column(db.String(120), unique=True)
    price= db.Column(db.Integer)
    discount_percentage=db.Column(db.Integer) 
    
    
#db.create_all()

# user table
u1 = User(email='parasmadan555@gmail.com', password='123paras',spending_done=1000, balance_left=2000,last_order_id=2)
u2=  User(email='yashwant@gmail.com', password='123par',spending_done=6000, balance_left=2000,last_order_id=3)
u3=  User(email='wadhwa@gmail.com', password='123par45',spending_done=9000, balance_left=2000,last_order_id=1)
u4=  User(email='raghav@gmail.com', password='123par455',spending_done=104000, balance_left=2000,last_order_id=5)
u5=  User(email='parasmadan123@gmail.com', password='123par',spending_done=6000, balance_left=2000,last_order_id=4)



# order table
o1 = Orders(name='Adidas shoes', shipping_address='Link Road Saharanpur ', last_checkpoint_of_ordered_product='Guragon Facility')
o2 = Orders(name='One Plus Nord 2', shipping_address='Thapar University Patiala ', last_checkpoint_of_ordered_product='Ambala Facility')
o3 = Orders(name='Philips Trimmer', shipping_address='Rohini Sec-13 Delhi ', last_checkpoint_of_ordered_product='Meerut Facility')
o4 = Orders(name='Woolen Jacket', shipping_address='Raj Colony Jaipur ', last_checkpoint_of_ordered_product='Udaipur Facility')
o5 = Orders(name='Power Bank 1000 mh', shipping_address='Sector 25 Panipat', last_checkpoint_of_ordered_product='Noida Facility')

# mapping users to orders
mou1 = Mapping_orders_user(user_email='raghav@gmail.com', order_id=2)
mou2 = Mapping_orders_user(user_email='yashwant@gmail.com', order_id=4)
mou3 = Mapping_orders_user(user_email='parasmadan123@gmail.com', order_id=1)
mou4 = Mapping_orders_user(user_email='wadhwa@gmail.com', order_id=5)
mou5 = Mapping_orders_user(user_email='parasmadan555@gmail.com', order_id=3)

#cart 
c1 = Cart(product_id=3)
c2 = Cart(product_id=2)
c3 = Cart(product_id=1)


#Mapping_cart_user
mcu1=Mapping_cart_user(user_email='raghav@gmail.com', product_id=2)
mcu2=Mapping_cart_user(user_email='parasmadan555@gmail.com', product_id=1)
mcu3=Mapping_cart_user(user_email='yashwant@gmail.com', product_id=3)


# product category add
p1=Product_categories(category_name='Shoes',category_desc='Shoes of all brands including Adidas , Reeebok , Adda, Woodland and many more',category_count=50)
p2=Product_categories(category_name='Gadgets',category_desc='All sorts of gadgets including Mobile Phones , laptops , Chargers and etc',category_count=170)
p3=Product_categories(category_name='Clothes',category_desc='Clothes of all brands and for all Men,Women and Childern',category_count=500)
p4=Product_categories(category_name='Home Appliances',category_desc='All home appliances at one place',category_count=30)
p5=Product_categories(category_name='Sports',category_desc='Bats, Footall and all sports at a single place',category_count=80)




    
# product category add
p1=Product_gadgets(name='Zara Jacket XL',discount_percentage=20,price=4999)
p2=Product_clothing(name='Woodland Lower',discount_percentage=45,price=2499)
p3=Product_clothing(name='Crop Top',discount_percentage=50,price=1899)
p4=Product_clothing(name='Levis Jeans ',discount_percentage=18,price=3999)
p5=Product_clothing(name='Leather Jacket',discount_percentage=30,price=9999)


pg1=Product_gadgets(name='One plus Nord 2',discount_percentage=20,price=4999)
pg2=Product_gadgets(name='Philips Trimmer',discount_percentage=45,price=2499)
pg3=Product_gadgets(name='Samsung 30W charger',discount_percentage=50,price=1899)
pg4=Product_gadgets(name='Controller Joystick',discount_percentage=18,price=3999)
pg5=Product_gadgets(name='Asus Tuf Laming laptop',discount_percentage=30,price=99999)


ps1=Product_shoes(name='Woodland High Sole',discount_percentage=20,price=4999)
ps2=Product_shoes(name='Adda Sports Shoes',discount_percentage=45,price=2499)
ps3=Product_shoes(name='SparX Ladies Sandal',discount_percentage=50,price=1899)
ps4=Product_shoes(name='Bata Comfortable Shoes',discount_percentage=18,price=3999)
ps5=Product_shoes(name='Woodland Trekking Shoes',discount_percentage=30,price=9999)


db.session.add(ps5)
db.session.commit()




























