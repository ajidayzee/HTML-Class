print('Please enter the following information: ')
print()
# Basic Information
first = input('First name:')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number:')
# Additional Information
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
month = input('Starting Month: ')
training = input('Completed additional trainig? ')
print('\nThe ID card is: ')
print('----------------------------------------------')
print(last.upper(), first.capitalize())
print(job_title.title())
print('ID:'+id_number)
print()
print(email.lower())
print(phone)
print('----------------------------------------------')
print()
print('Hair:'+hair_color+ '               ' 'Eyes:' +eye_color)
print('Month:'+month+ '          ' 'Training:'+training)
print('----------------------------------------------')