# Cache Tests Javaport

FinalCache cannot be used as a drop-in replacement for existing caches because of the strong coupling between FinalCache and its entries resulting from the use of 
finalize. This code contains a simulation of FinalCache, plus two additional caches for comparison, that uses trace data collected from Firefox. Example log data is 
located in ../fire_logs

Much of this code was written by Aleksandr Diamond [original implemenation on GitHub](https://github.com/asdiamond/cache.tests/tree/javaport). 
The simulation is written in Java and was originally an IntelliJ project. However, during the course of publication it was very difficult to setup the build
environment on another system, so the code has been refactored to run from the terminal. The Python programs that generate the graphs require matplotlib and numpy.

Each caching algorithm has its own Java class and tester. LRUCache and TestUtils serve as the basis for each caching algorithm and tester respectively.

LRUCache extends LinkedHashMap. LRUCache will evict the least recently used entry once its size is exceeded. 
TestUtils knows how to parse the logs and generates the appropirate cache events.

The following is a description of each test and their output:
* LRUTest is for LRA and prints hits, misses, in-use missess, and in-use evictions
* NenovCacheTest is for LRAwe. LRAwe cannot have in-use misses or in-use evictions. We called it Nenov after the strategy of using Soft references for 
evicted entries from Nenov and Dobrikov. [Memory Sensitive Caching in Java](https://pdfs.semanticscholar.org/f1d7/3b7933abcca9842a74c15a48c084a29d95db.pdf)
* FinalCacheTest is the same as LRAwe but for FinalCache.
* FiguresTest gives an overview of the types of observed cache operations.

Be sure to update line 15 of TestUtils to reference the location of your Firefox logs. Do **NOT** have any other files in said directory
aside from log file.

Compile the Java programs with

> javac \*.java

And execute them with

> java \<java_class_file\>

SizeTest, HistogramTest, and IntervalFinalCacheTest generate output to be used as input for the python graphers.

To generate the graphs run

> python \<filename.py\> \< \<corresponding_data_file\>
