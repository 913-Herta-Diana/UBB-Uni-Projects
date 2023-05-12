#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	currentNode = b.head;
	currentFrequency = 1;
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
TComp SortedBagIterator::getCurrent() {
	if (this->currentNode == nullptr) {
		throw exception();
	}
	return this->currentNode->data;
	
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
bool SortedBagIterator::valid() {
	if (this->currentNode == nullptr) {
		return false;
	}
	return true;
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
void SortedBagIterator::next() {
	if (this->currentNode == nullptr) {
		throw exception();
	}
	else {
		if (this->currentFrequency < this->currentNode->frequency) {
			this->currentFrequency++;
		}
		else {
			this->currentNode = this->currentNode->next;
			this->currentFrequency = 1;
		}
	}
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
void SortedBagIterator::first() {
	this->currentNode = this->bag.head;
}

