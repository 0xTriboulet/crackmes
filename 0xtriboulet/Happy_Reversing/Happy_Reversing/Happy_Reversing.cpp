#include <iostream>
#include <string>

using namespace std;

string generate_key() {
    string keys = "Keks{You_found_the_key!}";
    return keys;
}

int main()
{
    string inputString;
    std::cout << "Welcome to 0xTriboulet's Reversing Challenge #1!\n\n";
    std::cout << "Enter the secret key:";
    std::cin >> inputString;
    if (inputString.compare(generate_key())) {
        std::cout << "Your key was incorrect! Try again later :(";
    }
    else {
        std::cout << "Your key was correct!";
    }
    

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

