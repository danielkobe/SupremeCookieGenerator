
print("========= Shipping Info =========")
name = input("Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State (initials): ")
zip_code = input("Zip Code: ")
country = input("Country (USA or CANADA): ")
email = input("Email: ")
phone_number = input("Phone number (no dashes): ")

value = name.replace(" ", "+") + "%7C" + address.replace(" ", "+") + "%7C%7C" + city.replace(" ", "+") + "%7C" + state + "%7C" + zip_code + "%7C" + country + "%7C" + email.replace("@", "%40") + "%7C" + phone_number

cookie = str(json).replace("'", '"').replace("True,", "true,").replace("False,", "false,")
print("document.cookie=\"address=" + value + "\"")

print("Cookie generated! First go to http://www.supremenewyork.com/ then to the Chrome Developer Tools->Console, then past the cookie into the console and press enter.")
