#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <errno.h>

int main (int argc, char** argv)
{
    if (argc != 2)
    {
        std::cerr << "Wrong num of args. Must be 1, but "
            << argc-1 << std::endl;
        return EXIT_FAILURE;
    }
    char** endptr = new char*;
    const unsigned long acc = strtoul(argv[1], endptr, 10);
    if (*argv[1] != '\0' && **endptr == '\0')
    {
        std::cout << "acc=" << acc << std::endl;
        double pi = 0;
        double mig = -1;
        for (unsigned long i = 0; i < acc; ++i)
        {
            std::cout << pi << std::endl;
            pi += 4 * mig / (2*i+1);  
            mig = -mig;
        }
    }
    else
    {
        perror("strtoul");
        return EXIT_FAILURE;
    }
    return 0;
}
