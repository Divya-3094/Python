products = [ 
{"id": 1, "name": "Laptop", "price": 45000}, 
{"id": 2, "name": "Smartphone", "price": 15000}, 
{"id": 3, "name": "Headphones", "price": 2000}, 
{"id": 4, "name": "Keyboard", "price": 1200}, 
{"id": 5, "name": "Mouse", "price": 800}, 
{"id": 6, "name": "Charger", "price": 500}, 
{"id": 7, "name": "USB Cable", "price": 300}, 
{"id": 8, "name": "Backpack", "price": 2500} 
] 

def viewproducts():
    print("view products is executed")
    for p in products:
        print(f"product name is {p['name']} and price is {p['price']}")
#here we have mainly three conditions
# 1. check the cart whether the product is there or not
# 2. if the product was already in cart we need to update it
# 3. if we get the new product into the cart    
def addToCart(products,cart,product_id,quantity):
    product=None
    for items in products:
        if items['id']==product_id:
            product=items
            break
        if not products:
            print('the cart is empty')

    for item in cart:
        if item['id']==product_id:
            item['quantity']+=quantity

    new_items={
        "id":product["id"],
        'name':product['name'],
        'price':product['price'],
        'quantity':quantity
    }       
    cart.append(new_items())
    print("add to cart is executed")

def viewCart():
    print("view cart is executed")
def updateCart():
    print("update cart is executed")
def removeFromCart():
    print("remove cart is executed")
def checkout():
    print("checkout cart is executed")            
    
def menu():
    ip=int(input("enter choice: "))
    if ip == 1:
        viewproducts()
    elif ip == 2:
        addToCart()
    elif ip == 3:
        viewCart()
    elif ip == 4:
        updateCart()
    elif ip == 5:
        removeFromCart()
    elif ip == 6:
        checkout()
    else:
        print('invalid choice')
menu()                        
           

