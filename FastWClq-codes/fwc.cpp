#include "fwc.hpp"
#include "fastwclq.cpp"
//#include <utility> //std::move

//-----------------------------------------------------------------
//default constructor 
fwc::fwc() {
}

//-----------------------------------------------------------------
//destructor
fwc::~fwc() {
}

std::vector<long> fwc::get_best_solution(std::string cpp_str){
	return testando(cpp_str);
}
