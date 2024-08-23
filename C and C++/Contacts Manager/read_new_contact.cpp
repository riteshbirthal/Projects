#include "read_write_files.cpp"

void read_names(struct Contact& person){
    bool name = true;
    while (name){
        cout << "First Name: ";
        getline(cin, person.First_Name);
        cout << "Middle Name: ";
        getline(cin, person.Middle_Name);
        cout << "Last Name: ";
        getline(cin, person.Last_Name);
        struct Name_ name_ = Name_Valid(person.First_Name, person.Middle_Name, person.Last_Name);
        if(name_.valid){
            person.First_Name = name_.First_Name;
            person.Middle_Name = name_.Middle_Name;
            person.Last_Name = name_.Last_Name;
            name = false;
        }else{
            cout << "Please input valid name.\n";
        }
    }
    return ;
}

void read_phone(struct Contact &person){
    bool phone = true;
    while(phone){
        cout << "Phone Number: ";
        getline(cin, person.Phone);
        struct Phone_ phone_ = Phone_Valid(person.Phone);
        if(phone_.exists){
            cout << "This phone number already exists." << endl;
        }else if(phone_.valid){
            person.Phone = phone_.Phone;
            phone = false;
        }else{
            cout << "Please input valid phone number." << endl;
        }
    }
    return ;
}

void read_email(struct Contact &person){
    bool email = true;
    while(email){
        cout << "Email: ";
        getline(cin, person.Email);
        struct Email_ email_ = Email_Valid(person.Email);
        if(email_.valid){
            person.Email = email_.Email;
            email = false;
        }else{
            cout << "Please input valid email address.\n";
        }
    }
    return ;
}

void update_database(struct Contact &person){
    // adding contact to directory
    Contact_Database.push_back(person);
    first_names[person.First_Name].push_back(ids);
    middle_names[person.Middle_Name].push_back(ids);
    last_names[person.Last_Name].push_back(ids);
    if(person.Email != "NA") emails[person.Email].push_back(ids);
    phone_number[person.Phone] = ids;
    ids += 1;
    cout << "Contact saved successfully!\n";
    write_file();
    return ;
}