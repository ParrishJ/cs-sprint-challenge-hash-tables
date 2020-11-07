# Interview questions

## Hashing Functions

### Hash functions have three properties: 1) They always output the same result when the same input is passed to the function (they are deterministic). 2) The output of the Hash function should be unique - two different inputs should not result in the same numerical output. And 3) The numerical output of the hash function should fall within a certain range

## Collision resolution

### Collisions on hash tables can be resolved in different ways. One such way, linear probing, involves searching for the next available open “slot” on the hash table when the hash function returns a value that is already in use. Another method, chaining, involves replacing the contents of a hash table “slot” with a linked list so that multiple entries can be made in the same “slot” on the hash table.

## Performance of basic hash table operations

### The performance of retrieving information from a hash table is typically O(1), or constant time, although the time complexity can increase to O(n), or linear time, in cases where the load factor is especially high and there has been a high number of collisions on the table.

## Load factor

### The load factor of the table tells the developer / program how full the hash table is. It can be calculated by dividing the number of entries in the hash table by the total number of “slots” or available spaces on the hash table. As more entries are made to the Hash table, the load factor increases.

## Automatic Resizing

### To increase performance and save space, a hash table can be programmed to automatically resize. To do this, the hash table can take the load factor into account and increase in size when the table is too full (the load factor is too high) or decrease in size when the table is too empty (the load factor is too low).

## Various use cases for hash tables

### Hash tables are used in many different areas of computer science. They are especially useful for storing items that are looked up consistently. They are also used in caching (server and client caching) and in encrypting data.
