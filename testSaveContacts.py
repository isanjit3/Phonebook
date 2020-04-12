import csv
toCSV = [
    {
        "name": "Sanjit Thangarasu",
        "email": "isanjit3@gmail.com",
        "number": "(240)586-2284"
    },
    {
        "name": "Hema Ponnuvel",
        "email": "hemappriya@gmail.com",
        "number": "(240)274-8790"
    },
    {
        "name": "Thangarasu Palanisamy",
        "email": "thanga.palanisamy@gmail.com",
        "number": "(240)274-9814"
    }
]
keys = ['name', 'email', 'number']
print(keys)
with open('contacts.txt', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)