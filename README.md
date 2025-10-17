# voters_data_storage
This project implements a voter management system using a hash table with chaining to organize voter records by house number. It is designed to store, search, display, and delete voter details efficiently, simulating a realistic village-house-member structure.
Each voter record contains:

Voter ID

Name

Age

Address

House Number

Total Members in the House

The hash table uses the house number modulo table size as the hash key, allowing multiple members in the same house to be stored under the same hash slot (using linear chaining).
The user specifies the number of houses in their area.

Each house can have multiple voters; their details are entered individually.

Records are stored in a hash table, using house_no % size as the slot.

Display groups all members in the same house together for easy visualization.
