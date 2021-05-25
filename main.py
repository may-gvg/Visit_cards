

# Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker, którą opisaliśmy powyżej.
# Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.

from faker import Faker
fake = Faker()

#Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki. Przyjmij, że każda wizytówka zawiera dane takie jak: imię,
# nazwisko, nazwa firmy, stanowisko, adres e-mail.

class visit_card:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.adres = adres
        self.e_mail = e_mail

    #   Zmodyfikuj kod z poprzedniego ćwiczenia na temat książki adresowej tak, aby obiekt wizytówki przedstawiony jako string zawierał imię, nazwisko i adres e-mail osoby, do której należy wizytówka.

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.e_mail}'

    # Rozwiń program przechowujący wizytówki. Do klasy opisującej wizytówkę dodaj metodę contact(), która wypisze na konsoli napis “Kontaktuję się z …”,
    # a na końcu wyświetli imię, nazwisko, stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.

    def contact(self):
        print("Kontaktuje się z " + self.imie + " " + self.nazwisko +  ", " + self.stanowisko + ", " + self.e_mail)

    #W klasie przechowującej wizytówkę zdefiniuj dynamiczny atrybut (używając @property), który będzie zwracał sumę długości


    @property
    def name_size(self):
        return(len(self.imie + " " + self.nazwisko))

#Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych (dane możesz skopiować ze strony takiej jak Fake Name Generator.

klient_1 = visit_card (imie="Marysia", nazwisko="Low", nazwa_firmy="Yellow", stanowisko=("stomatolog"), adres = "Wrocek, 18 procek " , e_mail="marysia@gmail.com")
klient_2 = visit_card (imie="Władek", nazwisko="High", nazwa_firmy="Red", stanowisko=("kosmita"), adres = "Cieszyn, 15 wzgórze " , e_mail="wlasekgu@gmail.com")
klient_3 = visit_card (imie="Olek", nazwisko="nice", nazwa_firmy="Grey", stanowisko=("astronauta"), adres = "Dubrownik, Havrsko Sunsko" , e_mail="olek@gmail.com")
klient_4 = visit_card (imie="Marian", nazwisko="LOL", nazwa_firmy="Blue", stanowisko=("lekarz"), adres = "Fiesta Majorca, 6543 Island" , e_mail="marian@gmail.com")
klient_5 = visit_card (imie="Piotrek", nazwisko="wow", nazwa_firmy="Black", stanowisko=("gamer"), adres = "Cubana 15, LA California" , e_mail="piotr@gmail.com")
klient_6 = visit_card (imie=fake.name(), nazwisko=(""), nazwa_firmy=fake.company(), stanowisko=fake.job(), adres =fake.address(), e_mail=fake.email())
# Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker, którą opisaliśmy powyżej.
# Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.

lista = [klient_1, klient_2, klient_3, klient_4, klient_5, klient_6 ]

#  Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy sposoby – według imienia, nazwiska oraz adresu e-mail.


lista2 = sorted(lista, key=lambda klient1: klient1.imie)
lista3 = sorted(lista, key=lambda klient1: klient1.nazwisko)
lista4 = sorted(lista, key=lambda klient1: klient1.e_mail)


for i in lista:
    print(i.imie, i.nazwisko, i.nazwa_firmy, i.stanowisko)
    print("Imie: " + i.imie)
    print("Nazwisko: " + i.nazwisko)
    print("Nazwa Firmy: " + i.nazwa_firmy)
    print("Stanowisko: " + i.stanowisko)
    print("Adres: " + i.adres)
    print("e_mail: " + i.e_mail)

    print("---")

for i in lista2:
    print("Imie: " + i.imie)
    print("Nazwisko: " + i.nazwisko)
    print("Nazwa Firmy: " + i.nazwa_firmy)
    print("Stanowisko: " + i.stanowisko)
    print("Adres: " + i.adres)
    print("e_mail: " + i.e_mail)

    print("---")

for i in lista3:
    print("Imie: " + i.imie)
    print("Nazwisko: " + i.nazwisko)
    print("Nazwa Firmy: " + i.nazwa_firmy)
    print("Stanowisko: " + i.stanowisko)
    print("Adres: " + i.adres)
    print("e_mail: " + i.e_mail)

    print("---")


for i in lista4:
    print("Imie: " + i.imie)
    print("Nazwisko: " + i.nazwisko)
    print("Nazwa Firmy: " + i.nazwa_firmy)
    print("Stanowisko: " + i.stanowisko)
    print("Adres: " + i.adres)
    print("e_mail: " + i.e_mail)

    print("---")


#Dysponujesz już całkiem rozbudowanym programem do obsługi wizytówek. Po dodaniu kilku elementów wyślij go Mentorowi.
 #   Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać podstawowe dane
#   kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie
#   informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
  #  Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i
#  dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
   # Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
    #Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.

class BaseContact():
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.e_mail}'

    def contact(self):
        print("Wybieram numer " + self.telefon + " i dzwonię do " + self.imie + ", " + self.nazwisko)

    def __init__(self, imie, nazwisko, e_mail, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.e_mail = e_mail
        self.telefon = telefon

x = BaseContact(imie="Majkel", nazwisko="mekson", e_mail="at@o6.pl", telefon="1234")
print (x)


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, telefon2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon2 = telefon2

    def contact(self):
        print("Wybieram numer " + self.telefon2 + " i dzwonię do " + self.imie + ", " + self.nazwisko)

x = BusinessContact(imie="Majkel", nazwisko="Maejkson", e_mail="pulajla@v.pl", telefon="123456", stanowisko="ninja", nazwa_firmy="gate", telefon2="999 888 777")
print (x.contact())
