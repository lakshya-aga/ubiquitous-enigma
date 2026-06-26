
- Do we ever use dynamic cast? seems to have another direction at runtime -> performance bad
- `reinterpret_cast` realistic use case? maybe in network packets
	- ### High-performance packet processing
		Examples:
		
		- DPDK
		- kernel networking
		- NIC drivers
		- packet analyzers