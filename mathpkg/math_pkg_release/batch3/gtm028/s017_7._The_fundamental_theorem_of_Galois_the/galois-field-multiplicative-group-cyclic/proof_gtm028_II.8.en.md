---
role: proof
locale: en
of_concept: galois-field-multiplicative-group-cyclic
source_book: gtm028
source_chapter: "II"
source_section: "§8. Galois fields"
---

Let $h = q_1^{r_1} q_2^{r_2} \cdots q_m^{r_m}$ be the decomposition into prime factors of the order $h = p^n - 1$ of the multiplicative group of $GF(p^n)$, and let $h_i = h/q_i$. The polynomial $X^{h_i} - 1$ has at most $h_i$ roots in $GF(p^n)$, and since $h_i < h$ it follows that there exist elements $\neq 0$ in $GF(p^n)$ which are not roots of this polynomial. We fix such an element $\beta_i$ for each $i = 1, 2, \cdots, m$ and we set
\[
y_i = \beta_i^{h/q_i^{r_i}}, \qquad y = y_1 y_2 \cdots y_m.
\]

We have $y_i^{q_i^{r_i}} = \beta_i^h = 1$, whence the order of $y_i$ is a divisor of $q_i^{r_i}$ (see I, §3) and is therefore a power $q_i^{s_i}$ of $q_i$, with $s_i \leq r_i$. On the other hand,
\[
y_i^{q_i^{r_i-1}} = \beta_i^{h/q_i} = \beta_i^{h_i} \neq 1.
\]
Hence $y_i$ is exactly of order $q_i^{r_i}$.

We claim that $h$ is precisely the order of $y$. For assume the contrary. Then the order of $y$ is a proper divisor of $h$ and is therefore a divisor of at least one of the $m$ integers $h/q_i$, say of $h/q_1$. We have then
\[
1 = y^{h/q_1} = y_1^{h/q_1} y_2^{h/q_1} \cdots y_m^{h/q_1}.
\]
Now if $2 \leq i \leq m$, then $q_i^{r_i}$ divides $h/q_1$, and since $y_i$ has order $q_i^{r_i}$, we have $y_i^{h/q_1} = 1$. Therefore $y_1^{h/q_1} = 1$. This implies that the order of $y_1$ must divide $h/q_1$, which is impossible since the order of $y_1$ is $q_1^{r_1}$ and $q_1^{r_1}$ does not divide $h/q_1$. Hence $y$ has order $h$, and the multiplicative group of $GF(p^n)$ is cyclic.
