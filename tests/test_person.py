import pytest


from beings import Person

# from person import Person

# print(sys.path)

def test_init():
    person = Person("Ethan Henderson", 24)
    assert person.name == "Ethan Henderson"
