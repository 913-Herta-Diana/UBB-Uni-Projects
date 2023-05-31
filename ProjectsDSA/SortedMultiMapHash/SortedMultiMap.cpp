#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
	this->m = 16;
	this->hashtable = new TElem[this->m];
	this->_size = 0;
	this->relation = r;
	for (int i = 0; i < m; i++)
		hashtable[i] = NULL_TELEM;
}

void SortedMultiMap::resize()
{
	//load factor: size/capacity > 0.7 
	int oldM = this->m;
	this->m *= 2;
	TElem el = NULL_TELEM;
	TElem* newHashtable = new TElem[m];
	for (int i = 0; i < m; i++)
		newHashtable[i] = NULL_TELEM;
	for (int i = 0; i < oldM; i++)
		if (hashtable[i] != NULL_TELEM)
			addWithHash(newHashtable, hashtable[i]); //check for loop
	this->hashtable = newHashtable;
}
void SortedMultiMap::addWithHash(TElem* hashtable, TElem element)
{
	int i = 0;
	int pos = quadraticProbing(i, element.first);
	while (i < m && hashtable[pos] != NULL_TELEM)
	{
		i++;
		//cout << "position: " << i << "\n";
		pos = quadraticProbing(i, element.first);

	}
	//if (i == m)
	//	resize();
	/*else*/
		hashtable[pos] = element;
		_size++;
}
int SortedMultiMap::hash(TKey key) {
	return key % m;
}

int SortedMultiMap::quadraticProbing(int i, TKey k) {

	return (int)(hash(abs(k)) + K1 * i + K2 * i * i) % m;
}
void SortedMultiMap::printHash()
{
	for (int i = 0; i < m; i++)
		cout << i<<"."<<hashtable[i].first << "," << hashtable[i].second << "\n";
}

void SortedMultiMap::add(TKey c, TValue v) {
	if (_size >= m)
		resize();
	addWithHash(hashtable, make_pair(c, v));

}

vector<TValue> SortedMultiMap::search(TKey c)  {
	
	vector<TValue> values;

	int i = 0;
	int pos = quadraticProbing(i,c);
	while (i < m && hashtable[pos] != NULL_TELEM) {
		if (hashtable[pos].first == c) {
			values.push_back(hashtable[pos].second);
		}
		i++;
		pos = quadraticProbing(i, c);
	}

	return values;
}

bool SortedMultiMap::remove(TKey c, TValue v) {
	int i = 0;
	int pos = quadraticProbing(i, c);
	while (i < m ) {
		if (hashtable[pos].first == c && hashtable[pos].second == v) {
			hashtable[pos] = DELETED_TELEM;
			_size--;
			return true;
		}
		i++;
		pos = quadraticProbing(i, c);
	}

	return false;
}


int SortedMultiMap::size() const {
	return _size;
}

bool SortedMultiMap::isEmpty() const {
	return _size == 0;
}

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}

SortedMultiMap::~SortedMultiMap() {
	delete[] hashtable;
}
