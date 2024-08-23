#include "struct_definition.cpp"

// Function to write an unordered_map<string, int> to a binary file
void writeMapToFile0(unordered_map<string, int>& map, string filename) {
    // remove(filename.c_str());
    ofstream file(filename, ios::binary);
    if (!file) {
        cerr << "Error opening file: " << filename << endl;
        return;
    }

    // Write the size of the map
    size_t size = map.size();
    file.write(reinterpret_cast<const char*>(&size), sizeof(size));

    // Write each key-value pair in the map
    for (const auto& pair : map) {
        // Write the length of the key string
        size_t keyLength = pair.first.length();
        file.write(reinterpret_cast<const char*>(&keyLength), sizeof(keyLength));

        // Write the key string
        file.write(pair.first.c_str(), keyLength);

        // Write the value
        file.write(reinterpret_cast<const char*>(&pair.second), sizeof(pair.second));
    }

    file.close();
}

// Function to read an unordered_map<string, int> from a binary file
unordered_map<string, int> readMapFromFile0(string filename) {
    unordered_map<string, int> map;
    ifstream file(filename, ios::binary);
    if (!file) {
        // writeMapToFile0(emails, filename);
        cerr << "Error opening file: " << filename << endl;
        return map;
    }

    // Read the size of the map
    size_t size;
    file.read(reinterpret_cast<char*>(&size), sizeof(size));

    // Read each key-value pair in the map
    for (size_t i = 0; i < size; ++i) {
        // Read the length of the key string
        size_t keyLength;
        file.read(reinterpret_cast<char*>(&keyLength), sizeof(keyLength));

        // Read the key string
        string key(keyLength, '\0');
        file.read(&key[0], keyLength);

        // Read the value
        int value;
        file.read(reinterpret_cast<char*>(&value), sizeof(value));

        // Insert the key-value pair into the map
        map[key] = value;
    }

    file.close();
    return map;
}
