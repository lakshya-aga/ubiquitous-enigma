Matrix inversion finds \(A^{-1}\) such that:
$$
AA^{-1}=A^{-1}A=I
$$

Key condition:
- \(A\) must be square and non-singular (\(\det(A)\neq 0\)).

In numerical work:
- Prefer solving linear systems (\(Ax=b\)) via factorization ([[LUdecomposition]], [[Cholesky'sDecomposition]]).
- Explicit inverse is often slower and less stable.

Common use:
- Closed-form derivations and theoretical expressions.
- Precision matrix in Gaussian models.

---

Topics: "Linear Algebra, Numerical Methods"
Reference: "Strang, Introduction to Linear Algebra"
Type: #atom
