#include <iostream>
#include "lib3.hpp"
#include "lib31.hpp"

int main(){
  struct lib31::arg1 a;
  std::cout << "lib3::func1(): " << lib3::func1(a) << std::endl;
  std::cout << "lib31::func1(): " << lib31::func1(a) << std::endl;
  return 0;
}
