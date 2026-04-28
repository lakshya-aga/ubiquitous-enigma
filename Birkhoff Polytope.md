This is an imaginary n-dimensional space containing all convex combinations of all permutations of a given scenario

Imagine a sequence where the sequence can be 1,2,3 or any permutation of it

So a matrix would be:

$$
\begin{bmatrix}
1 & 0 & 0
\\
0 & 1 & 0
\\
0 & 0 & 1

\end{bmatrix}
$$


$$
\begin{bmatrix}
0 & 1 & 0
\\
1 & 0 & 0
\\
0 & 0 & 1

\end{bmatrix}
$$

so a convex combination would be
$$
0.3* \begin{bmatrix}
1 & 0 & 0
\\
0 & 1 & 0
\\
0 & 0 & 1
\end{bmatrix} 

+ 0.7 * \begin{bmatrix}
0 & 1 & 0
\\
1 & 0 & 0
\\
0 & 0 & 1
\end{bmatrix}
$$

So a convex combination of all possible perms makes up the Birkhoff's Polytope
### Why does it live in (n−1)² dimensions?

An n×n matrix has n² entries. The row-sum constraints are n equations, the column-sum constraints are another n — but one of these is redundant (if all rows sum to 1 then columns automatically sum to n, so the column constraints give only n−1 independent equations). Total independent constraints: n + (n−1) = 2n−1. So the dimension is n² − (2n−1) = **(n−1)²**.

For n=3: dimension = 4. You can't visualize it directly, but you can understand it.


Note it only allows permutations without repetitions
For other cases, relax the row or column constraints. Try deviating from this to the combinations or permutations with repetitions

This is used in conjunction with Smoothening using $exp(X/\tau)$ and then feeding into the smoothening to form the basis of The Gumbel-Sinkhorn paper

---

Topics: [[Probability And Statistics for Finance]]
Reference:
Type: #atom