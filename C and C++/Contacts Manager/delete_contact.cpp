#include "edit_contact.cpp"

void delete_function(int contact_id){
    struct Contact person = Contact_Database[contact_id];
    Contact_Database[contact_id] = Contact_Database[Contact_Database.size()-1];
    Contact_Database[contact_id].ID = contact_id;
    phone_number[Contact_Database[contact_id].Phone] = contact_id;
    Contact_Database.pop_back();
    for(int i = 1; i < 5; i++) delete_asset(assets(person, i), contact_id, i);
    phone_number.erase(person.Phone);
    ids -= 1;
    cout << "Contact deleted successfully!\n" << endl;
    write_file();
    return ;
}

void delete_contact(){
    cout << "Please provide ID of the contact to delete.\n";
    cout << "1: if you know ID.\n";
    cout << "2: if you want to search contact for ID.\n";
    cout << "-1: to return.\n";
    cout << "Input: ";
    int user_input;
    cin >> user_input;
    cin.ignore();
    if(user_input == 1){
        int contact_id;
        cout << "ID: ";
        cin >> contact_id;
        cin.ignore();
        if(contact_id < ids){
            cout << "You want to delete Contact:" << endl;
            cout << "Please type 'YES' to delete." << endl;
            cout << "type: ";
            string sure;
            getline(cin, sure);
            if(sure == "YES") delete_function(contact_id);
        }else{
            cout << "No such ID exists." << endl;
        }
    }else if(user_input == 2){
        search_contact();
    }else if(user_input == -1){
        return ;
    }else{
        cout << "Please provide valid input.\n";
        string str;
        getline(cin, str);
    }
    return ;
}