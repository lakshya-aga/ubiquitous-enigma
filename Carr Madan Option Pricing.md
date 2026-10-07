The method that enables us to use Fast Fourier Transform for pricing multiple strikes and build volatility smiles efficiently.

Start with price formula as payoff

$$
C = e^{-rT}E[(S-K)^+]
$$
Here we need $q_c(s)$ - the pdf in order to do the pricing
Let s=log S and k = log K

$$
C = e^{-rT} \int_{k}^{\infty}{q_{T}(s).(e^s−e^k)}ds
$$
lower limit is taken as k since otherwise option price is 0
Note: The $e^s$ produced due to the change in varibles is absorbed into q(s) as $$
p_T(e^s)e^s=q_T(s).
$$
This is somewhat hard to evaluate, thus we take C(k) to be equal to c(k) with an additional dampening factor $e^{\alpha k}$ 
$$
c(k) = e^{\alpha k}C(k)
$$
Then apply the [[Fourier Transform]] to get

$$
ψ(v)=∫_{−∞}^∞e^{ivk}c(k) dk
$$

---


citation: https://www.ma.imperial.ac.uk/~ajacquie/IC_Num_Methods/IC_Num_Methods_Docs/Literature/CarrMadan.pdf
Type: #source #academic 
Topics: [[Derivative Pricing]]


