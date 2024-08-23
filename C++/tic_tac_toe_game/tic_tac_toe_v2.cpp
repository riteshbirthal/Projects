#include <iostream>
#include<vector>
#include<cstdlib>
using namespace std;


void displayGameBoard(vector<vector<char>>& board){
    for(int i = 0; i < 3; i++){
        if(i) cout << "---" << "|" << "---" << "|" << "---" << endl;
        for(int j = 0; j < 3; j++){
            cout << " " << board[i][j] << " ";
            if(j!=2)
                cout << "|";
        }
        cout << endl;
    }
    cout << endl << endl;
    return ;
}

void instructions(){
    cout << "Game Instructions:" << endl;
    cout << "    1. Please pick a number 1-9 corresponding to box you want to fill" << endl << endl;
    cout << "Box numbers are defined as follow:" << endl << endl;
    vector<vector<char>> vec(3, vector<char>(3, '0'));
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++)
            vec[i][j] += 3 * i + j + 1;
    }
    displayGameBoard(vec);
    cout << endl;
    return ;
}

int checkWinner(vector<vector<char>>& board, char computer, char player){
    int flag_1, flag_2, flag_3;
    // Columns
    flag_1 = board[0][0] != ' ' ? 1 : 0;
    flag_2 = board[0][1] != ' ' ? 1 : 0;
    flag_3 = board[0][2] != ' ' ? 1 : 0;
    for(int i = 1; i < 3; i++){
        if(flag_1 && board[i][0]!=board[i-1][0]) flag_1 = 0;
        if(flag_2 && board[i][1]!=board[i-1][1]) flag_2 = 0;
        if(flag_3 && board[i][2]!=board[i-1][2]) flag_3 = 0;
    }
    if(flag_1)
        return board[0][0] == computer ? 1 : -1;
    if(flag_2)
        return board[0][1] == computer ? 1 : -1;
    if(flag_3)
        return board[0][2] == computer ? 1 : -1;

    // Rows
    flag_1 = board[0][0] != ' ' ? 1 : 0;
    flag_2 = board[1][0] != ' ' ? 1 : 0;
    flag_3 = board[2][0] != ' ' ? 1 : 0;
    for(int i = 1; i < 3; i++){
        if(flag_1 && board[0][i]!=board[0][i-1]) flag_1 = 0;
        if(flag_2 && board[1][i]!=board[1][i-1]) flag_2 = 0;
        if(flag_3 && board[2][i]!=board[2][i-1]) flag_3 = 0;
    }
    if(flag_1)
        return board[0][0] == computer ? 1 : -1;
    if(flag_2)
        return board[1][0] == computer ? 1 : -1;
    if(flag_3)
        return board[2][0] == computer ? 1 : -1;
    
    // Diagonals
    flag_1 = board[0][0] != ' ' ? 1 : 0;
    flag_2 = board[2][2] != ' ' ? 1 : 0;
    for(int i = 1; i < 3; i++){
        if(flag_1 && board[i][i]!=board[i-1][i-1]) flag_1 = 0;
        if(flag_2 && board[2-i][i]!=board[3-i][i-1]) flag_2 = 0;
    }
    if(flag_1)
        return board[0][0] == computer ? 1 : -1;
    if(flag_2)
        return board[2][2] == computer ? 1 : -1;
    
    // Checking for tie
    flag_1 = 1;
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if(board[i][j]==' ') flag_1 = 0;
    if(flag_1)
        return 0;
    return 2;
}

void playerMove(vector<vector<char>>& board, char player){
    int number = -1;
    while(number<1 || number>9 || board[(number-1)/3][(number-1)%3]!=' '){
        cout << "Enter your move(1-9): ";
        cin >> number;
    }
    number--;
    board[number/3][number%3] = player;
    return ;
}

int ComputerAlgoritham(vector<vector<char>>& board, char computer, char player, int turn){
    int winner = checkWinner(board, computer, player);
    if(winner!=2) return winner;
    int score = INT_MIN, temp_score;
    if(!turn)
        score = INT_MAX;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i][j]==' '){
                if(turn){
                    board[i][j] = computer;
                    temp_score = ComputerAlgoritham(board, computer, player, false);
                    score = max(score, temp_score);
                    board[i][j] = ' ';
                }else{
                    board[i][j] = player;
                    temp_score = ComputerAlgoritham(board, computer, player, true);
                    score = min(score, temp_score);
                    board[i][j] = ' ';
                }
            }
        }
    }
    return score;
}

void computerMove(vector<vector<char>>& board, char computer, char player){
    int best_score = INT_MIN, x = -1, y = -1, score;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i][j]==' '){
                board[i][j] = computer;
                score = ComputerAlgoritham(board, computer, player, false);
                if(score > best_score){
                    best_score = score;
                    x = i, y = j;
                }
                board[i][j] = ' ';
            }
        }
    }
    if(x!=-1)
        board[x][y] = computer;
    return ;
}



int main(){
    instructions();
    cout << "Let's Play!" << endl;
    vector<vector<char>> board(3, vector<char>(3, ' '));
    bool running = true;
    char computer = 'X', player = 'O';
    while(running){
        displayGameBoard(board);
        playerMove(board, player);
        if(checkWinner(board, computer, player)==1){
            cout << "Congrats You Won!" << endl << endl;
            break;
        }
        if(checkWinner(board, computer, player)==0){
            cout << "Tie!" << endl << endl;
            break;
        }
        computerMove(board, computer, player);
        if(checkWinner(board, computer, player)==-1){
            cout << "Computer Won!" << endl << endl;
            break;
        }
        if(checkWinner(board, computer, player)==0){
            cout << "Tie!" << endl << endl;
            break;
        }
    }
    return 0;
}