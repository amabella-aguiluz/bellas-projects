#include <iostream>

int main() {

    int num;
    int guess;
    int tries;

    srand(time(NULL));
    num = rand() % 100 + 1;
    std::cout << "Number Guessing Game \n";
    do{
    std::cout << "Enter a number between 1-100. \n";
    std::cin >> guess;
    tries++;
    if(guess > num)
        {
            std::cout << "Too high! \n";
        }
    else if(guess < num)
        {
            std::cout << "Too low! \n";
        }
    else if(guess == num)
        {
            std::cout << "Correct! \n";
            std::cout << "You attempted " << tries << " times. \n";
        }
    }
    while(guess != num);


    return 0;
}