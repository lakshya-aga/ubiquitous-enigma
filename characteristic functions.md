These are functions that let us describe the probability distribution using complex numbers

for a random variable X, its characteristic function is:
$$
\phi(X) = E[e^{iuX}] 


$$
$$
e^{iuX}=cos⁡(uX)+{i}.{sin⁡(uX)},
$$

But this is equal to 
$$
\int_{-\infty}^{\infty}f(x)e^{iux}dx
$$
where $f(x)$ is probability distribution function and this entire thing is [[Fourier Transform]] of this function. That is **characteristic function is the Fourier transform of the probability density function**.

---

Topics: [[Stochastic Calculus and Modelling]]
Reference:
Type: #atom