#include "ListIterator.h"
#include "IteratedList.h"
#include <exception>

ListIterator::ListIterator(const IteratedList& list) : list(list) {
	index = list.head;
}
//BC: theta(1), WC: theta(1), AC: O(1)

void ListIterator::first() {
	this->index = this->list.head;
}
//BC: theta(1), WC: theta(1), AC: O(1)

void ListIterator::next() {
	if (this->index == -1) {
		throw std::exception();
	}
	this->index = this->list.next[index];
}
//BC: theta(1), WC: theta(1), AC: O(1)

bool ListIterator::valid() const {
	return index != -1;
}
//BC: theta(1), WC: theta(1), AC: O(1)

TElem ListIterator::getCurrent() const {
	if (this->index == -1) {
		throw std::exception();
	}

	return this->list.elems[this->index];
}
//BC: theta(1), WC: theta(1), AC: O(1)



