import erppeek
from sys import argv

# Insert credentials below

URL = '172.104.29.204'
DB = 'odoo'
USERNAME = 'test@test.com'
PASSWORD = 'admin'

##########################

client = erppeek.Client(server='http://172.104.29.204:8069', db='odoo', user='test@test.com', password='admin',
                        verbose=True)

# when verbose is true you can see the commands that this library is entering,
# which can help you learn about the documentation

if len(argv)<2:
    name = input('Product Name:')
    x_asin = input('x_asin:')
else:
    print(argv)
    command = argv[1:]
    x_asin = command.pop() #assuming the x_asin is one word
    name=' '.join(command)
# print(name)
# print(x_asin)
#
# # can add more questions for fields like cost, sales price etc..
#
# prod = client.model('product.product')
# prod.create({'name': name, 'x_asin': x_asin})

print('Record added successfully!')

# Test
# x = [product.name for product in prod.browse(range(2,44))]
# print(x)
# print(name in x)
# same deal here i used this to check whether the name appears in x or not
# returns false for create command and true for write command not sure why
# TODO: add way to remove products
# TODO: add way to view products without knowing ids/count


# erppeek is also usable as a command line, by leaving the -m flag blank, it becomes interactive
# typing the following into your command prompt would achieve similar results
# erppeek --server=http://172.104.29.204:8069 -d odoo -u test@test.com -p admin --verbose
# prod = model('product.product')
# prod.create({ 'name': 'Test Produkt'})
# further reading: https://stackoverflow.com/questions/24742741/how-can-i-create-an-odoo-openerp-product-instance-in-python-interactively
