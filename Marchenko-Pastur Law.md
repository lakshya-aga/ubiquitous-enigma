
This Explains why Shrinkage and PCA are important for covariance matrices to be useful.

AI generated summary: #todo replace with own
Suppose the *true* covariance is the identity Σ=INΣ=IN​ (so the true eigenvalues are all exactly 1). You draw TT samples of NN i.i.d. standard-normal variables and form the sample covariance  

Σ^=1TX⊤X.Σ^=T1​X⊤X.

If estimation worked perfectly, all NN eigenvalues of Σ^Σ^ should also be 1. They're not.

## The Marchenko–Pastur law

As N,T→∞N,T→∞ with the ratio q=N/Tq=N/T fixed, the empirical distribution of eigenvalues of Σ^Σ^ converges to a deterministic density supported on [λ−,λ+][λ−​,λ+​], where  

λ±=(1±q)2.λ±​=(1±q​)2.

Read what that says. The *true* eigenvalues are all 1. The *sample* eigenvalues spread out over an interval of width 4q4q​, centered (roughly) at 1.

Plug in your numbers, N=500N=500, T=1000T=1000, so q=0.5q=0.5:

- λ−=(1−0.5)2≈0.086λ−​=(1−0.5​)2≈0.086
- λ+=(1+0.5)2≈2.914λ+​=(1+0.5​)2≈2.914

So eigenvalues that should all equal 1 are scattered between roughly **0.09 and 2.91**. That's a 34× spread, generated entirely by sampling noise, with zero true signal. The smallest sample eigenvalue is ~12× smaller than the truth — and the inverse Σ^−1Σ^−1 (which is what optimization actually uses, e.g. Markowitz weights ∝Σ^−1μ∝Σ^−1μ) blows up that error.

## The pathological case: q→1q→1

Now imagine N=TN=T exactly. Then q=1q​=1, so λ−=0λ−​=0. The smallest sample eigenvalues *crash into zero*. If N>TN>T, Σ^Σ^ is **singular** — rank deficient — and not even invertible. The "estimate" is mathematically degenerate even though every entry is computed correctly.

This is why N≈TN≈T is the danger zone: you're approaching the edge of the Marchenko–Pastur support.

## Why this is a _proof_ of the variance problem

Marchenko–Pastur tells you the eigenvalue spread is **not** a finite-sample artifact that vanishes with more data — it's a deterministic feature of the N/TN/T ratio. The only way to shrink it is to shrink qq, i.e. get T≫NT≫N. With 500 stocks and daily data, getting T=50,000T=50,000 means ~200 years of stationary returns. Not happening.

So you have two options:

1. Wait 200 years.
2. Add structure (shrinkage, factor models, sparse estimation) — i.e., spend bias to buy variance.

That's why shrinkage isn't a hack; it's a forced move.

---

Topics: 
Reference:
Type: #atom
