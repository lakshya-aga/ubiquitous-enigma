The idea behind this is simple enough to see with a 4 length long array for which we have to compute softmax

$$
S = \frac{e^{i-i_{max}}}{\sum\limits{e^{i-i_{max}}}}
$$
Assume an array of `[2,4,6,1]`

Online Softmax Block 1:
$$
l = e^{2-4}+e^{4-4} = 1.135
$$
Block 2:
$$
l*e^{prevMax - newMax} = 1.135*0.135 = 0.154
$$
$$
l=0.154+e^{6-6}+e^{1-6} = 0.154+1+0.007 = 1.160
$$
Finally, output is scaled with this sum, enabling us to compute running sum without getting max first and then looking at the full thing for sum, causing 2 passes.


Note this optimisation is for the sum only

---

Topics: [[ML Optimisations]]
Reference: https://arxiv.org/html/2205.14135
Type: #atom