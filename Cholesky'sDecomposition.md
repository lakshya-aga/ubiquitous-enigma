Cholesky decomposition factors a symmetric positive-definite matrix:
$$
A = LL^\top
$$
where \(L\) is lower triangular.


Common quant use-cases:
- Sampling correlated Gaussian vectors - correlated returns
- Fast solves in covariance-based models.

```python
import numpy as np
X = pd.read_csv("prices.csv")
A = X.corr() # or X.cov()
L = np.linalg.cholesky(A)
```

Prerequisite:
Matrix must be symmetric and strictly positive-definite (not just PSD).

---

Topics: "Linear Algebra, Covariance Modeling, Quant"
Reference: "Golub & Van Loan, Matrix Computations"
Type: #atom
