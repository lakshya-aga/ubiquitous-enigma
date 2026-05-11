
**Goal:** Evaluate $I = \int_{-\infty}^{\infty} e^{-x^2}, dx$

Square the integral

$$I^2 = \int_{-\infty}^{\infty} e^{-x^2}, dx \cdot \int_{-\infty}^{\infty} e^{-y^2}, dy = \iint e^{-(x^2 + y^2)}, dx, dy$$

## Switch to polar coordinates

Let $x = r\sin\theta$, $y = r\cos\theta$, so $x^2 + y^2 = r^2$.

$$dx = \sin\theta, dr + r\cos\theta, d\theta$$ $$dy = \cos\theta, dr - r\sin\theta, d\theta$$

By the Jacobian, $dx, dy = r, dr, d\theta$.

## Evaluate in polar form

$$I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2}, r, dr, d\theta$$

Substitute $t = -r^2$, so $dt = -2r, dr$:

$$I^2 = \int_0^{2\pi} \left[ -\tfrac{1}{2} e^{-r^2} \right]_0^{\infty} d\theta = \int_0^{2\pi} \left(-\tfrac{1}{2}\right)(0 - 1), d\theta$$

$$= \tfrac{1}{2} \cdot 2\pi \cdot 1 = \pi$$

## Result

$$\boxed{,I = \sqrt{\pi},}$$

One note: the substitution $x = r\sin\theta$, $y = r\cos\theta$ is swapped from the usual convention (typically $x = r\cos\theta$, $y = r\sin\theta$), but it doesn't affect the result since the integrand depends only on $r^2 = x^2 + y^2$.