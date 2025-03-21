"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
    Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present.
    Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements
    (it's guaranteed that at least one element exists when this method is called).
    Each element must have the same probability of being returned.


Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-2^31 <= val <= 2^31 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        # This map is used to get the index in array in O(1) time.
        self.dictionary = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dictionary:
            return False

        # Put the element at the end of the list
        l = len(self.array)
        self.array.append(val)
        self.dictionary[val] = l
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        index = self.dictionary.get(val, None)
        if index is None:
            return False

        del self.dictionary[val]

        # Swap element with last element so that removal from the list can be done in O(1) time.
        length = len(self.array)
        last = self.array[length - 1]
        self.array[index], self.array[length - 1] = self.array[length - 1], self.array[index]
        del self.array[-1]
        if last in self.dictionary:
            self.dictionary[last] = index
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randrange(0, len(self.array))
        return self.array[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())

