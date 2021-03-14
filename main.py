# baza kontrachentów - plik główny

from companyModule import Company

companies = []

database = open("database.txt","r")
for line in database:
    companyName, postcode, city, street, contact, mail, phoneNumber = line.split("|")
    company = Company(companyName, postcode, city, street, contact, mail, phoneNumber)
    companies.append(company)
database.close()


def addEntry():
    """dodanie firmy do bazy danych"""

    finish = 0
    print('\nDodawanie firmy do bazy danych. Wpisz "CANCEL" żeby anulować')
    while finish == 0:
        companyName = input("Nazwa firmy: ")
        if companyName.lower() == "cancel":
            break

        postcode = input("Kod pocztowy: ")
        if postcode.lower() == "cancel":
            break

        city = input("Miasto: ")
        if city.lower() == "cancel":
            break

        street = input("Ulica: ")
        if street.lower() == "cancel":
            break

        contact = input("Osoba kontaktowa: ")
        if contact.lower() == "cancel":
            break

        mail = input("E-mail: ")
        if mail.lower() == "cancel":
            break

        phoneNumber = input("Numer telefonu: ")
        if phoneNumber.lower() == "cancel":
            break

        company = Company(companyName, postcode, city, street, contact, mail, phoneNumber)
        companies.append(company)
        saveDatabase()

        see = input("\nDodano wpis o firmie " + companyName + ". Czy chcesz go zobaczyć? (T/N): ")
        finish = 0
        while finish == 0:
            if see == "T" or see == "t":
                print("\nNazwa firmy: " + companyName)
                print("Kod pocztowy: " + postcode)
                print("Miasto: " + city)
                print("Ulica: " + street)
                print("Osoba kontaktowa: " + contact)
                print("E-mail: " + mail)
                print("Numer telefonu: " + phoneNumber)
                finish = 1
            elif see == "N" or see == "n":
                finish = 1
            else:
                see = input("Błędne dane. Wpisz T (tak) albo N (nie): ")

def searchEntry():
    """wyszukiwanie firmy po nazwie"""

    companyName = input("\nWpisz nazwę firmy do wyszukania: ")
    found = 0
    for company in companies:
        if company.companyName == companyName:
            found = 1
            see = input("\nZnaleziono wpis o firmie " + companyName + ". Czy chcesz go zobaczyć? (T/N): ")
            finish = 0
            while finish == 0:
                if see == "T" or see == "t":
                    print("\nNazwa firmy: " + company.companyName)
                    print("Kod pocztowy: " + company.postcode)
                    print("Miasto: " + company.city)
                    print("Ulica: " + company.street)
                    print("Osoba kontaktowa: " + company.contact)
                    print("E-mail: " + company.mail)
                    print("Numer telefonu: " + company.phoneNumber)
                    finish = 1
                elif see == "N" or see == "n":
                    finish = 1
                else:
                    see = input("Błędne dane. Wpisz T (tak) albo N (nie): ")
    if found == 0:
        print("Nie znaleziono wpisów na temat tej firmy. Spróbuj innej nazwy.")

def deleteEntry():
    """usuwanie wejścia o firmie o podanej nazwie"""
    companyName = input("\nWpisz nazwę firmy do wyszukania i usunięcia: ")
    found = 0
    for company in companies:
        if company.companyName == companyName:
            found = 1
            see = input("\nZnaleziono wpis o firmie " + companyName + ". Czy na pewno chcesz go usunąć? (Usuń/Anuluj): ")
            finish = 0
            while finish == 0:
                if see.lower() == "usuń":
                    deleteIndex = companies.index(company)
                    companies.pop(deleteIndex)
                    print("Usunięto wpis")
                    saveDatabase()
                    finish = 1
                elif see.lower() == "anuluj":
                    print("Anulowano")
                    finish = 1
                else:
                    see = input("Błędne dane. Wpisz Usuń albo Anuluj: ")
    if found == 0:
        print("Nie znaleziono wpisów na temat tej firmy. Spróbuj innej nazwy.")

def displayDatabase():
    """wyświetla nazwy wszystkich firm"""
    i = 0
    print("Firmy figurujące obecnie w bazie danych:\n")
    for company in companies:
        i = i + 1
        print("\t" + str(i) + ". " + str(company.companyName) + "")

def saveDatabase():
    """zapisuje obecny stan bazy danych do pliku zewnętrznego"""
    file = open("database.txt", "w+")
    i = 0
    for company in companies:
        i = i + 1
        file.write(company.companyName + "|" + company.postcode + "|" + company.city + "|" + company.street + "|" + company.contact + "|" + company.mail + "|" + company.phoneNumber + "\n")
    file.close()

def menu():
    """obsługa menu"""
    choiceCheck = 0
    while choiceCheck == 0:
        choice = input("______________________________\n\nWybierz akcję:\n\t1 - Dodaj wpis\n\t2 - Usuń wpis\n\t3 - Wyszukaj wpis\n\t4 - Wypisz bazę danych\n\t5 - Zakończ pracę programu\n")
        if choice == "1":
            print("______________________________")
            addEntry()
        elif choice == "2":
            if companies == []:
                print("\nBaza danych jest pusta. Nie można usunąć wpisu, który nie istnieje!")
            else:
                print("______________________________")
                deleteEntry()
        elif choice == "3":
            if companies == []:
                print("\nBaza danych jest pusta. Nie można wyszukać wpisu, który nie istnieje!")
            else:
                print("______________________________")
                searchEntry()
        elif choice == "4":
            if companies == []:
                print("\nBaza danych jest pusta.")
            else:
                print("______________________________")
                displayDatabase()
        elif choice == "5":
            print("\nDo widzenia :)")
            choiceCheck = 1
        else:
            print("Błędne dane. Wpisz 1, 2, 3, 4, albo 5")

print("\nProjekt: Baza danych firm\n\tAutor: Krzysztof Siwek\n\tKlasa: 3IC")
menu()