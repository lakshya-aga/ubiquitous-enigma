![[Screenshot 2026-02-15 at 9.09.41 PM.png]]

- Mid ground between fully connected graphs vs minimum spanning trees
- Allows edges
- allows cycles
- Show be drawable in a plane
- Max edges 3N - 6
Algorithm to build:
- Sort edges by weights high to low
- Add one by one 
- Check Planarity
- If planarity holds, keep and continue for next node
- If planarity violated, remove and continue for next node
- Continue till 3N-6 edges or edges exhausted
---

Topics: Topology, Clustering, Outlier Detection
Reference: _Tumminello, M., Aste, T., Di Matteo, T. & Mantegna, R. N. A tool for filtering information in complex systems. Proceedings of the National Academy of Sciences
102/30, 10421–10426 (2005).
Type: #atom