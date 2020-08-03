# FinalCache
FinalCache uses LRU to evict entries. However it does not use access-history to compute LRU. Rather when objects become unreachable (unused) they become managed by LRU.

## .NET Core (Cross-Platform)


> dotnet build --configuration Release

> dotnet run


## Linux:

Required: Mono SDK 

> dmcs Program.cs

> ./Program.exe


## Windows:

Required: Visual Studio or Microsoft Build Tools/SDK

> csc Program.cs

> .\Program.exe
