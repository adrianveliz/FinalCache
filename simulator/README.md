# Cache Tests Javaport

Simulation of Least Recently Accessed (LRA), LRA Weak Evict (LRAwe), and FinalCache. FinalCache cannot be used as a drop-in replacement for existing caches 
because of the strong coupling between FinalCache and its entries resulting from the use of finalize. 

Much of this code was written by Aleksandr Diamond and this is the link to his [GitHub implemenation](https://github.com/asdiamond/cache.tests/tree/javaport). 
The simulation is written in Java and was originally an IntelliJ project. However, during the course of publication it was very difficult to setup the build
environment on another system so the code has been refactored to run from the terminal. Also note, the graphs require matplotlib and numpy to generate.

Each caching algorithm has its own java class and tester. LRUCache and TestUtils serve as the basis for each caching algorithm and tester respectively.
Be sure to update the directory where the log data is stored on line 15 of TestUtils to your generated Firefox logs. Do **NOT** have any other files in said directory
aside from log file.

The following is a description of each test and their output:
* LRUTest is for LRA and prints hits, misses, in-use missess, and in-use evictions
* NenovCacheTest is for LRAwe. LRAwe cannot have in-use misses or in-use evictions. We called it Nenov after the strategy of using Soft references for 
evicted entries from Nenov and Dobrikov. [Memory Sensitive Caching in Java](https://pdfs.semanticscholar.org/f1d7/3b7933abcca9842a74c15a48c084a29d95db.pdf)
* FinalCacheTest is the same as LRAwe but for FinalCache.
* FiguresTest gives an overview of the types of observed cache operations.

SizeTest, HistogramTest, and IntervalFinalCacheTest generate output to be used as input for the python graphers.
