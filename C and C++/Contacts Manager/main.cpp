#include "delete_contact.cpp"

int main(){
    read_files();
    ids = Contact_Database.size();
    while(true){
        cout << "1: to Create New Contact." << endl;
        cout << "2: to Find a Contact." << endl;
        cout << "3: to Edit a Contact." << endl;
        cout << "4: to Delete a Contact." << endl;
        cout << "-1: to Exit." << endl;
        int mode;
        cout << "Input: ";
        cin >> mode;
        cin.ignore();
        if(mode == 1){
            cout << "Write NA, if information is not applicable.\n";
            cout << "Name should include only alphabates.\n";
            struct Contact person;
            read_names(person);
            read_email(person);
            read_phone(person);
            person.ID = ids;
            update_database(person);
        }else if(mode == 2){
            // search phone directory
            search_contact();
        }else if(mode == 3){
            edit_contact();
        }else if(mode == 4){
            delete_contact();
        }else if(mode == -1){
            write_file();
            return 0;
        }else{
            cout << "Please input valid operation number.\n";
            string str;
            getline(cin, str);
        }
    }
    return 0;
}