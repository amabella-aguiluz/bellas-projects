#include <iostream>
#include <ctime>

    int main(){
        srand(time(0));
        int randNum = rand() % 5 + 1;
        std::string result;
        switch(randNum) {
            case 1: {
                result = "1 million dollars";
                break;
            }
            case 2: {
                result = "skibidi toilet";
                break;
            }
            case 3: {
                result = "knife";
                break;
            }
            case 4: {
                result = "air fryer";
                break;
            }
            case 5: {
                result = "teddy bear"; 
                break;
            }   
        }
        std::cout << "You won a " << result << "!\n";
        return 0;
    }