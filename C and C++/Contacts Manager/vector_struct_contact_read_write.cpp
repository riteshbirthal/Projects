#include "map_string_vector_int_read_write.cpp"

// Serialization function for writing a string to a binary file
void serializeString(std::ofstream& outputFile, const std::string& str) {
    int size = str.size();
    outputFile.write(reinterpret_cast<const char*>(&size), sizeof(size));
    outputFile.write(str.data(), size);
}

// Deserialization function for reading a string from a binary file
void deserializeString(std::ifstream& inputFile, std::string& str) {
    int size;
    inputFile.read(reinterpret_cast<char*>(&size), sizeof(size));
    str.resize(size);
    inputFile.read(&str[0], size);
}


// Function to write a vector<struct Contact> to a binary file
void writeVectorToFile(vector<vector<string>>& vec, string filename) {
    // Write the vector of strings to a binary file
    // remove(filename.c_str());
    std::ofstream outputFile(filename, std::ios::binary);
    if (!outputFile) {
        std::cerr << "Failed to open the file for writing." << std::endl;
        return ;
    }
    
    for (const auto& row : vec) {
        int rowSize = row.size();
        outputFile.write(reinterpret_cast<const char*>(&rowSize), sizeof(rowSize));
        
        for (const std::string& str : row) {
            serializeString(outputFile, str);
        }
    }
    
    outputFile.close();
    return ;
}

// Function to read a vector<struct Contact> from a binary file
vector<vector<string>> readVectorFromFile(string filename) {
    std::ifstream inputFile(filename, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Failed to open the file for reading." << std::endl;
        return {};
    }
    
    std::vector<std::vector<std::string>> vec;
    
    while (true) {
        int rowSize;
        inputFile.read(reinterpret_cast<char*>(&rowSize), sizeof(rowSize));
        
        if (inputFile.eof())
            break;
        
        std::vector<std::string> row;
        
        for (int i = 0; i < rowSize; ++i) {
            std::string str;
            deserializeString(inputFile, str);
            row.push_back(str);
        }
        
        vec.push_back(row);
    }
    
    inputFile.close();
    return vec;
}