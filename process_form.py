import cgi

# Parse the form data
form = cgi.FieldStorage()

# Get the value of the "name" field
name = form.getvalue("name")

# Get the value of the "email" field
email = form.getvalue("email")

# Print the form values
print("Content-Type: text/html")
print()
print("<html><body>")
print("Name:", name)
print("Email:", email)
print("</body></html>")
