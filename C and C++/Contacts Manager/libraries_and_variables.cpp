#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int ids;
unordered_map<string, int> phone_number;
vector<struct Contact> Contact_Database;
vector<vector<string>> Contact_Database_;
unordered_map<string, vector<int>> emails;
unordered_map<string, vector<int>> first_names;
unordered_map<string, vector<int>> middle_names;
unordered_map<string, vector<int>> last_names;
