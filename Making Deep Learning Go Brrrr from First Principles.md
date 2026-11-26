Author: [[Horace He]]
Type: #source #
Link: https://horace.io/brrr_intro.html 
Topics:

---
GPU computations are divided into 2 main components:
- Memory (DRAM)
- Compute + SRAM
DRAM is the slow memory in GPU.
SRAM is what is used by the GPU during compute.

The most popular optimisation in deep learning in operator fusion.

If one operator is being used at a time on some data, then data is moved to DRAM, read again, operated on again, it wastes precious cycles. Why write if you're just going to read right after. Thus, we read operate multiple times and then write back![[Screenshot 2026-11-26 at 2.36.20 PM.png]]
Sometimes you may accidentally turn this off by using pytorch on eager mode, which evaluates eagerly rather than lazily. Lazy loading generally allows optimisations.