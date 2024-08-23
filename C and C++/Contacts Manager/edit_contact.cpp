#include "search_contact.cpp"

void delete_asset(string asset, int contact_id, int asset_id){
    int size;
    vector<int> asset_data;
    if(asset_id == 1) asset_data = first_names[asset];
    else if(asset_id == 2) asset_data = middle_names[asset];
    else if(asset_id == 3) asset_data = last_names[asset];
    else if(asset_id == 4) asset_data = emails[asset];
    else return ;
    for(int i = 0; i < asset_data.size()-1; i++){
        if(asset_data[i] == contact_id){
            asset_data[i] = asset_data[i+1];
            asset_data[i+1] = contact_id;
        }
    }
    asset_data.pop_back();
    if(asset_id == 1) first_names[asset] = asset_data;
    else if(asset_id == 2) middle_names[asset] = asset_data;
    else if(asset_id == 3) last_names[asset] = asset_data;
    else if(asset_id == 4) emails[asset] = asset_data;
    else return ;
    return ;
}

bool check_old_new_names(struct Name_ a, struct Name_ b){
    if(a.First_Name != b.First_Name) return false;
    if(a.Middle_Name != b.Middle_Name) return false;
    if(a.Last_Name != b.Last_Name) return false;
    return true;
}

void edit_name(int contact_id){
    struct Contact person = Contact_Database[contact_id];
    struct Name_ old_name = Name_Valid(person.First_Name, person.Middle_Name, person.Last_Name);
    bool name = true;
    string f_name, m_name, l_name;
    while (name){
        cout << "New First Name: ";
        getline(cin, f_name);
        cout << "New Middle Name: ";
        getline(cin, m_name);
        cout << "New Last Name: ";
        getline(cin, l_name);
        struct Name_ new_name_ = Name_Valid(f_name, m_name, l_name);
        if(check_old_new_names(new_name_, old_name)){
            cout << "This is the old Name. Please provide new Name." << endl;
        }else if(new_name_.valid){
            Contact_Database[contact_id].First_Name = new_name_.First_Name;
            Contact_Database[contact_id].Middle_Name = new_name_.Middle_Name;
            Contact_Database[contact_id].Last_Name = new_name_.Last_Name;
            first_names[f_name].push_back(contact_id);
            middle_names[m_name].push_back(contact_id);
            last_names[l_name].push_back(contact_id);
            name = false;
        }else{
            cout << "Please input valid name.\n";
        }
    }
    for(int i = 1; i < 4; i++) delete_asset(assets(person, i), contact_id, i);
    cout << "Name updated successfully!" << endl;
    return ;
}

void edit_email(int contact_id){
    string old_email = Contact_Database[contact_id].Email;
    bool email = true;
    string new_email;
    while(email){
        cout << "New Email: ";
        getline(cin, new_email);
        struct Email_ new_email_ = Email_Valid(new_email);
        if(new_email_.Email == old_email){
            cout << "This is old email address. Please provide new Email Address." << endl;
        }else if(new_email_.valid){
            Contact_Database[contact_id].Email = new_email_.Email;
            emails[new_email_.Email].push_back(contact_id);
            email = false;
        }else{
            cout << "Please input valid email address.\n";
        }
    }
    delete_asset(old_email, contact_id, 4);
    cout << "Email updated successfully!" << endl;
    return ;
}

void edit_contact(){
    cout << "Please provide ID to edit a contact." << endl;
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
            cout << "1: to edit Name." << endl;
            cout << "2: to edit Email." << endl;
            cout << "Input: ";
            int edit_input;
            cin >> edit_input;
            cin.ignore();
            if(edit_input == 1) edit_name(contact_id);
            else if(edit_input == 2) edit_email(contact_id);
            else cout << "Please provide valid input." << endl;
            write_file();
        }else cout << "No such ID exists." << endl;
    }else if(user_input == 2) search_contact();
    else if(user_input == -1) return ;
    else{
        cout << "Please provide valid input.\n";
        string str;
        getline(cin, str);
    }
    return ;
}