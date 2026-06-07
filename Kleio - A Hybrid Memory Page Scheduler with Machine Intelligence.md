
citation: https://dl.acm.org/doi/epdf/10.1145/3307681.3325398
Type: #source #academic 
Topics: [[ML and operating systems]]

---

This paper examines the simple conjecture that a machine-learning-guided policy for loading hot pages into memory can achieve higher hit rates than currently used heuristics. The first algorithm considered is Reinforcement learning with the problem expressed as:
Program execution burst is a state transition. The Agent must choose what pages to load (policy). Next, the state will provide rewards, i.e., hit rates.
It compares 2 setups. One is the old heuristics-based approach, and one is the "Oracle" which has a priori knowledge - an unrealistic best policy.

The second algorithm proposed is the RNN, specifically LSTMs. The input data is the sequence of page accesses from the memory (not from the cache - more on this).
![[Screenshot 2026-06-07 at 7.11.51 PM.png]]

This graph is essentially the aim. Looking at this, clearly the number of pages accessed for each time stamp are in the order of 1000s. For HPC apps, this can blow up very easily. So the paper takes a flipped approach and instead aims to predict each page's timestamp of being accessed. 