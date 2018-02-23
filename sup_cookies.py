json = {
    "domain": "www.supremenewyork.com",
    "expirationDate": 1529257680,
    "hostOnly": True,
    "httpOnly": False,
    "name": "address",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "id": 12
}

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

json["value"] = value

outfile = open("cookie.txt", "w")

outfile.write(str(json).replace("'", '"').replace("True,", "true,").replace("False,", "false,"))

print("Cookie generated! Check cookie.txt and copy it to your browser using EditThisCookie (or any other other cookie editor)")
