
- Do we ever use dynamic cast? seems to have another direction at runtime -> performance bad
- `reinterpret_cast` realistic use case? maybe in network packets
	- ### High-performance packet processing
		Examples:
		
		- DPDK:
			- EAL: Environment Abstraction Layer (EAL) is responsible for gaining access to low level resources such as hardware and memory space. It provides a generic interface that hides the environment specifics from the applications and libraries. It is the responsibilty of the initilaisation routine to decide how to 
			- TX: transmitter
			- RX: receiver
			- RSS: Receive side scaling
			- Ring sizing
		- kernel networking
		- NIC drivers
		- packet analyzers