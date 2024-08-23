from Display_Functions.text_page import *
from Read_Write_Functions.read_write import *


def delete_contact_id(id_):
    for i in range(len(contact_database) - 1):
        if contact_database[i].id_ == id_:
            contact_database[i] = contact_database[i+1]
            delete_name(contact_database[i+1])
            delete_email(contact_database[i+1])
            contact_database[i].id_ = i
            add_person(contact_database[i])
    if len(contact_database):
        contact_database.pop()
    write_data()
    return


def delete_email(person):
    emails[person.email].remove(person.id_)
    return


def delete_name(person):
    first_names[person.first_name].remove(person.id_)
    middle_names[person.middle_name].remove(person.id_)
    last_names[person.last_name].remove(person.id_)
    return


def delete_submit_phone(phone, screen):
    if phone_valid(phone)[1]:
        id_ = phone_numbers[phone.strip()]
        person = contact_database[id_]
        delete_name(person)
        delete_email(person)
        del(phone_numbers[phone.strip()])
        delete_contact_id(id_)
        write_data()
        return contact_deleted(screen)
    else:
        return invalid_number(screen)


def delete_submit_id(user_id, screen):
    if len(user_id) and user_id.isdigit() and int(user_id) < len(contact_database):
        delete_submit_phone(contact_database[int(user_id)].phone, screen)
        write_data()
        return contact_deleted(screen)
    else:
        return invalid_id(screen)
