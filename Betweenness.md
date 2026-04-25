Betweenness centrality measures how often a node lies on shortest paths between other nodes.

For node \(v\):
$$
C_B(v)=\sum_{s \ne v \ne t}\frac{\sigma_{st}(v)}{\sigma_{st}}
$$
where:
- $(\sigma_{st})$: number of shortest paths from \(s\) to \(t\)
- $(\sigma_{st}(v)$): those paths passing through \(v\)

Interpretation:
- High betweenness nodes are bridges/bottlenecks.
- Removing them can strongly fragment a network.

---

Topics: "Graph Theory, Networks, [[PlanarMaximallyfilteredGraphs]]"
Reference: "Freeman, L. C. (1977) A set of measures of centrality based on betweenness"
Type: #atom
