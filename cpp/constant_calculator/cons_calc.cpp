#include <iostream>

int main()
{
    char op;
    double num1;
    double num2;
    double result;


    std::cout << "Enter either: (+ - * /): ";
    std::cin >> op;
    std::cout << "No. 1: ";
    std::cin >> num1;
    std::cout << "No. 2: ";
    std::cin >> num2;

    switch(op) {
        case '+':
        result = num1 + num2;
        std::cout << result;
        break;
        case '-':
        result = num1 - num2;
        std::cout << result;
        break;
        case '*':
        result = num1 * num2;
        std::cout << result;
        break;
        case '/':
        result = num1 / num2;
        std::cout << result;
        break;
        
    default:
        std::cout << "You used a wrong symbol.";
        break; 
    }
    return 0;
}