//this program was completed on 5/8/2022 at 7:43 pm
#include <iostream>
#include <vector>

using namespace std;

int evaluate(vector<vector<string>> Board) {
    int xNumber = 0;
    int oNumber = 0;
    
    //Checks for vertical wins
    for(int d = 0;d < Board.size();d++) {
        xNumber = 0;
        oNumber = 0;
        for(int h = 0;h < Board.size();h++) {
            if(Board[h][d] ==  "X"){ xNumber++; }
            if(Board[h][d] ==  "O"){ oNumber++; }
            
            if(xNumber == Board.size()){ return -10; }
            if(oNumber == Board.size()){ return 10; }
        }
    }
    
    //Checks for horizontial wins
    for(int h = 0;h < Board.size();h++) {
        xNumber = 0;
        oNumber = 0;
        for(int d = 0;d < Board.size();d++) {
            if(Board[h][d] == "X"){ xNumber++; }
            if(Board[h][d] == "O"){ oNumber++; }
            
            if(xNumber == Board.size()){ return -10; }
            if(oNumber == Board.size()){ return 10; }
        }
    }
    
    //Checks for diagonal wins
    xNumber = 0;
    oNumber = 0;
    for(int i = 0;i < Board.size();i++) {
        if(Board[Board.size() - i - 1][i] == "X") { xNumber++; }
        if(Board[Board.size() - i - 1][i] == "O") { oNumber++; }
        
        if(xNumber == Board.size()){ return -10; }
        if(oNumber == Board.size()){ return 10; }
    }
    xNumber = 0;
    oNumber = 0;
    for(int i = 0;i < Board.size();i++) {
        if(Board[i][i] == "X"){ xNumber++; }
        if(Board[i][i] == "O"){ oNumber++; }
        
        if(xNumber == Board.size()){ return -10; }
        if(oNumber == Board.size()){ return 10; }
    }
    return 0;
}

bool isMovesLeft(vector<vector<string>> Board){
    for(int h = 0;h < Board.size();h++){
        for(int d = 0;d < Board.size();d++){
            if(Board[h][d] == " "){return true;}
        }
    }
    return false;
}

int minimax(vector<vector<string>> Position, int depth, bool isMax){
    int best = 0;
    
    int score = 0;
    
    //if a end state had been reached the return static evaluation
    if(evaluate(Position) != 0 || isMovesLeft(Position) == false){
        return evaluate(Position);
    }
    
    //finds best move for the maximizer
    if(isMax){
        best = -1000;
        for(int h = 0;h < Position.size();h++){
            for(int d = 0;d < Position.size();d++) {
                if(Position[h][d] == " "){
                    Position[h][d] = "O";
                    
                    //recursive function
                    score = minimax(Position,depth+1,!isMax);
                    
                    Position[h][d] = " ";
                    
                    best = max(best, score);
                }
                
            }
        }
        return best;
    }
    
    //finds best move for the minimizer
    if(!isMax){
        best = 1000;
        for(int h = 0;h < Position.size();h++){
            for(int d = 0;d < Position.size();d++) {
                if(Position[h][d] == " "){
                    Position[h][d] = "X";
                    
                    //recursive function
                    score = minimax(Position,depth+1,!isMax);
                    
                    Position[h][d] = " ";
                    
                    best = min(best, score);

                }
            }
        }
        return best;
    }
    return 0;
}
int AImove(vector<vector<string>> Position){
    int bestMove = 0;
    
    int moveVal = 0;
    int bestEval = -1000;
    
    for(int h = 0; h < Position.size();h++){
        for(int d = 0; d < Position.size();d++){
            if(Position[h][d] == " "){
                Position[h][d] = "O";
                
                moveVal = minimax(Position,0,false);
                
                Position[h][d] = " ";
                
                if(moveVal > bestEval){
                    bestEval = moveVal;
                    bestMove = Position.size() * (Position.size() - h - 1) + d + 1;
                }
            }
        }
    }
    return bestMove;
}

int main()
{
    vector<vector<string>> Board
    {
        {" ", " ", " "},
        {" ", " ", " "},
        {" ", " ", " "}
    };
    int playerInput;

    
    bool hasMoved = false;
    bool AIcanMove = true;
    bool run = true;
    
    string input;
    cout << "Welcome to tic tac toe! to play you will enter a number between 1 and 9 to enter an X.\n";
    cout << "The goal is to get three X's in a row.\n";
    cout << "press any key to start.\n";
    cin >> input;
    system("clear");
    
    while(run) {
        //Prints Tic Tac Toe board to the screen
        for(int h = 0; h < Board.size();h++){
            cout << " ";
            for(int d = 0; d < Board[h].size();d++){
                cout << Board[h][d];
                if(d < Board[h].size() - 1){ cout <<"||"; }
            }
            if(h < Board.size() - 1){ cout << "\n---------\n"; }
            
        }
        cout << "\n choose a number 1-9 to place an X: ";
        cin >> playerInput;
        
        //adds player input to the board
        hasMoved = false;
        while(!hasMoved){
            for(int h = 0; h < Board.size();h++){
                for(int d = 0; d < Board[h].size();d++){
                    if(Board[h].size() * (Board[h].size() - h - 1) + d + 1 == playerInput && Board[h][d] == " ") {
                        Board[h][d] = "X";
                        hasMoved = true;
                    }
                }
            }
            if(!hasMoved){
                cout << "\n choose a number 1-9 to place an X: ";
                cin >> playerInput;
            }
        }

        //AI move
        
        if(evaluate(Board) == 0 && isMovesLeft(Board)){
            AIcanMove = true;
        }
        for(int h = 0;h < Board.size();h++){
            for(int d = 0;d < Board.size();d++){
                if(AImove(Board) == Board.size() * (Board.size() - h - 1) + d + 1 && AIcanMove){
                    Board[h][d] = "O";
                    AIcanMove = false;
                }
            }
        }
        AIcanMove = false;
        
        if(evaluate(Board) != 0 || !isMovesLeft(Board)){run = false;}
    }
    //displays who won
    system("clear");
    if(evaluate(Board) == -10){ cout << "X Won!";}
    if(evaluate(Board) == 10){ cout << "O Won!";}
    
    if(!isMovesLeft(Board)){cout << "Tie Game!";}
}
