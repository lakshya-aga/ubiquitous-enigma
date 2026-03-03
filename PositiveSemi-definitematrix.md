A matrix \(A\) is positive semi-definite (PSD) if:
$$
x^\top A x \ge 0 \quad \forall x
$$

Equivalent checks for symmetric \(A\):
- all eigenvalues are non-negative,
- it can be interpreted as a covariance-like matrix.

Why it matters:
- Covariance matrices must be PSD.
- Many optimizations (e.g., portfolio variance minimization) assume PSD structure.

Numerical note:
Estimated covariance matrices can lose PSD due to noise; [[Shrinkage]] and projection methods can fix this.

---

Topics: "Linear Algebra, Covariance, Optimization"
Reference: "Boyd & Vandenberghe, Convex Optimization"
Type: #atom
