
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

There are 2 packet forwarding mechanisms
hash and longest prefix match

			- lcore: logical core
			- port 
			- socket: in DPDK it refers to both the physical sockets as well as NUMA nodes
			- IOCTL: system call to allow applications to communicate with device drivers to perform specific i/o ops
			- RX queue: Reciever queue
			- TX queue
			- descriptor
			- mempool 
			- mbuf: mbuf is a data structure used internally to carry messages(mainly network packets). 
			- pkt_mbuf: mbuf carrying a netwok packet
			- PMD: Poll Mode driver is a driver in DPDK, continuously polling as default behaviour instead of waiting for a HW interrupt.
			- PMD: performance monitoring unit
			- TX: transmitter
			- RX: receiver
			- RSS: Receive side scaling
			- Ring sizing
			- main lcore: lcore that stars the main()
			- MTU: maximum transfer Unit is the size of the largest protocol data unit PDU that can be communicated in a single network layer transactions. In general, it relates to ethernet frame size.
		- L1: Physicl layer reponsible for sending and recieving signals to transmit bits
		- L2: Datalink layer reponsible for local delivery of frames between nodes. eg ethernet
		- L3: network layer reponsible for packet routing, eg. IP
		- L4 Transport layer reponsible for datagram or segment communication (TCP/UDP)
		- kernel networking
		- NIC drivers
		- packet analyzers