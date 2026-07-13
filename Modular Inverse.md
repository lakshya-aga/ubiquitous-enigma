
$$
\frac{A}{B}mod{M}
$$
Is not trivially calculated like modular multiplication

Instead we use -:

A/B MOD M -> (A* inv(B)) MOD M

to do this we make use of the extended euclidean algorithm

i.e. x, y, gcd = gcd(A, B)
where x and y are coefficients in

$$
xa+yb=gcd(a,b)
$$

---

Topics: [[Competitve Programming]]
Reference: https://www.geeksforgeeks.org/dsa/modular-division/
Type: #atom