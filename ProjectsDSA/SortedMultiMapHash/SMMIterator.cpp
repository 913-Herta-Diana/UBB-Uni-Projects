#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	this->array = new TElem[this->map.m];
	this->currentPos = 0;

	for (int i = 0; i < this->map.m; i++)
			this->array[i] = this->map.hashtable[i];

	for (int i = 0; i < this->map.m - 1; i++)
		for (int j = 0; j < this->map.m; j++)
			if (map.relation(array[i].first, array[j].first) == false)
				swap(array[i], array[j]);
	
}

void SMMIterator::first(){
	this->currentPos = 0;
	//while (this->currentPos < this->map.m && (this->map.hashtable[currentPos] != NULL_TELEM || this->map.hashtable[currentPos]!=DELETED_TELEM))
	//this->currentPos++;
	
}

void SMMIterator::next(){

	//if (!valid())
	//	throw exception("Element is not valid!");
	if(valid() && currentPos<this->map.m-1)
		this->currentPos++;
	
	//while (this->currentPos < this->map.m && (this->map.hashtable[this->currentPos]!=NULL_TELEM || this->map.hashtable[this->currentPos] != DELETED_TELEM))
	//	this->currentPos++;

}

bool SMMIterator::valid() const {

	return this->currentPos < this->map.m && this->array[this->currentPos] != NULL_TELEM && this->array[this->currentPos] != DELETED_TELEM;
}


TElem SMMIterator::getCurrent() const{
	if(!valid())
		return NULL_TELEM;
	return this->array[this->currentPos];
}


