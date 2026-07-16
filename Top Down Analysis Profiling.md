
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

---

Topics: [[High Performance Computing]]
Reference: https://perfwiki.github.io/main/top-down-analysis/
Type: #atom