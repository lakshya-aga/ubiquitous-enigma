
A Chi-squared random variable with k degrees of freedom is defined as sum of k independent draws from a standard normal distribution
More formally:

$$
\sum_{i=1}^{k} N_{i} \sim \chi^{2}(k)
$$

Exercise: What distribution does sample variance follow as a function of k (size of sample)?

Let:
$$
Q = \frac{Ns^{2}}{\sigma^{2}} 
$$
$$
Z_i = \frac{X_{i}- \mu}{\sigma}
$$

$$
\sum(Z-\bar{Z})^{2} = \frac{\sum\limits{(X_i-\bar{X})^2}}{\sigma ^{2}}=\frac{N s^2}{\sigma ^{2}}=Q
$$

$$
\sum(Z-\bar{Z})^{2} = \sum{Z^{2}+ \bar Z ^{2}-2Z\bar Z} = \Sigma{ Z^{2}} -N\bar Z 
$$

But summation of $Z^{2}$ is Chi squared distribution with $k$ degrees of freedom by definition, this is intuitively there already but formally:

Let 
Z = a vector

Form an orthogonal matrix with row = 1/\sqrt{N} on top and fill in the rest anyhow using [Helmert Matrix](https://search.r-project.org/CRAN/refmans/fastmatrix/html/helmert.html) or something else
Multiply vector by this matrix to get Y

Y = AZ

Now Y also follows

---

Topics: [[Probability and Statistics for Finance]]
Reference: [[ChatGPT]]
Type: #atom