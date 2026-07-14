
- The aim of Data Plane Dev Kit is to provide a framework for fast packet processing in data plane applications. Some Common terms to be used throughout
	- **EAL/`rte_eal`:** Environment Abstraction Layer (EAL) is responsible for gaining access to low level resources such as hardware and memory space. It provides a generic interface that hides the environment specifics from the applications and libraries. It is the responsibility of the initialisation routine to decide how to allocate these resources.
		It provides the interface for the following services:
		- DPDK launching and loading
		- Core affinity and assignment procedures
		- System memory allocation/de-allocation
		- Atomic / lock ops and other utils
		- Timings
		- PCI bus access
		- Trace and debug functions
		- CPU feature identification
		- Interrupt Handling
		- Alarms
	- **`rte_timer`** : Timer facilities
	- **`rte_mempool`**: Handles a pool of objects stored in a ring buffer. allows bulk enqueue/deque and per-CPU cache.
	- **`rte_mbuf`**: Manipulation of packet buffers carrying network data
	- **`rte_ring`**: Fixed-size lockless FIFO for storing objects in a table
	- **`rte_malloc`**: Allocation of names memory zones using `libc malloc()`
	- **`rte_debug`**: Provides debug helpers



			- lcore 
			- port 
			- RX queue
			- TX queue
			- descriptor
			- mempool 
			- rte_mbuf 
			- PMD
			- TX: transmitter
			- RX: receiver
			- RSS: Receive side scaling
			- Ring sizing
		- kernel networking
		- NIC drivers
		- packet analyzers