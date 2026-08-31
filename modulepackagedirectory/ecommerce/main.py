from products.product import product_details
from products.inventory import check_stock
from customers.customer import customer_details
from customers.address import customer_address
from orders.order import create_order
from orders.status import order_status
from payments.payment import make_payment
from payments.invoice import generate_invoice

product = input("Enter product: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

customer = input("Enter customer name: ")
city = input("Enter city: ")

product_details(product, price)
print("Stock:", check_stock(quantity))

customer_details(customer)
customer_address(city)

create_order(product, quantity)
print(order_status())

amount = price * quantity
make_payment(amount)
generate_invoice(amount)