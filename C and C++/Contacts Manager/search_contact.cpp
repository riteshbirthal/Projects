#include "read_new_contact.cpp"

void print_contact(struct Contact person){
    cout << "Person ID: " << person.ID << endl;
    cout << "First Name: " << person.First_Name << endl;
    cout << "Middle Name: " << person.Middle_Name << endl;
    cout << "Last Name: " << person.Last_Name << endl;
    cout << "Email: " << person.Email << endl;
    cout << "Phone Number: " <<  person.Phone << endl;
    cout << endl;
    return ;
}

void search_by_name(){
    string asset_id;
    cout << "1: search by First Name.\n";
    cout << "2: search by Middle Name.\n";
    cout << "3: search by Last Name.\n";
    cout << "-1: to exit.\n";
    //searching by name
    int n;
    cout << "Input: ";
    cin >> n;
    cin.ignore();
    vector<int> id_;
    unordered_map<string, vector<int>> asset;
    if(n==1){
        cout << "First Name: ";
        asset = first_names;
    }else if(n==2){
        cout << "Middle Name: ";
        asset = middle_names;
    }else if(n==3){
        cout << "Last Name: ";
        asset = last_names;
    }else if(n==-1){
        return ;
    }else{
        cout << "Try again with valid input.\n";
        return ;
    }
    getline(cin, asset_id);
    if((asset.find(asset_id) == asset.end()) || (asset[asset_id].size()==0)){
        cout << "No records found.\n";
    }else if(asset_id == "NA" || asset_id == "." || asset_id == " " || asset_id == "\n"){
        cout << "Try again with valid input.\n";
    }else{
        id_ = asset[asset_id];
        cout << "Record found!" << endl << "Details: " << endl;
        for(int i = 0; i < id_.size(); i++){
            print_contact(Contact_Database[id_[i]]);
        }
    }
    return ;
}

void search_by_email(){
    string Email;
    bool run = true;
    while(run){
        cout << "Email: ";
        getline(cin, Email);
        struct Email_ email_ = Email_Valid(Email);
        if(email_.valid){
            run = false;
        }else{
            cout << "Please input valid email address.\n";
        }
    }
    if((emails.find(Email) == emails.end()) || (emails[Email].size() == 0)){
        cout << "Record not found!\n";
    }else{
        cout << "Record found!" << endl << "Details: " << endl;
        vector<int> id_ = emails[Email];
        for(int i = 0; i < id_.size(); i++){
            print_contact(Contact_Database[id_[i]]);
        }
    }
    return ;
}

void search_by_phone(){
    string phone;
    bool run = true;
    while(run){
        cout << "Phone Number: ";
        getline(cin, phone);
        struct Phone_ phone_ = Phone_Valid(phone);
        if(phone_.valid){
            run = false;
        }else{
            cout << "Please input valid phone number.\n";
        }
    }
    if(phone_number.find(phone) == phone_number.end()){
        cout << "Record not found!\n";
    }else{
        cout << "Record found!" << endl << "Details: " << endl;
        print_contact(Contact_Database[phone_number[phone]]);
    }
    return ;
}

void search_by_ID(){
    int ID;
    cout << "ID: ";
    cin >> ID;
    cin.ignore();
    if(ID >= ids){
        cout << "Record not found!\n";
    }else{
        cout << "Record found!" << endl << "Details: " << endl;
        print_contact(Contact_Database[ID]);
    }
    return ;
}

void search_contact(){
    int operation;
    cout << "1: Search by Name." << endl;
    cout << "2: Search by Email." << endl;
    cout << "3: Search by ID." << endl;
    cout << "4: Search by Phone Number." << endl;
    cout << "Input: ";
    cin >> operation;
    cin.ignore();
    if(operation == 1){
        search_by_name();
    }else if(operation == 2){
        search_by_email();
    }else if(operation == 3){
        search_by_ID();
    }else if(operation == 4){
        search_by_phone();
    }else{
        cout << "Please provide valid input." << endl;
        cin.ignore();
    }
    return ;
}