#include "map_string_int_read_write.cpp"

// Function to write an unordered_map<string, vector<int>> to a binary file
void writeMapToFile1(unordered_map<std::string, vector<int>>& map, string filename) {
    // remove(filename.c_str());
    ofstream file(filename, ios::binary);
    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    // Write the number of elements in the map
    size_t numElements = map.size();
    file.write(reinterpret_cast<const char*>(&numElements), sizeof(numElements));

    // Write each key-value pair to the file
    for (const auto& entry : map) {
        const std::string& key = entry.first;
        const std::vector<int>& values = entry.second;

        // Write the length of the key string
        size_t keyLength = key.length();
        file.write(reinterpret_cast<const char*>(&keyLength), sizeof(keyLength));

        // Write the key string itself
        file.write(key.c_str(), keyLength);

        // Write the number of elements in the vector
        size_t numValues = values.size();
        file.write(reinterpret_cast<const char*>(&numValues), sizeof(numValues));

        // Write the vector elements
        file.write(reinterpret_cast<const char*>(values.data()), numValues * sizeof(int));
    }

    file.close();
}

// Function to read an unordered_map<string, vector<int>> from a binary file
unordered_map<string, vector<int>> readMapFromFile1(string filename) {
    unordered_map<string, vector<int>> map;
    ifstream file(filename, std::ios::binary);
    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return map;
    }

    // Read the number of elements in the map
    size_t numElements;
    file.read(reinterpret_cast<char*>(&numElements), sizeof(numElements));

    // Read each key-value pair from the file
    for (size_t i = 0; i < numElements; ++i) {
        // Read the length of the key string
        size_t keyLength;
        file.read(reinterpret_cast<char*>(&keyLength), sizeof(keyLength));

        // Read the key string
        std::string key(keyLength, '\0');
        file.read(&key[0], keyLength);

        // Read the number of elements in the vector
        size_t numValues;
        file.read(reinterpret_cast<char*>(&numValues), sizeof(numValues));

        // Read the vector elements
        std::vector<int> values(numValues);
        file.read(reinterpret_cast<char*>(values.data()), numValues * sizeof(int));

        // Insert the key-value pair into the map
        map[key] = values;
    }

    file.close();
    return map;
}