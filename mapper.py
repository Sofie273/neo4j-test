"""
This shows how neo4j data can be delivered to the server as dict


TO RUN
install:
    pip install neomodel
run local:
    neo4j local database:
        user: neo4j
        password: 123456
        address: localhost:7687
"""

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'


"""Not used yet"""


class Country(StructuredNode):
    name = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')


def add_person(name, age):
    person = Person(name=name, age=age).save()
    person.save()
    print("Created Person with name ", person.name)

def add_country(name):
    country = Country(name=name).save()
    country.save()
    print("Created Country with name ", country.name)

def connect_nodes(person, country):
    person.country.connect(country)
    print(person.name, " is from ", country.name)

def output(person, country):
    print(person, " is from ", country)

def return_age(name):
    person = Person.nodes.get(name=name)
    return person.age

def change_age(name, age):
    person = Person.nodes.get(name=name)
    person.age = age
    person.save()   

""" if __name__ == '__main__':
    a = 1
    while (a):
        try:
            person = Person.nodes.get(name="Sofie")
            country = Country.nodes.get(name="Germany")

            person.country.connect(country)
            a = 0
        except:
            add_person("Sofie", 21)
            add_country("Germany")
        

    output(person, country) """