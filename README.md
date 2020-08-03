# FinalCache

FinalCache was designed to only evict entries that are unused by the client program without requiring explicit notification of cache entry usage. This repository includes all the source code and raw data used to test FinalCache. 

What's included in this repo?
* fire_logs contains the raw data used for publication
* prototype includes an implementation of FinalCache written in C# that shows it was possible to create FinalCache without modifying existing languages/runtimes
* simulator uses Java and Python to generate results based on the trace data collected by Firefox for several eviction heuristics
* tools are the scripts used to both generate and filter the raw data

For a complete discussion on FinalCache please see Adrian Veliz's dissertation "FinalCache: Eviction Based on Implicit Entry Reachabilty" available from [SCHOLARWORKS@UTEP](https://scholarworks.utep.edu/open_etd/)

Thank you to Aleksandr Diamond for creating most of the simualation and Dr. Eric Freudenthal for advising.
