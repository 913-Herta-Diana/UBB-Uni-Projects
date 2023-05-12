#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
using namespace std;
//Theta(1)
SortedBag::SortedBag(Relation r) {
	this->head = nullptr;
	this->tail = nullptr;
	this->relation = r;
	this->length = 0;
}

//BC: Theta(1) when we insert on the first position
//WC: Theta(length) when we insert on the last position
//AC: O(length)
void SortedBag::add(TComp e) {
	Node* current = head;
	Node* previous = nullptr;

	while (current != nullptr && relation(current->data, e)) {
		previous = current;
		current = current->next;
	}

	if (previous != nullptr && previous->data == e) {
		previous->frequency++;
		length++;
	}
	else {
		Node* newNode = new Node{ previous, current, 1, e };
		if (previous == nullptr) {
			head = newNode;
		}
		else {
			previous->next = newNode;
		}
		if (current == nullptr) {
			tail = newNode;
		}
		else {
			current->previous = newNode;
		}
		length++;
	}

	
}

//BC: Theta(1) when we remove from the first position
//WC: Theta(length) when we remove from the last position
//AC: O(length)
bool SortedBag::remove(TComp e) {
	Node* current = head;
	Node* previous = nullptr;

	while (current != nullptr && current->data != e) {
		previous = current;
		current = current->next;
	}
	if (current != nullptr) {
		if (current->frequency > 1) {
			current->frequency--;
			length--;
		}
		else {
			if (previous == nullptr) {
				head = current->next; //shift
			}
			else {
				previous->next = current->next;
			}
			if (current->next == nullptr) {
				tail = previous;
			}
			else {
				current->next->previous = previous;
			}
			delete current;
			length--;
		}
		return true;
	}

	return false;
}

//BC: Theta(1) when we find the element on the first position
//WC: Theta(length) when we find the element on the last position
//AC: O(length)
bool SortedBag::search(TComp elem) const {
	Node* current = head;

	while (current != nullptr && current->data != elem) {
		current = current->next;
	}

	return current != nullptr;
}

//BC: Theta(1) 
//WC: Theta(length) 
//AC: O(length)
int SortedBag::nrOccurrences(TComp elem) const {
	Node* current = head;

	while (current != nullptr && current->data != elem) {
		current = current->next;
	}

	if (current != nullptr) {
		return current->frequency;
	}

	return 0;
}



//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
int SortedBag::size() const {
	return length;
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
bool SortedBag::isEmpty() const {
	return length == 0;
}

//BC: Theta(1) 
//WC: Theta(1) 
//AC: O(1)
SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}

//BC: Theta(length) 
//WC: Theta(length) 
//AC: O(length)
SortedBag::~SortedBag() {
	Node* current = head;

	while (current != nullptr) {
		Node* next = current->next;
		delete current;
		current = next;
	}
}

//BC: Theta(length) 
//WC: Theta(length) 
//AC: O(length)
int SortedBag::toSet()
{
	Node* current = head;
	Node* previous = nullptr;
	int removedEl = 0;
	while (current != nullptr)
	{
		int oldFreq = current->frequency;
		if (current->frequency > 1)
		{
			current->frequency=1;
			oldFreq--;
			removedEl += oldFreq;
		}

		previous = current;
		current = current->next;
	}
	return removedEl;

	
}
