#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
using namespace std;

SortedMap::SortedMap(Relation r) { 
	
	this->nrPairs = 0;
	this->capacity = 100;
	this->elements=new TElem[capacity];
	this->relation = r;
	

}//Theta(1)

void SortedMap::resize() {
	int newCapacity = capacity * 2;
	TElem* new_elements = new TElem[newCapacity];
	for (int i = 0; i < nrPairs; i++) {
		new_elements[i] = elements[i];
	}
	delete[] elements;
	elements = new_elements;
	capacity = newCapacity;
}

TValue SortedMap::add(TKey k, TValue v) {


	if (nrPairs == capacity) {
		resize();
	}
	int start = 0;
	int end = nrPairs - 1;
	int mid = 0;
	while (start <= end) {
		mid = start + (end - start) / 2;
		if (k == elements[mid].first) {
			TValue oldValue = elements[mid].second;
			elements[mid].second = v;
			return oldValue;
		}
		else if (relation(k,elements[mid].first)) {
			end = mid - 1;
		}
		else {
			start = mid + 1;
		}
	}
	// shift elements to the right to make room for the new element
	for (int i = nrPairs - 1; i >= start; i--) {
		elements[i + 1] = elements[i];
	}
	elements[start].first = k;
	elements[start].second = v;
	nrPairs++;
	return NULL_TVALUE;
}// BC:T(1) AC:O(logn) WC: T(logn)

TValue SortedMap::search(TKey k) const {
	
	int index = 0;
	for (index = 0; index < this->nrPairs; index++)
		if (this->elements[index].first == k) {
			TValue found = this->elements[index].second;
			return found;
		}
	return NULL_TVALUE;
}//BC: Theta(1), AC:O(nrPairs), WC: Theta(nrPairs)

TValue SortedMap::remove(TKey k) {
	
	int index = 0;
	bool found = false;
	while (index < this->nrPairs && found==false)
		if (this->elements[index].first == k)
			found = true;
		else
			index++;
	int valueDeleted = this->elements[index].second;
	if (found == true) {
		for (int i = index; i < this->nrPairs; i++)
			this->elements[i] = this->elements[i + 1];
		this->nrPairs--;
		return valueDeleted;
	}

	return NULL_TVALUE;
}//BC: Theta(1), AC:O(nrPairs), WC: Theta(nrPairs)

int SortedMap::updateValues(SortedMap& sm)
{
	//modifies the values of those Keys that are in sm to be equal to their value from sm (assume both SortedeMaps use the same relation)
	//returns the number of modified pairs
	int count_modified = 0;
	bool modified = false;
	for (int i = 0; i < this->nrPairs; i++)
		if (this->elements[i].first != this->elements[i].second) {
			modified = true;
			this->elements[i].first = this->elements[i].second;
			count_modified++;
		}
	if (!modified)
		return 0;
	for (int i = 0; i < this->nrPairs - 1; i++)
		for (int j = i+1; j < this->nrPairs; j++)
			if (!this->relation(elements[i].first, elements[j].first))
				swap(elements[i].first, elements[j].first);
	return count_modified;
}
//BC: Theta(nrPairs) WC: Theta(nrPairs^2) AC: TO(nrPairs^2);

int SortedMap::size() const {
	
	int arraySize = this->nrPairs;
	return arraySize;
}//Theta(1)

bool SortedMap::isEmpty() const {
	if (this->nrPairs == 0)
		return true;
	return false;
}//Theta(1)

SMIterator SortedMap::iterator() const {
	return SMIterator(*this); //already done
}//Theta(1)

SortedMap::~SortedMap() { //this is the destructor //Theta(1)
	
	delete[] this->elements; //array to destroy
}//Theta(1)

