
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
But if gcd is 1;
$$
xa + my = 1 (MOD m)
$$$$
```cpp
int gcdExtended(int a, int b, int&x, int&y){

    if(a==0){
        x=0;
        y=1;
        return b;
    }

    int x1, y1;
    int gcd = gcdExtended(b%a, a, x1, y1);
    x = y1 - (b/a)*x1;
    y = x1;
    return gcd;

}
  

int inverse(int i){
    int x, y;
    int g = gcdExtended(i, MOD, x, y);
    if(g!=1)
    return -1;

    return (x%MOD + MOD)%MOD;

}
```


---

Topics: [[Competitve Programming]]
Reference: https://www.geeksforgeeks.org/dsa/modular-division/
Type: #atom