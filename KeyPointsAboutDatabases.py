'''
Files and databases provide persistent storage. This means they can exist after
the program has stopped running, or after a power outage, computer crash etc.

The advantage of memory variables in efficiency if not required to be saved
as you don't need a file or database call function to read them

Pros and Cons of files
Persistent storage

Requires processing a lot of files
file processing is notorious for errors
Data might need to be combined across multiple files, which can cause format issues
The huge data process requirement causes a really long queue

Databases therefore, were created to carefully handle lange data quantities
They were designed for;
-correctness - atomicity, consistency, isolation, durability (these are asset properties of databases)
-flexibility - data can be changed without changing code (ie - with files, if header changes, the code must be changed). Flexibility is provided using SQL.
-concurrent access - large numbers of simultaneous reads and writes are handled correctly
-Data semantics - realtionships between data can be easily specified and enforced

'''
