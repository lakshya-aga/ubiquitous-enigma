LU decomposition factors a matrix \(A\) into:
$$
A = LU
$$
where \(L\) is lower-triangular and \(U\) is upper-triangular.

Why use it:
- Solve \(Ax=b\) efficiently for many right-hand sides.
- Compute determinant quickly from diagonal of \(U\) (with pivoting sign adjustment).
- Core primitive in numerical linear algebra pipelines.

In practice, partial pivoting is usually used:
$$
PA = LU
$$
to improve numerical stability.

---

Topics:  [[Linear Algebra For Finance]]
Reference: "Golub & Van Loan, Matrix Computations"
Type: #atom
