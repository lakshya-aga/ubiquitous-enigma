
Level 1 categories for CPU cycles are as follows

- **Retiring**: General case
- **Frontend Bound**: Time spent in CPU fetching instructions
- **Backend bound:** memory bound, network bound or execution units busy
- **Bad speculation:** bad branch speculation (`vtable` stuff)

`perf stat -M TopdownL1 bench mem memcpy`


---

Topics: [[High Performance Computing]]
Reference: https://perfwiki.github.io/main/top-down-analysis/
Type: #atom