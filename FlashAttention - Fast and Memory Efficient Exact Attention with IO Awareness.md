citation: https://arxiv.org/html/2205.14135v2
Type: #source #academic 
Topics: [[ML Optimisations]]

---
The aim of this paper is to show that we can reduce the number of HBM read cycles by being IO aware and use of tiling.
IO awareness here refers to accounting for reads and writes to different levels of fast (SRAM) and slow memory (DRAM).

This video explains well what the paper is trying to say
https://www.youtube.com/watch?v=vLKDOXwun2c

The 2 main speed ups come from tiling and online softmax, which help reduce read write cycles assuming order of N>>d.
[[Online softmax]]