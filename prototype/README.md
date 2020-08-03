# FinalCache
FinalCache uses LRU to evict entries. However it does not use access-history to compute LRU. Rather when objects become unreachable (unused) they become managed by LRU by being resurrected via finalize. FinalCacheEntries (FCEs) remain reachable from the cache via weak reference while the entry is in-use. Once they are resurrected, their mapping is changed from weak to strong. If an entry is accessed while in-use, then the next call to finalize is ignored for a second chance of not being accessed while in-use. 

This implementation relies on the following feature set of C#:
* unsafe/long weak references
* multiple resurrection via finalize
* enable / disable finalize
* explicit GC invocation
* wait for finalize

## .NET Core (Cross-Platform)


> dotnet build --configuration Release

> dotnet run

The configuration tag is important because in dotnetcore versions 2 and later, the default build is debug. In debug mode, all finalize commands may not be executed. This fact took a whole week of frustration to identify after the update from version 1.1.

## Linux:

Required: Mono SDK 

> dmcs Program.cs

> ./Program.exe


## Windows:

Required: Visual Studio or Microsoft Build Tools/SDK

> csc Program.cs

> .\Program.exe
