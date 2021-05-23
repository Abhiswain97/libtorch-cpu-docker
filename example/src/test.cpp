#include "test.h"

int main(){
    auto x = torch::eye(10);

    std::cout << x << std::endl;
}