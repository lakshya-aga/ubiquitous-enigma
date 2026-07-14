
-e cycles:u,instructions:u

to specify events to monitor with modifiers

-a to group by cpu, default is by thread

-C 1,2-3 to specify CPUs to monitor

-p to monitor a specific thread with PID

-i to limit inheritance effect

```
perf record ./noploop -
perf annotate -d ./noploop
```
---

Topics: [[High Performance Computing]]
Reference: https://perfwiki.github.io/main/tutorial
Type: #atom