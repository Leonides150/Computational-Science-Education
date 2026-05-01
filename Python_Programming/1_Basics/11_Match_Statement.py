#Match statement is a new feature in Python 3.10 that allows you to compare a value against a series of patterns and execute code 
#based on which pattern matches. 
http_status = 550

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad Request')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else:
    print('Unknown')

match  http_status: 
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 404:
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknown')
