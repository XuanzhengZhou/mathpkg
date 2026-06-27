---
role: exercise
locale: en
chapter: "VI"
section: "32"
exercise_number: 10
---

For still another characterization of capacity define the energy dissipated by a finite set $A$ (or the expected area swept out by the set $A$) as
$$E_n(A) = \sum_{x \in R} P_x[T_A \leq n].$$

Investigate whether $E_n(A) - E_n(B)$ may be normalized appropriately so as to approximate $C(A) - C(B)$ for arbitrary recurrent random walk.

Hint: Consider first the asymptotic Abel sums, showing that
$$\sum_{n=0}^{\infty} t^n [E_n(A) - E_n(\{0\})] \sim \left[ \sum_{n=0}^{\infty} R_n t^n \right]^2 C(A) \text{ as } t \to 1.$$

Here, as usual, $R_n = P_0[T_0 > n]$. Conclude that
$$\lim_{n \to \infty} \frac{E_n(A) - E_n(B)}{\sum_{k=0}^{n} R_k R_{n-k}} = C(A) - C(B)$$
whenever this limit exists. (S. Port has shown [S23] that it exists for arbitrary recurrent random walk.)
