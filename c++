#include <iostream>

using namespace std;

int AIMove(int PlayerMove);
int HasWon(string GameBoard[3][3], int boardLength);
int main () {
    const int Length = 3;
    string Board[Length][Length] = {
        {" ", " ", " "},
        {" ", " ", " "},
        {" ", " ", " "},
    };
    int NodeMap[Length][Length] = {
        {0,0,0},
        {0,0,0},
        {0,0,0},
    };
    int NodeNumber = 1;
    for(int h = Length - 1; h >= 0;h--) {
        for(int d = 0; d < Length;d++) {
            NodeMap[h][d] = NodeNumber;
            NodeNumber++;
        }
    }
    
    int Player;
    bool HasMoved = false;
    bool run = true;
    while(run) {
        //Prints Tic Tac Toe board to the screen
        for(int h = 0; h < Length;h++) {
            cout << " ";
            for(int d = 0; d < Length;d++) {
                cout << Board[h][d];
                if(d < Length - 1) { cout <<"||"; }
            }
            if(h < Length - 1) { cout << "\n---------\n"; }
            
        }
        //Gets player input
        cout << "\n choose a number 1-9 to place an X: ";
        cin >> Player;
        
        //Adds it to the board
        HasMoved = false;
        while(!HasMoved) {
            for(int h = 0; h < Length; h++) {
                for(int d = 0; d < Length; d++) {
                    if(NodeMap[h][d] == Player && Board[h][d] == " ") { 
                        Board[h][d] = "X"; 
                        HasMoved = true;
                    }
                }
            }
            if(!HasMoved) {
                cout << "\n choose a number 1-9 to place an X: ";
                cin >> Player;
            }
        }
        cout << HasWon(Board, Length) << "\n";
        if(Player == 0) {
            run = false;
        }
    }
    for(int i = 0;i < Length;i++) {
        cout << NodeMap[i][i] << " ";
    }
    cout << "\n";
    for(int i = Length - 1;i >= 0;i--) {
        cout << NodeMap[i][i] << " ";
    }
}

int AIMove(int PlayerMove, int boardLength);

//Checks if anyone has won yet. 0: nothing has happend, 1: tie, 2: X win, 3: O win.
int HasWon(string GameBoard[3][3], int boardLength) {
    int xNumber = 0;
    int oNumber = 0;
    
    //Checks for vertical wins
    for(int d = 0;d < boardLength;d++) {
        xNumber = 0;
        oNumber = 0;
        for(int h = 0;h < boardLength;h++) {
            if(GameBoard[h][d] ==  "X") { xNumber++; }
            if(GameBoard[h][d] ==  "O") { oNumber++; }
            
            if(xNumber == boardLength ) { return 2; }
            if(oNumber == boardLength ) { return 3; }
        }
    }
    
    //Checks for horizontial wins
    for(int h = 0;h < boardLength;h++) {
        xNumber = 0;
        oNumber = 0;
        for(int d = 0;d < boardLength;d++) {
            if(GameBoard[h][d] ==  "X") { xNumber++; }
            if(GameBoard[h][d] ==  "O") { oNumber++; }
            
            if(xNumber == boardLength ) { return 2; }
            if(oNumber == boardLength ) { return 3; }
        }
    }
    
    //Checks for diagonal wins
    xNumber = 0;
    oNumber = 0;
    for(int i = boardLength - 1;i >= 0;i--) {
        if(GameBoard[i][i] == "X") { xNumber++; }
        if(GameBoard[i][i] == "O") { oNumber++; }
        
        if(xNumber == boardLength ) { return 2; }
        if(oNumber == boardLength ) { return 3; }
    }
    
    xNumber = 0;
    oNumber = 0;
    for(int i = 0;i < boardLength;i++) {
        if(GameBoard[i][i] == "X") { xNumber++; }
        if(GameBoard[i][i] == "O") { oNumber++; }
        
        if(xNumber == boardLength ) { return 2; }
        if(oNumber == boardLength ) { return 3; }
    }
    
    //Checks for a tie
    xNumber = 0;
    oNumber = 0;
    for(int h = 0;h < boardLength;h++) {
        for(int d = 0;d < boardLength;d++) {
            if(GameBoard[h][d] ==  "X") { xNumber++; }
            if(GameBoard[h][d] ==  "O") { oNumber++; }
            
            if(xNumber+oNumber == boardLength*boardLength) { return 1; }
        }
    }
    return 0;
}