from Display_Functions.text_page import *
from Read_Write_Functions.read_write import *


def save_contact(person, screen):
    person.id_ = len(contact_database)
    person.first_name = person.first_name.strip().lower()
    person.middle_name = person.middle_name.strip().lower()
    person.last_name = person.last_name.strip().lower()
    person.email = person.email.strip().lower()
    person.phone = person.phone.strip()
    contact_database.append(person)
    add_person(person)
    write_data()
    if contact_added(screen) is False:
        return False
