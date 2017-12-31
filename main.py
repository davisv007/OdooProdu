import odoorpc

# Insert credentials below

URL = '172.104.29.204'
DB = 'odoo'
USERNAME = 'test@test.com'
PASSWORD = 'admin'


##########################


def main():
    name = input('Product name you would like to add?')
    x_asin = input('x_asin of the product you would like to add?')

    # Prepare the connection to the server
    odoo = odoorpc.ODOO(URL, port=8069)

    # Login
    odoo.login(DB, USERNAME, PASSWORD)

    # Check available databases
    # print(odoo.db.list())

    # Current user
    # user = odoo.env.user

    # print(user.name)            # name of the user connected
    env = odoo.env
    Product = env['product.product']
    Product.create({'name': name, 'x_asin': x_asin})  # creates a new record
    print('Record added successfully!')
    # Product.write(1,{'name': 'ksd','a_sin':'1234124'})           # edits an existing record

    # Test
    # x = [product.name for product in Product.browse(range(2, 43))]
    # heres the thing, why 43? checked the database and is says 28
    # took off the products filter and it says 37, so I'm not sure where this number is coming from
    # when I add an entry, it appears in the database, but it doesnt appear in the x list
    # I deleted the item with ID =1 , not sure how to assign ids , using an 'id' field doesnt work

    # print(x)
    # print(name in x) # i used this to check whether the name appears in x or not
    # returns false for create command and true for write command

    # TODO: add way to remove products
    # TODO: add way to view products without knowing ids/count


main()
