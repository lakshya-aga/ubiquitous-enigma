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
```cpp

#include <type_traits>
#include <utility>
template <typename T,      
typename = 
std::enable_if_t<std::is_same_v<decltype(std::declval<T().getone()), T>>>
    T make_one() {    
    return T{};
    }

```
9.  CRTP and static interfaces
10. std::construct_at / std::destroy_at
11. efficent allocators to avoid malloc calls: bump allocator, slab/slub, whatever kernel does for sk_buff things
12. std::pmr
13. tc_malloc and other malloc variants
14. attempt iterators implemention for a custom class with type traits
15. nic to user call(network packet in linux both ingress and egress path)
16. user space networking(DPDK) 
`Lakshya: Data plane development kit. configuring NIC to talk to programs directly. How? from what I understand: have a shared memory reource to implement a FIFO queue. Continously poll in the process to check for queue entry and write to this queue from NIC.`
17. _attribute_((packed)) and alignment costs in c++ structs 
`Lakshya: Save memory by bit packing, probably costs more in processing terms fixed alignment enables hardware specialised optimisations`
18. RTTI and why is it evil?
19. SSE, AVX — wide registers and parallel execution 
20. std::ranges!!
21. lambda capture performance gains and losses
`Lakshya: Allow compilers to give inlining benefits by removing overhead of function calls. General pass by value and pass by reference, copy/move variants.`
22. microbenchmarking and tools (perf, objdump, nm, readelf, gdb, valgrind)
23. unittesting basics
24. Rough access numbers for all memory levels
`ns for cache L1, 100s of ns for L2, micro seconds for memory reads and millis for disk I/O based on drive type SSD or HDD`
25. x86 cache coherence protocol (some mesh thing is done now not common bus snooping)
26. NUMA (Non-unified memory access). Relevance in HFT