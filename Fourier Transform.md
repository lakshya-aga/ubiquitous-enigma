Fourier Transform of a function is defined as:
$$
\hat{f}(u) = \int_{-\infty}^{\infty}{e^{-iux} f(x)}dx
$$

Inversion is done as:
$$
f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\hat{f}(u) \,du

$$

$e^{iux}$ is the phase factor

- $u$ may be imaginary or real

Additional notes:

The constant coefficient changes in different references. e.g
$\frac{1}{\sqrt{2\pi}}$ in both Fourier transform and inverse

Why is it used in financial derivatives pricing?
It is useful in calibrating and pricing options. This is because it lets us use [[Characteristic Functions]] instead of prob. density functions and integrating the PDF. This is "generally" harder and more expensive computationally.

## Semantically

Semantically say a function is represented as follows
$$
A_1cos(w_1x)+A_2sin(w_2x)...A_ncos(w_nx)
$$
So now we can plot function values and omega
---

Topics: [[Stochastic Calculus and Modelling]]
Reference:
Type: #atom