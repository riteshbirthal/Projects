from Display_Functions.text_page import *
from Read_Write_Functions.read_write import *


def edit_submit_name(person, screen, contact_id):
    new_f_name = person.first_name.strip().lower()
    new_m_name = person.middle_name.strip().lower()
    new_l_name = person.last_name.strip().lower()
    if name_valid(new_f_name, new_m_name, new_l_name)[3]:
        f_name = contact_database[contact_id].first_name
        m_name = contact_database[contact_id].middle_name
        l_name = contact_database[contact_id].last_name
        if f_name == new_f_name and m_name == new_m_name and l_name == new_l_name:
            return same_name(screen)
        else:
            contact_database[contact_id].first_name = new_f_name
            contact_database[contact_id].middle_name = new_m_name
            contact_database[contact_id].last_name = new_l_name
            first_names[f_name].remove(contact_id)
            middle_names[m_name].remove(contact_id)
            last_names[l_name].remove(contact_id)
            if new_f_name in first_names.keys():
                first_names[new_f_name].append(contact_id)
            else:
                first_names[new_f_name] = [contact_id]
            if new_m_name in middle_names.keys():
                middle_names[new_m_name].append(contact_id)
            else:
                middle_names[new_m_name] = [contact_id]
            if new_l_name in last_names.keys():
                last_names[new_l_name].append(contact_id)
            else:
                last_names[new_l_name] = [contact_id]
            write_data()
            return name_updated(screen)
    else:
        return invalid_name(screen)


def edit_submit_email(user_id, screen, id_):
    if email_valid(user_id):
        user_id = user_id.strip().lower()
        old_email = contact_database[id_].email
        contact_database[id_].email = user_id
        emails[old_email].remove(id_)
        if user_id in emails.keys():
            emails[user_id].append(id_)
        else:
            emails[user_id] = [id_]
        write_data()
        return email_updated(screen)
    else:
        return invalid_email(screen)


def edit_submit_phone(user_id, screen, contact_id):
    if phone_valid(user_id)[0] and (not phone_valid(user_id)[1]):
        user_id = user_id.strip()
        del(phone_numbers[contact_database[contact_id].phone])
        contact_database[contact_id].phone = user_id
        phone_numbers[user_id] = contact_id
        write_data()
        return phone_updated(screen)
    elif phone_valid(user_id)[1]:
        return already_exists(screen)
    else:
        return invalid_number(screen)
