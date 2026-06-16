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
8. C++ syntax for shm and syncornization constructs!9.  SFINAE, type traits and concepts!
9.  CRTP and static interfaces
10. std::construct_at / std::destroy_at
11. efficent allocators to avoid malloc calls: bump allocator, slab/slub, whatever kernel does for sk_buff things
12. std::pmr
13. tc_malloc and other malloc variants
14. attempt iterators implemeation for a custom class with type traits
15. nic to user call(network packet in linux both ingress and egress path)
17 . user space networking(DPDK)
16. _attribute_((packed)) and alignment costs in c++ structs
17. RTTI and why is it evil?
18. SSE, AVX — wide registers and parallel execution 
19. std::ranges!!
20. lambda capture performance gains and losses
21. microbenchmarking and tools (perf, objdump, nm, readelf, gdb, valgrind)
22. unittesting basics
23. Rough access numbers for all memory levels
24. x86 cache coherence protocol (some mesh thing is done now not common bus snooping)
25. forwarding