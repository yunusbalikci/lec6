print("Welcome in Yunus’ store.")

product_name = input("Product Name")
product_price =float(input("Price:"))
email =input("Email:")
phone =input("Phone")

product_price = float(product_price)

tax = 0.23
gross_price = (product_price * tax) + product_price

print("Your Basket:")
print(product_name,gross_price,email,phone)

try:
    product_name = input("Product Name:")
    product_price = float(input("product price"))
    email = input("Email:")
    phone = input("Phone:")
    gross_price = (product_price * tax) + product_price
    print("Your Basket:")
    print("Product Name:","Price","Email","Phone")
    print(product_name, gross_price, email, phone)
except:
    print("Process interrupted. Bad data type.")
    exit()


    print((not (x < 15 and y >= 3))
    print((x >= 15 or y < 3))
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

