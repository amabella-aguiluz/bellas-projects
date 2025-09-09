#include <iostream>
#include <cmath>

int main()
{
    double a;
    double b;
    double c;

    std::cout << "Enter side A:";
    std::cin >> a;
    std:: cout << "\n";

    std::cout << "Enter side B:";
    std::cin >> b;
    std:: cout << "\n";

    c = sqrt(pow(a, 2) + pow(b, 2));
    std::cout << "Side C: " << c ;


    return 0;
}