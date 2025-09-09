#include <iostream>
#include <iomanip>


int main()
{
    std::string questions[] = {
        "What is 2 + 2?: ",
        "What is the meaning of life?: ",
        "Who is my husband?: "};

    std::string options[][4] = {
        {"A. 4", "B. 5", "C. 6", "D. 3"},
        {"A. 69", "B. 42", "C. 420", "D. 666"},
        {"A. Tsukihiko Amano", "B. Your mom", "C. Reigen Arataka", "D. Kim Dokja"}
    };

    char answerkey[] = {'A', 'B', 'A'};

    int size = sizeof(questions)/sizeof(questions[0]);
    char guess;
    int score;
    
    for(int i = 0; i < size; i++){
        std::cout << questions[i] << "\n";
        for(int j = 0; j < sizeof(options[i])/sizeof(options[i][0]); j++){
            std::cout << options[i][j] << "\n";
        }
        std::cout << "\n";

        std::cin >> guess;
        guess = toupper(guess);
        if(guess == answerkey[i]){
            std::cout << "Correct! \n";
            score++;
        } 
        else{
            std::cout << "Wrong, sorry. \n";
            std::cout << "Answer: " << answerkey[i] << "\n";
        }
    }

    std::cout << "Correct Guesses: " << score << "\n"; 
    std::cout << "Score: " <<  std::setprecision(0) << std::fixed << (score/(double)size)*100 << "%\n";
    return 0;
}