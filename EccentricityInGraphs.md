The eccentricity of a node \(v\) is its maximum shortest-path distance to any other node:
$$
e(v)=\max_{u \in V} d(v,u)
$$

Graph-level quantities:
- Radius: \(\min_v e(v)\)
- Diameter: \(\max_v e(v)\)

Interpretation:
- Low eccentricity nodes are more central by worst-case distance.
- High eccentricity nodes are peripheral.

Useful for:
- network resilience analysis,
- identifying central/peripheral assets in financial graphs.

---

Topics: "Graph Theory, Networks, Topology"
Reference: "Diestel, Graph Theory"
Type: #atom
