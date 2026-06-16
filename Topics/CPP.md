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
`for programmes that may throw exceptions, stack unwinding is the method to get out of the exception and terminate the programme`
4.  memory fences in c++ (atomic_flag and atomic_fences)
5.  TSO in x86
6. Meyer's Pattern for static local initialization
7. std::call_once and it's cost attached 
8. C++ syntax for shm and syncronization constructs!
9.  SFINAE, type traits and concepts!
10.  CRTP and static interfaces
11. std::construct_at / std::destroy_at
12. efficent allocators to avoid malloc calls: bump allocator, slab/slub, whatever kernel does for sk_buff things
13. std::pmr
14. tc_malloc and other malloc variants
15. attempt iterators implemeation for a custom class with type traits
16. nic to user call(network packet in linux both ingress and egress path)
17 . user space networking(DPDK)
17. _attribute_((packed)) and alignment costs in c++ structs
18. RTTI and why is it evil?
19. SSE, AVX — wide registers and parallel execution 
20. std::ranges!!
21. lambda capture performance gains and losses
22. microbenchmarking and tools (perf, objdump, nm, readelf, gdb, valgrind)
23. unittesting basics
24. Rough access numbers for all memory levels
25. x86 cache coherence protocol (some mesh thing is done now not common bus snooping)
26. forwarding