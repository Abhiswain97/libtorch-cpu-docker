#include "test.h"

int main()
{
    auto y = torch::eye(10);

    auto x = torch::sigmoid(torch::randn({10, 10}));

    std::cout << x << std::endl;
    std::cout << y << std::endl;
}