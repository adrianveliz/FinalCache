# FinalCache

The eviction of entries in software caches is meant to limit the cache's total memory footprint. We observe that if an evicted entry is in-use, or reachable, elsewhere in the program, then said eviction will have a negilible reduction in memory usage. Worse yet, a subsequent request for the evicted entry could result in the creation of a duplicate object, increasing memory usage and risking data inconsistency. FinalCache was designed to only evict entries that are unused by the client program without requiring explicit notification of cache entry usage. This repository includes the source code for a prototype FinalCache and the raw data and simulation used to test it. 

What's included in this repo?
* fire_logs contains the raw data used for publication
* prototype includes an implementation of FinalCache written in C# that shows it was possible to create FinalCache without modifying existing languages/runtimes
* simulator uses Java and Python to generate results based on the trace data collected by Firefox for several eviction heuristics
* tools are the scripts used to both generate and filter the raw data

For a complete discussion on FinalCache please see Adrian Veliz's dissertation "FinalCache: Eviction Based on Implicit Entry Reachabilty" available from [SCHOLARWORKS@UTEP](https://scholarworks.utep.edu/open_etd/)

Thank you to Aleksandr Diamond for creating most of the simualation and Dr. Eric Freudenthal for advising.
