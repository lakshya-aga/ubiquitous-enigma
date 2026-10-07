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
Note: The $e^s$ produced due to the change in variables is absorbed into q(s) as $$
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

which turns into

$$
ψ(v)=e^{−rT}\frac{ϕ_T(v−(α+1)i)}{α^2+α−v^2+i(2α+1)v}
$$
where $\phi$ is the characteristic function symbol

Now recover $C(k)$ through Fourier Inversion

$$
C(k)=e^{−αk}\frac{1}{2π}∫_{−∞}^∞e^{−ivk}ψ(v) dv.
$$


The values are generally computed on a grid
so one transform can be used to price multiple strikes effectively

$$
 {ψ(v_j)}_{j=0}^{N−1}
    
 =>   
    
{C(k_j)}_{j=0}^{N−1}
$$

---


citation: https://www.ma.imperial.ac.uk/~ajacquie/IC_Num_Methods/IC_Num_Methods_Docs/Literature/CarrMadan.pdf
Type: #source #academic 
Topics: [[Derivative Pricing]]


