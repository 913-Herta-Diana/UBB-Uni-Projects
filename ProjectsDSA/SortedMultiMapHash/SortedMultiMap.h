#pragma once
//DO NOT INCLUDE SMMITERATOR

//DO NOT CHANGE THIS PART
#include <vector>
#include <utility>
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111)
#define DELETED_TELEM pair<TKey, TValue>(-999999, -999999)
#define K1 0.5
#define K2 0.5
using namespace std;
class SMMIterator;
typedef bool(*Relation)(TKey, TKey);


class SortedMultiMap {
	friend class SMMIterator;
private:
	
	int m;
	TElem* hashtable;
	int _size;                    // Number of elements in the hashtable
	Relation relation;           // Function defining the order of keys

	void resize();
	void addWithHash(TElem* hashtable,TElem element);
	int hash(TKey key);
	int quadraticProbing(int i,TKey k);

public:

	// constructor
	SortedMultiMap(Relation r);

	void printHash();

	//adds a new key value pair to the sorted multi map
	void add(TKey c, TValue v);

	//returns the values belonging to a given key
	vector<TValue> search(TKey c) ;

	//removes a key value pair from the sorted multimap
	//returns true if the pair was removed (it was part of the multimap), false if nothing is removed
	bool remove(TKey c, TValue v);

	//returns the number of key-value pairs from the sorted multimap
	int size() const;

	//verifies if the sorted multi map is empty
	bool isEmpty() const;

	// returns an iterator for the sorted multimap. The iterator will returns the pairs as required by the relation (given to the constructor)	
	SMMIterator iterator() const;

	//return the difference between the maximum and the minimum value (assume integer values)
	// //if the sorted map is empty the range is -1
	int getValueRange() const;

	// destructor
	~SortedMultiMap();
};
