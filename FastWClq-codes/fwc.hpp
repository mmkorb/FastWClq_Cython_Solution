#include <iostream> //std::ostream
#include <string>
#include <vector>

class fwc {
	public:
	    //default constructor 
	    fwc();

	    //destructor
	    ~fwc();

	    std::vector<long> get_best_solution(std::string cpp_str);

};
