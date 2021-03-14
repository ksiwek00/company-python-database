# moduł zawierający klasę opisującą firmę

class Company():
    """klasa opisująca dowolny samochód"""

    def __init__(self,companyName, postcode, city, street, contact, mail, phoneNumber):
        """inicjalizacja atrybutów samochodu"""
        self.companyName = companyName
        self.postcode = postcode
        self.city = city
        self.street = street
        self.contact = contact
        self.mail = mail
        self.phoneNumber = phoneNumber