import cgi, cgitb 

# Create instance of FieldStorage
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('data')
print(first_name)