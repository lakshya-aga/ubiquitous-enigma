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

So a convex combination of all possible perms makes up the Brikhoff Polytope

Note it only allows permutatiosn without repetitions
For other cases, relax the row or column constraints. Try deviating from this to the combinations or permutations with repetitions

---

Topics: [[Probability And Statistics for Finance]]
Reference:
Type: #atom