#include <iostream>

# 374245455400126

int getDigit(const int number);
int sumOddDigits(const std::string cardNum);
int sumEvenDigits(const std::string cardNum);

int main(){
    std::string cardNum;
    int result = 0;

    std::cout << "Enter a credit card number: \n";
    std::cin >> cardNum;
    result = sumEvenDigits(cardNum) + sumOddDigits(cardNum);
    if(result % 10 == 0){
        std::cout << "Card number is valid. \n";
    }
    else{
        std::cout << "Card number is not valid. \n";
    }
}

int getDigit(const int number){
    return number % 10 + (number / 10 % 10);
}
int sumOddDigits(const std::string cardNum){
    
    int sum = 0;
    for(int i = cardNum.size() - 1; i >= 0; i-= 2){
        sum += cardNum[i] - '0';
    }

    return sum;
}
int sumEvenDigits(const std::string cardNum){
    int sum = 0;
    for(int i = cardNum.size() - 2; i >= 0; i-= 2){
        sum += getDigit((cardNum[i] - '0') * 2);
    }

    return sum;
}