from task import engine, Person, Account, Bank
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(
        input(
            "1 - įveskite vartotoją\n2 - įveskite banką\n3 - įveskite sąskaitą\n4 - įveskite pajamas/išlaidas\n6 - peržiūrėti vartotojus\n7 - peržiūrėti bankus\n8 - peržiūrėti sąskaitas\n9 - išeiti iš programos"
        )
    )

    if pasirinkimas == 1:
        name = input("Įveskite vardą: ")
        surname = input("Įveskite pavardę: ")
        PID = int(input("Įveskite asmens kodą: "))
        phone_nr = int(input("Įveskite tel.Nr : "))
        asmuo = Person(name=name, surname=surname, PID=PID, phone_nr=phone_nr)
        session.add(asmuo)
        session.commit()

    if pasirinkimas == 2:
        pavadinimas = input("Įveskite banko pavadinimą: ")
        adresas = input("Įveskite adresą: ")
        banko_kodas = input("Įveskite banko kodą: ")
        swift_kodas = input("Įveskite SWIFT kodą: ")
        bankas = Bank(
            name=pavadinimas, address=adresas, bank_nr=banko_kodas, Swift=swift_kodas
        )
        session.add(bankas)
        session.commit()

    if pasirinkimas == 3:
        numeris = input("Įveskite sąskaitos numerį: ")
        balansas = 0
        vartotojai = session.query(Person).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        vartotojo_id = int(input("Pasirinkite vartotojo ID: "))
        bankai = session.query(Bank).all()
        for vienas in bankai:
            print(vienas)
        banko_id = int(input("Pasirinkite banko ID: "))
        saskaita = Account(
            account_nr=numeris,
            amount=balansas,
            person_id=vartotojo_id,
            bank_id=banko_id,
        )
        session.add(saskaita)
        session.commit()

    if pasirinkimas == 4:
        saskaitos = session.query(Account).all()
        for viena in saskaitos:
            print(viena)
        saskaitos_id = int(input("Pasirinkite sąskaitos ID: "))
        pasirinkta_saskaita = session.query(Account).get(saskaitos_id)
        irasas = float(input("Įveskite pajamas/išlaidas (su -): "))
        pasirinkta_saskaita.amount += irasas
        session.commit()

    if pasirinkimas == 6:
        persons = session.query(Person).all()

        for person in persons:
            print(person)

    if pasirinkimas == 7:
        banks = session.query(Bank).all()
        for bank in banks:
            print(bank)

    if pasirinkimas == 8:
        accounts = session.query(Account).all()
        for account in accounts:
            print(account)

    if pasirinkimas == 9:
        print("Programa baigta")
        session.close()
        break



