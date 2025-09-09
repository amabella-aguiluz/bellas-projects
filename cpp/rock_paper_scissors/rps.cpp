#include <iostream>
#include <ctime>

char userChoice();
char computerChoice();
void showChoice(char choice);
void chooseWinner(char player, char computer);

int main(){
    char player;
    char computer;

    player = userChoice();
    std::cout << "You chose: ";
    showChoice(player);
    computer = computerChoice();
    std::cout << "Computer chose: ";
    showChoice(computer);
    chooseWinner(player, computer);
    return 0;
}

char userChoice(){
    char player;
    std::cout << "Rock, paper, or scissors?\n";
    do
    {std::cout << "'r' for rock\n'p' for paper\n's' for scissors\n";
    std::cin >> player;
    }
    while(player != 'r' && player != 'p' && player != 's');
    return player;
}

char computerChoice(){
    char computer;
    srand(time(NULL));
    int num = rand() % 3 + 1;

    switch(num){
        case 1:
        return 'r';
        break;
    case 2:
        return 'p';
    case 3:
        return 's';
    }
}

void showChoice(char choice){
    switch(choice){
        case 'r':
        std::cout << "Rock\n";
        break;
        case 'p':
        std::cout << "Paper\n";
        break;
        case 's':
        std::cout << "Scissors\n";
        break;
    }
}

void chooseWinner(char player, char computer){
    switch(player){
        case 'r':
        if(computer == 'r')
        {std::cout << "It's a tie!\n";}
        else if(computer == 'p')
        {std::cout << "You lose!\n";}
        else
        {std::cout << "You win!\n";}        
        break;


        case 'p':
        if(computer == 'p')
        {std::cout << "It's a tie!\n";}
        else if(computer == 'r')
        {std::cout << "You lose!\n";}
        else
        {std::cout << "You win!\n";}
        break;


        case 's':
        if(computer == 's')
        {std::cout << "It's a tie!\n";}
        else if(computer == 'r')
        {std::cout << "You lose!\n";}
        else
        {std::cout << "You win!\n";}
        break;
    }
}


/*srand(time(NULL));

int result = rand() % 3 + 1;
std::cout << "Rock, paper, or scissors?\n";
std::cin >> choice;
std::cout << result;

if(result == choice){
    std::cout << "Congratulations!\n";
}
else{
    std::cout << "Better luck next time.\n";
}
randomize result ( % 3)
    rock
    paper
    scissors

    case correct
    congrats!

    case false
    try again*/