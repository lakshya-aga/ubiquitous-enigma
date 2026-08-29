
Level 1 categories for CPU cycles are as follows

- **Retiring**: General case
- **Frontend Bound**: Time spent in CPU fetching instructions
- **Backend bound:** memory bound, network bound or execution units busy
- **Bad speculation:** bad branch speculation (`vtable` stuff)

`perf stat -M TopdownL1 perf bench mem memcpy`

Think of this like `perf stat -M TopdownL1 [executable]` 
Where topDownL1 is a predefined set of metrics

![[Pasted image 20260716172918.png]]

This is the sample of the output

To drill down use `_group` suffix as

`perf stat -M tma_backend_bound_group perf bench mem memcpy`


Then we can drill down in a similar manner as deep as needed

```
  $ perf stat -M tma_ports_utilization_group perf bench mem memcpy

  [... benchmark output truncated ...]

   Performance counter stats for 'perf bench mem memcpy':

         1,812,959      RESOURCE_STALLS.SCOREBOARD       #     16.6 %  tma_ports_utilized_0  (34.73%)
         1,991,726      cpu/EXE_ACTIVITY.3_PORTS_UTIL,umask=0x80/                                     (34.73%)
        14,159,441      CPU_CLK_UNHALTED.THREAD                                              (34.73%)
         6,689,757      CYCLE_ACTIVITY.STALLS_TOTAL                                          (34.73%)
         3,838,402      CYCLE_ACTIVITY.STALLS_MEM_ANY                                        (34.73%)
         3,282,823      UOPS_EXECUTED.CYCLES_GE_3        #     22.9 %  tma_ports_utilized_3m  (52.98%)
        14,324,185      CPU_CLK_UNHALTED.THREAD                                              (52.98%)
        14,599,955      CPU_CLK_UNHALTED.THREAD          #     12.5 %  tma_ports_utilized_2  (65.27%)
         1,823,495      EXE_ACTIVITY.2_PORTS_UTIL                                            (65.27%)
         1,819,926      EXE_ACTIVITY.1_PORTS_UTIL        #     12.5 %  tma_ports_utilized_1  (79.65%)
        14,591,940      CPU_CLK_UNHALTED.THREAD                                              (79.65%)

        0.012931961 seconds time elapsed

        0.008647000 seconds user
        0.004323000 seconds sys
```

Bracket numbers like  (34.73%) imply multiplexing. Multiplexing is reusing the same counter in a round robin fashion so event is not measured throughout but in fractions of the total run time


To avoid multiplexing, just pass that stat as arg -M


---

Topics: [[High Performance Computing]]
Reference: https://perfwiki.github.io/main/top-down-analysis/
Type: #atom