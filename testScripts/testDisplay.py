from operator import itemgetter

def displayContacts(data, keys, header=None, sort_by_key=None, sort_order_reverse=False):
    """Takes a list of dictionaries, formats the data, and returns
    the formatted data as a text table.

    Required Parameters:
        data - Data to process (list of dictionaries). (Type: List)
        keys - List of keys in the dictionary. (Type: List)

    Optional Parameters:
        header - The table header. (Type: List)
        sort_by_key - The key to sort by. (Type: String)
        sort_order_reverse - Default sort order is ascending, if
            True sort order will change to descending. (Type: Boolean)
    """
    # Sort the data if a sort key is specified (default sort order
    # is ascending)
    if sort_by_key:
        data = sorted(data,
                      key=itemgetter(sort_by_key),
                      reverse=sort_order_reverse)

    # If header is not empty, add header to data
    if header:
        # Get the length of each header and create a divider based
        # on that length
        header_divider = []
        for name in header:
            header_divider.append('-' * len(name))

        # Create a list of dictionary from the keys and the header and
        # insert it at the beginning of the list. Do the same for the
        # divider and insert below the header.
        header_divider = dict(zip(keys, header_divider))
        data.insert(0, header_divider)
        header = dict(zip(keys, header))
        data.insert(0, header)

    column_widths = []
    for key in keys:
        column_widths.append(max(len(str(column[key])) for column in data))

    # Create a tuple pair of key and the associated column width for it
    key_width_pair = zip(keys, column_widths)

    format = ('%-*s ' * len(keys)).strip() + '\n'
    formatted_data = ''
    for element in data:
        data_to_format = []
        # Create a tuple that will be used for the formatting in
        # width, value format
        for pair in key_width_pair:
            data_to_format.append(pair[1])
            data_to_format.append(element[pair[0]])
        formatted_data += format % tuple(data_to_format)
    return formatted_data

# Test

header = ['Name', 'E-mail', 'Phone Number']
keys = ['name', 'email', 'number']
sort_by_key = 'name'
data = [{
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
        }]

print (displayContacts(data, keys, header, sort_by_key))
print (displayContacts(data, keys, header, sort_by_key))
print (displayContacts(data, keys, header, sort_by_key))
print (displayContacts(data, keys, header, sort_by_key))
print (displayContacts(data, keys, header, sort_by_key))