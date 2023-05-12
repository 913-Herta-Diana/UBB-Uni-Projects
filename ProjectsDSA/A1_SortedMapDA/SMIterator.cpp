#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
	this->currentPos = 0;
} //Theta(1)

void SMIterator::first(){
	this->currentPos = 0;
}//Theta(1)

void SMIterator::next(){
	if (this->currentPos==this->map.nrPairs) {
		throw exception();
	}
	else
	{
		this->currentPos++;
	}
}//Theta(1)

bool SMIterator::valid() const{
	if (this->currentPos < this->map.nrPairs)
		return true;
	return false;
}//Theta(1)

TElem SMIterator::getCurrent() const{
	if (this->currentPos == this->map.nrPairs) {
		throw exception();
	}
	return this->map.elements[this->currentPos];
	return NULL_TPAIR;
}//Theta(1)


