#include "libraries_and_variables.cpp"

struct Contact {
    std::string First_Name, Middle_Name, Last_Name, Phone, Email;
    int ID;
};

struct Name_{
    string First_Name, Middle_Name, Last_Name;
    bool valid;
};

struct Phone_{
    string Phone;
    bool valid, exists;
};

struct Email_{
    string Email;
    bool valid;
};

struct Phone_ Phone_Valid(string Phone){
    Phone.erase(::remove_if(Phone.begin(), Phone.end(), ::isspace), Phone.end());
    struct Phone_ phone;
    phone.Phone = Phone;
    phone.exists = phone_number.find(Phone) != phone_number.end() ? true : false;
    phone.valid = (Phone.length() == 10);
    return phone;
}

struct Name_ Name_Valid(string First_Name, string Middle_Name, string Last_Name){
    First_Name.erase(::remove_if(First_Name.begin(), First_Name.end(), ::isspace), First_Name.end());
    Middle_Name.erase(::remove_if(Middle_Name.begin(), Middle_Name.end(), ::isspace), Middle_Name.end());
    Last_Name.erase(::remove_if(Last_Name.begin(), Last_Name.end(), ::isspace), Last_Name.end());
    struct Name_ name;
    name.First_Name = First_Name;
    name.Middle_Name = Middle_Name;
    name.Last_Name = Last_Name;
    name.valid = false;
    if(First_Name=="NA" && Middle_Name=="NA" && Last_Name=="NA") return name;
    name.valid = true;
    return name;
}

struct Email_ Email_Valid(string Email){
    bool at_pre = false, dot_pre = false, dot_after_at_pre = false;
    Email.erase(::remove_if(Email.begin(), Email.end(), ::isspace), Email.end());
    struct Email_ email;
    email.Email = Email;
    email.valid = false;
    if(!((Email[0] >= 'a' && Email[0] <=  'z') || (Email[0] >= 'A' && Email[0] <= 'Z'))) return email;
    if(Email[Email.length()-1] == '.') return email;
    for(int i = 0; i < Email.length(); i++){
        if(Email[i] == '@') at_pre = true;
        else if(Email[i] == '.') dot_pre = true;
        if(at_pre && Email[i] == '.') dot_after_at_pre = true;
    }
    if(at_pre && dot_pre && dot_after_at_pre){
        email.valid = true;
        return email;
    }
    return email;
}

string assets(struct Contact person, int asset_id){
    if(asset_id == 0) return to_string(person.ID);
    else if(asset_id == 1) return person.First_Name;
    else if(asset_id == 2) return person.Middle_Name;
    else if(asset_id == 3) return person.Last_Name;
    else if(asset_id == 4) return person.Email;
    else if(asset_id == 5) return person.Phone;
    else return "";
}

void correct_ids(){
    return ;
}