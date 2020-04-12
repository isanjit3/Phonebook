contacts = [
    {
        "name": "Tom", 
        "email": "tom@gmail.com"
    },
    {
        "name": "Mark", 
        "email": "mark@gmail.com"
    },
    {
        "name": "Pam",
        "email": "pam@gmail.com"
    }
]

var = next((item for item in contacts if item["email"] == "pam@gmail.com"), None)
lamb = list(filter(lambda contact: contact["email"] == "pam@gmail.com", contacts))

print(var)
print(lamb)