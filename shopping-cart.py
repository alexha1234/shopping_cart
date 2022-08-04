# shopping_cart.py
import pandas as pd
import io
import requests

link = "https://raw.githubusercontent.com/alexha1234/shopping_cart/main/Data/products.csv"
csv=requests.get(link).content
df=pd.read_csv(io.StringIO(csv.decode('utf-8')))
products = df.to_dict(orient='records')
# This code pulled from https://stackoverflow.com/questions/64187630/creating-a-list-of-dictionaries-from-a-url-that-points-to-a-csv
#starter code provided

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
# using datetime module
import datetime
from gettext import install;
ct = datetime.datetime.now()
# ct stores current time

selected_products = [] 
subtotal = 0

while True:
    selected_id = input("Please input a product id, or 'DONE': " )
    if selected_id.upper() == "DONE":
        break # break out of the while loop 
    else:
        #print("LOOKING UP PRODUCT", selected_id)
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0] # this will trigger an IndexError if there are no matching products
        selected_products.append(matching_product)
        subtotal = subtotal + matching_product["price"]
        # continue the while loop
tax_rate = input("PLEASE INPUT TAX RATE: ")
print("---")
print("THANK YOU FOR SHOPPING AT AL'S GROCERY!")
print ("123 Main St")
print("123-456-789")
print("---")
print (ct)
print("---")
print("    ")


for p in selected_products:
    print (p["name"], to_usd(p["price"]))
print("---")
print("   ")
print("SUBTOTAL:", to_usd(subtotal))
tax = float(subtotal) * float(tax_rate)
print("TAX:", to_usd(tax))
total = tax + subtotal
print("TOTAL:", to_usd(total))
print("---")
print("   ")
print("THANK YOU, PLEASE COME AGAIN SOON")

'''
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("alexander.n.hartley@gmail.com")  # Change to your verified sender
to_email = (To("alexander.n.hartley@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
'''