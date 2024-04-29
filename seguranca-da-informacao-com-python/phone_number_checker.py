import phonenumbers

from phonenumbers import geocoder

phone = input("Digitel o número de telefone no formato +55XXYYYYZZZZ: ")

# indica que a String é um número de telefone
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))