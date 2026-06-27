---
role: proof
locale: en
of_concept: kleene-recursion-theorem
source_book: gtm037
source_chapter: "5"
source_section: "1. Recursive Function Theory"
---

We construct a partial recursive function $h'$ by cases on the form of $x$, using the universal function and the s-m-n theorem.

**Case 1.** $x = 2$. Let $h'(x, y, e) = (y)_0 + 1$ for all $y$.

**Case 2.** $x = 2^n \cdot 3^{i+1}$, where $i < n$. Let $h'(x, y, e) = (y)_i$ for all $y$.

**Case 3.** $x = 2^n \cdot 5^n \cdot p_3^q \cdot p_4^{r_0} \cdot \dots \cdot p_{m+3}^{r_{m-1}}$, with $n, m > 0$. Let

$$h'(x, y, e) \simeq \varphi_e^2(q, p_0^{t_0} \cdot \dots \cdot p_{m-1}^{t_{m-1}}),$$

where $t_i \simeq \varphi_e^2(r_i, y)$ for each $i < m$.

**Case 4.** $x = 2 \cdot 7^a \cdot 11^q$ with $q > 0$. Let

$$h'(x, 1, e) = a,$$
$$h'(x, 2^{y+1}, e) \simeq \varphi_e^2(q, 2^y \cdot 3^v),$$

where $v \simeq \varphi_e^2(x, 2^y)$, and

$$h'(x, z, e) = 0$$

for $z$ not of the form $2^u$.

**Case 5.** $x = 2^{m+1} \cdot 11^q \cdot 13^r$ with $m > 0$ and $q > 0$. Let $y$ be given with $(y)_m = 0$. We set

$$h'(x, y, e) \simeq \varphi_e^2(q, y),$$
$$h'(x, y \cdot p_m^{z+1}, e) \simeq \varphi_e^2(r, y \cdot p_m^z \cdot p_{m}^{v+1}),$$

where $v \simeq \varphi_e^2(x, y \cdot p_m^z)$.

This case analysis defines a universal partial recursive function $h'$. By the s-m-n theorem, there is a primitive recursive function $s$ such that $\varphi_{s(x,e)}^{m-1}(\vec{y}) \simeq h'(x, \vec{y}, e)$. Applying the fixed-point theorem to $s$ yields the desired index $e$ with $\varphi_e^{m-1}(\vec{x}) \simeq f(e, \vec{x})$.
