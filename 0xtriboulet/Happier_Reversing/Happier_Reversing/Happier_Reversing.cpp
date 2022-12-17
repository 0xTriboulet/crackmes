#include <iostream>
#include <string>

using namespace std;

string string_xor(string x, string y) {
    string out_string;

    for (int i = 0; i < x.length(); i++) {
        out_string += static_cast<char> (x.at(i) ^ y.at(i % y.length()));
    }

    return out_string;

}

string generate_key() {
    string keys = "{U[CKi_EoV_E^ToDXUoCUS_^To[UI{'";
    string static_key = "00000000000000000000000000000ZZ";
    string out_key = string_xor(static_key, keys);
    return out_key;
}

int main()
{
    string inputString;
    string compareMe = generate_key();
    std::cout << "Welcome to 0xTriboulet's Reversing Challenge #2!\n\n";
    std::cout << "Enter the secret key:";
    std::cin >> inputString;

    if (inputString.compare(compareMe)) {
        std::cout << "Your key was incorrect! Try again later :(";
    }
    else {
        std::cout << "Your key was correct!";
    }
    return 0;
}
