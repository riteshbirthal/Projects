#include <iostream>
#include<vector>
#include<cstdlib>
using namespace std;


void displayGameBoard(vector<char>& board){
    for(int i = 0; i < 3; i++){
        if(i) cout << "---" << "|" << "---" << "|" << "---" << endl;
        cout << " " << board[3*i] << " " << "|" << " " << board[3*i + 1] << " " << "|" << " " << board[3*i + 2] << " " << endl;
    }
    cout << endl << endl;
    return ;
}

void instructions(){
    cout << "Game Instructions:" << endl;
    cout << "    1. Please pick a number 1-9 corresponding to box you want to fill" << endl << endl;
    cout << "Box numbers are defined as follow:" << endl << endl;
    vector<char> vec;
    for(int i = 0; i < 9; i++)
        vec.push_back('0'+i+1);
    displayGameBoard(vec);
    cout << endl;
    return ;
}

void playerMove(vector<char>& board, char player){
    int number = -1;
    while(number<1 || number>9 || board[number-1]!=' '){
        cout << "Enter your move(1-9): ";
        cin >> number;
    }
    number--;
    board[number] = player;
    return ;
}

void computerMove(vector<char>& board, char computer){
    int number = -1;
    while(number<1 || number>9 || board[number]!=' '){
        number = rand() % 9;
        if(number<1 || number>9)
            cout << "Invalid move!" << endl;
    }
    board[number] = computer;
    return ;
}

bool checkWinner(vector<char>& board){
    for(int i = 0; i < 3; i++){
        if(board[3*i]!=' ' && board[3*i]==board[3*i + 1] && board[3*i + 1]==board[3*i + 2])
            return true;
        if(board[i]!=' ' && board[i]==board[i + 3] && board[i + 3]==board[i + 6])
            return true;
    }
    if(board[0]!=' ' && board[0]==board[4] && board[4]==board[8])
        return true;
    if(board[2]!=' ' && board[2]==board[4] && board[4]==board[6])
        return true;
    return false;
}

bool checkTie(vector<char>& board){
    for(int i = 0; i < 9; i++){
        if(board[i]==' ')
            return false;
    }
    return true;
}

int main(){
    instructions();
    cout << "Let's Play!" << endl;
    vector<char> board;
    for(int i = 0; i < 9; i++)
        board.push_back(' ');
    bool running = true;
    while(running){
        displayGameBoard(board);
        playerMove(board, 'X');
        if(checkWinner(board)){
            cout << "Congrats You Won!" << endl << endl;
            break;
        }
        computerMove(board, 'O');
        if(checkWinner(board)){
            cout << "Computer Won!" << endl << endl;
            break;
        }
    }
    return 0;
}