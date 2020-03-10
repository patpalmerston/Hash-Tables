# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return 'repr()'

    def __str__(self):
        return f'key: {self.key}, value: {self.value}'


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        # create a hashed index
        hashed_index = self._hash_mod(key)
        # create a new node
        new_node = LinkedPair(key, value)
        # attach a node.next to its key
        new_node.next = self.storage[hashed_index]
        # attach the key to its node
        self.storage[hashed_index] = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # The goal is to find the previous node and make the prev.next equal to the curr.next to change the pointers for removal.

        # if key is not in storage return an error
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            return f"This key: {key} does not exist!"
        # if key is in storage get the current value of key and remove it
        # curr is our node to be deleted
        curr = self.storage[hashed_key]
        # set variable previous to none
        prev = None
        # loop while the key of our current node is equal to the key given as an argument
        while curr.key == key:
            # check if prev has a value
            if prev is not None:
                # if prev has a value then we need to iterate that value to the current nodes next
                prev.next = curr.next
            # if prev has no value
            else:
                # Then our initial key and value is equal to curr's next, which happens when we delete the first node.
                self.storage[hashed_key] = curr.next
            return True
        # give previous a value
        prev = curr
        # iterate curr forward so we can loop through the whole list
        curr = curr.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash the key to find it in the table
        current_key = self._hash_mod(key)
        # grab the index with that key in table
        current_value = self.storage[current_key]
        # loop while it is true there is a current_value from that key
        while current_value:
            # see if the current values current key matches the key given
            if current_value.key == key:
                # return that node
                return current_value.value
        # iterate through the tables keys to try and find key
            current_value = current_value.next
        # return none if nothing found
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double cpacity
        self.capacity = self.capacity * 2
        # new Hashtable
        new_storage = HashTable(self.capacity)
        count = 0
        # search for all nodes in storage
        for node in self.storage:
            # while there are nodes
            while node:
                count += 1
                print('node', node, count)
                # insert node key and value into new storage
                new_storage.insert(node.key, node.value)
                # continue moving through all the nodes
                node = node.next
        # current storage equals the new HT
        self.storage = new_storage

        # old_storage = self.storage
        # self.capacity = self.capacity * 2
        # self.storage = [None] * self.capacity

        # for bucket_item in old_storage:
        #     self.insert(old_storage[bucket_item], bucket_item.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
