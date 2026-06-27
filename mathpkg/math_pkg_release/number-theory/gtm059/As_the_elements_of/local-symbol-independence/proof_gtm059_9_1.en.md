---
role: proof
locale: en
of_concept: local-symbol-independence
source_book: gtm059
source_chapter: "9"
source_section: "1. A Local Pairing with the Logarithmic Derivative"
---

We have:

$$
[x_n, x_n] \equiv [x_n, N_{k,n} x_n] \pmod{n^{1+k}}
$$

$$
\equiv \frac{1}{2} T_k^*(x_n)(x_n(N_{k,n} x_n)) \pmod{n^{1+k}}
$$

$$
\equiv \frac{1}{2} T_k^*(x_n)(x_n(N_{k,n} x_n)) \pmod{n}
$$

$$
\equiv \frac{1}{2} \cdots
$$

By the Weierstrass preparation theorem, we may factor in the local ring:

$$
X - x_k = g(X) h(X)
$$

where

$$
g(X) = b_0 + \cdots + b_{k+1} X' + X^n, \quad b_0 \equiv 0 \pmod{\mathfrak{p}_K},
$$

$$
h(X) = c_1 X + \cdots + c_{k+1} \text{ is a unit power series},
$$

and

$$
T_{k+1,k} = g(X)(h(X))_k.
$$

Proceeding as before, we replace $x_i$ by $f(x_{i+1})$. From the factorization we have $c_i \equiv 1 \pmod{\mathfrak{p}_K}$, hence $h(x_{i+1})^{-1} \equiv 1 \pmod{\mathfrak{p}_K}$. The orthogonality relation then yields the desired congruence. The value is expressed in the projective limit as

$$
T(x_{i+1}) = \varprojlim K_n / (\text{trace map}),
$$

and the map $\delta: T(K_n) \to T(K_n)/(\text{trace map})$ yields the independence statement.

Two cases are distinguished:
(i) $x \neq x_0(x_n)$ and $m \geq 2n + 1$,
(ii) $x \neq x_0(4D^2(x_n))$ and $m \geq n$.
