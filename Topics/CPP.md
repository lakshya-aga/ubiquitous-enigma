Type: #topic

Low level programming language often used in finance for features such as speed and mature ecosystem:
- [[CPP Templates]]
- [[CPP Error Handling]]
- [[CPP Concepts and Generic Programming]]
- [[CPP Strings and Regular Expressions]]
- [[Constexpr CPP]]
- [[Move Semantics CPP]]
- [[Noexcept CPP]]

---

Actual list
1.  SPSC queues/lock free programming (lock free queus :'(, hazard ptr eww things in lockless stack and stuff)
2.  Exception-free programming(why are exceptions garbage in c++)
3.  stack unwiniding - 
`for programs that may throw exceptions, stack unwinding is the method to get out of the exception and terminate the program`
4.  memory fences in c++ (atomic_flag and atomic_fences)
5.  TSO in x86
6. Meyer's Pattern for static local initialization
7. std::call_once and it's cost attached 
8. C++ syntax for shm and syncronization constructs!
```cpp
// SHM in boost
#include <boost/interprocess/managed_shared_memory.hpp>
using namespace boost::interprocess;
int main(){
managed_shared_memory shm(create_only, "MySharedMemory", 65536);
int *shared_data = shm.construct<int>("MyInt")(42);
// shared_memory_object::remove("MySharedMemory");
}

// Different process
int main(){
	managed_shared_memory shm(open_only, "MySharedMemory");
	std::pair <int*, managed_shared_memory::size_type> res = shm.find<int>("MyInt");
	
	if (res.first) { 
	std::cout << "Found shared value: " << *(res.first) << std::endl; 
	}
}


```
Notes: 
	no dynamic containers allowed like vectors, stick to PODs, fixed size arrays
	If not unlinked and process crashes, need to clear memory segment manually
9.  SFINAE, type traits and concepts!
10.  CRTP and static interfaces
11. std::construct_at / std::destroy_at
12. efficent allocators to avoid malloc calls: bump allocator, slab/slub, whatever kernel does for sk_buff things
13. std::pmr
14. tc_malloc and other malloc variants
15. attempt iterators implemention for a custom class with type traits
16. nic to user call(network packet in linux both ingress and egress path)
17. user space networking(DPDK) 
`Lakshya: Data plane development kit. configuring NIC to talk to programs directly`
18. _attribute_((packed)) and alignment costs in c++ structs 
`Lakshya: Save memory by bit packing, probably costs more in processing terms fixed alignment enables hardware specialised optimisations`
19. RTTI and why is it evil?
20. SSE, AVX — wide registers and parallel execution 
21. std::ranges!!
22. lambda capture performance gains and losses
`Lakshya: Allow compilers to give inlining benefits by removing overhead of function calls. General pass by value and pass by reference, copy/move variants.`
23. microbenchmarking and tools (perf, objdump, nm, readelf, gdb, valgrind)
24. unittesting basics
25. Rough access numbers for all memory levels
`ns for cache L1, 100s of ns for L2, micro seconds for memory reads and millis for disk I/O based on drive type SSD or HDD`
26. x86 cache coherence protocol (some mesh thing is done now not common bus snooping)

