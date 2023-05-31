#include <iostream>

#include "ShortTest.h"
#include "ExtendedTest.h"
#include <exception>
int main(){
    testAll();
	testAllExtended();
    std::cout<<"Finished SMM Tests!"<<std::endl;
	system("pause");
}
