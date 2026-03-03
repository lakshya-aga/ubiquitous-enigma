Cholesky decomposition factors a symmetric positive-definite matrix:
$$
A = LL^\top
$$
where \(L\) is lower triangular.

Why it is preferred (when applicable):
- Roughly half the cost of generic LU on symmetric systems.
- Numerically stable for SPD matrices.

Common quant use-cases:
- Sampling correlated Gaussian vectors.
- Fast solves in covariance-based models.

Prerequisite:
Matrix must be symmetric and strictly positive-definite (not just PSD).

---

Topics: "Linear Algebra, Covariance Modeling, Quant"
Reference: "Golub & Van Loan, Matrix Computations"
Type: #atom
