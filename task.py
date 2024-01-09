# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti sąskaitas bankuose.

# Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
# Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
# Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
# Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose
# Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
# Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis, bankus, sąskaitas.
# Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų.
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///banks.db")
Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("bank_id", Integer, ForeignKey("bank.id")),
    Column("person_id", Integer, ForeignKey("person.id")),
)


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    PID = Column(Integer)
    phone_nr = Column(Integer)
    banks = relationship("Bank", secondary=association_table, back_populates="persons")
    accounts = relationship("Account", back_populates="person")

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.surname}"


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    account_nr = Column(Integer)
    amount = Column(Float)
    person_id = Column(Integer, ForeignKey("person.id"))
    bank_id = Column(Integer, ForeignKey("bank.id"))
    person = relationship("Person", back_populates="accounts")
    bank = relationship("Bank", back_populates="accounts")

    def __repr__(self):
        return f"{self.person}, {self.bank.name}, {self.account_nr}, {self.amount:10.2f}"


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    address = Column(String)
    name = Column(String)
    bank_nr = Column(Integer)
    Swift = Column(Integer)
    persons = relationship(
        "Person", secondary=association_table, back_populates="banks"
    )

    accounts = relationship("Account", back_populates="bank")

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.bank_nr}"


Base.metadata.create_all(engine)
