#include "vector_struct_contact_read_write.cpp"

void read_files(){
    //reading contact database
    Contact_Database_ = readVectorFromFile("data/Contact_Database_data.bin");
    for(int i = 0; i < Contact_Database_.size(); i++){
        struct Contact person;
        person.ID = stoi(Contact_Database_[i][0]);
        person.First_Name = Contact_Database_[i][1];
        person.Middle_Name = Contact_Database_[i][2];
        person.Last_Name = Contact_Database_[i][3];
        person.Email = Contact_Database_[i][4];
        person.Phone = Contact_Database_[i][5];
        Contact_Database.push_back(person);
    }
    Contact_Database_.clear();

    //reading emails
    emails = readMapFromFile1("data/emails_data.bin");

    //reading names
    first_names = readMapFromFile1("data/first_name_data.bin");
    middle_names = readMapFromFile1("data/middle_name_data.bin");
    last_names = readMapFromFile1("data/last_name_data.bin");

    //reading phone number
    phone_number = readMapFromFile0("data/phone_number.bin");
    return ;
}

void write_file(){
    //writing contact database
    Contact_Database_.clear();
    for(int i = 0; i < Contact_Database.size(); i++){
        vector<string> vec = {};
        for(int j = 0; j < 6; j++) vec.push_back(assets(Contact_Database[i], j));
        Contact_Database_.push_back(vec);
    }
    writeVectorToFile(Contact_Database_, "data/Contact_Database_data.bin");

    //writing Emails
    writeMapToFile1(emails, "data/emails_data.bin");

    //writing names
    writeMapToFile1(first_names, "data/first_name_data.bin");
    writeMapToFile1(middle_names, "data/middle_name_data.bin");
    writeMapToFile1(last_names, "data/last_name_data.bin");

    //writing phone number
    writeMapToFile0(phone_number, "data/phone_number.bin");
    return ;
}
