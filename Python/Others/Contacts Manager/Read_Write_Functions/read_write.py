from Libraries_and_Variables_Definition.checking_functions import *


def read_data():
    if not os.path.exists(path + 'contact_database'):
        write_data()
    with (open(path + 'contact_database', 'rb')) as openfile:
        for obj in pickle.load(openfile):
            converted_obj = Contact()
            converted_obj.__dict__ = obj.__dict__
            contact_database.append(converted_obj)
            add_person(converted_obj)
    # print(first_names, middle_names, last_names, emails, phone_numbers)


def write_data():
    with open(path + 'contact_database', 'wb+') as f:
        pickle.dump(contact_database, f, protocol=pickle.HIGHEST_PROTOCOL)
    f.close()
