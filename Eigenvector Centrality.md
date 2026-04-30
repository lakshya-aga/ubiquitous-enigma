Eigenvector centrality scores a node by both:
- how many neighbors it has, and
- how important those neighbors are.

It solves:
$$
Ax = \lambda x
$$
where \(A\) is adjacency matrix and \(x\) is the centrality vector (principal eigenvector).

Interpretation:
- High score means "connected to well-connected nodes."
- Better than plain degree when influence propagation matters.

Used in:
- network ranking,
- contagion analysis,
- financial correlation graph analysis.

---

Topics: "Graph Theory, Networks, [[Planar Maximally Filtered Graphs]]"
Reference: "Newman, Networks: An Introduction"
Type: #atom
