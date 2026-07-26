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

2.  Exception-free programming(why are exceptions garbage in C++)
`Have to call destructors, stack unwinding, more generated binary. For allocations such as move for vector<T>.push_back() -> causes reallocation to copy rather than move objects for exception handling`


3.  stack unwiniding - 
`for programs that may throw exceptions, stack unwinding is the method to get out of the exception and terminate the program. i.e. calling destructors in reverse order of constructor calls. noexcept promises no exception will be returned so compilers don't have to prepare code to catch exceptions -> resulting in smaller binaries and more inlining opportunities.`


4.  memory fences in c++ (atomic_flag and atomic_fences)



5.  TSO in x86 



6. Meyer's Pattern for static local initialization
I did not come across this naturally during my research -> ask Harsh where he found this topic

7. std::call_once and it's cost attached 
```cpp
#inlcude <thread>
#inlcude <mutex>

```

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
```

Why use CRTP?
It gives you static polymorphism: polymorphism without `virtual`. We hate virtual because it creates a virtual table and adds an extra direction for compiler to follow (chhee in performance). 
```


9. std::construct_at / std::destroy_at

10. efficent allocators to avoid malloc calls: bump allocator, slab/slub, whatever kernel does for sk_buff things

11. std::pmr

12. tc_malloc and other malloc variants

13. attempt iterators implemention for a custom class with type traits

14. nic to user call(network packet in linux both ingress and egress path)

15. user space networking(DPDK) 
`Lakshya: Data plane development kit. configuring NIC to talk to programs directly. How? from what I understand: have a shared memory reource to implement a FIFO queue. Continously poll in the process to check for queue entry and write to this queue from NIC.`


16. _attribute_((packed)) and alignment costs in c++ structs 
`Lakshya: Save memory by bit packing, probably costs more in processing terms fixed alignment enables hardware specialised optimisations`


17. RTTI and why is it evil?
`Virtual functions, additional redirection resoled at runtime via a virtual table. dynamic_cast<Dog*>(a) -> will do a similar lookup to get the metadata`
just use :  `-fno-rtti` during compile time


18. SSE, AVX — wide registers and parallel execution 

19. std::ranges!!

20. lambda capture performance gains and losses
`Lakshya: Allow compilers to give inlining benefits by removing overhead of function calls. General pass by value and pass by reference, copy/move variants.`


21. microbenchmarking and tools (perf, objdump, nm, readelf, gdb, valgrind)
[[perf]]

22. unittesting basics

23. Rough access numbers for all memory levels
`ns for cache L1, 100s of ns for L2, micro seconds for memory reads and millis for disk I/O based on drive type SSD or HDD`


24. x86 cache coherence protocol (some mesh thing is done now not common bus snooping)

25. NUMA (Non-unified memory access). Relevance in HFT
`Run time optimisation, memory and CPU on the same node as different nodes can cause significant latencies in memory access. Sidenote: NUMA was introduced because shared memory access was being bottlenecked by the shared bus linking CPU and memory.`
---
Final questions to practice code implementations:

- Given a base and derived pair, refactor the code to use CRTP to save that one virtual table jump
- overload a function to certain behaviour based on the principle of SFINAE.
- No compile time issues for function overloading based on whether a certain property is present or not
- Shared memory management, read/write
- How and when to use different allocation methods
- dynamic allocation code is given, use std::pmr to optimise it/make it predictable


- Drills:

1. Implement `UniquePtr<T>`.
2. Implement `FileHandle`.
3. Implement `Buffer` owning `int*`.
4. Implement `SocketFd`.
5. Implement `ScopeGuard`.
6. Rewrite each using Rule of Zero where possible.


Implementing a custom pointer wrapper
```cpp
#include <iostream>
#include <vector>
using namespace std;
template <typename T>
class Pointer{
    private:
        T& _obj;

    public:
        Pointer(T& obj): _obj(obj){};
        auto operator->(){
            return &_obj;
        }
};

  

int main(){
    vector<int> arr;
    Pointer p(arr);
    p->push_back(10);
    cout<<p->size()<<endl;
    cout<<arr.size()<<endl;

}
```

key insights:
`->` calls `->` recursively