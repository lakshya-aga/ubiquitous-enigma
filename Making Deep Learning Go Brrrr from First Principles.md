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

A nice way to determine this is to use a simple repetition of operations to see how much time is actually being spent in memory.
Example:
```python
def f(x: Tensor[N]):
    for _ in range(repeat):
        x = x * 2
    return x
```
With a Fusion compiler like NVFuser.
We can change different `repeat` values to see how it scales with operations. A crude way to put it is: take `repeat` value of 1, and 2. Difference it. You get the time spent in computation. The rest of it is memory bandwidth cost.
## [Colab](https://colab.research.google.com/drive/1Ao0GorwaNh88Y5hiGI74A5TSDQMu97oY) Notebook for measuring compute Intensity


