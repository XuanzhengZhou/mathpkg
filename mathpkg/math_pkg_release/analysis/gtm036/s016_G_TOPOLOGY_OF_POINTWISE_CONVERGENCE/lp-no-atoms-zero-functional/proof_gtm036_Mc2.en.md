---
role: proof
locale: en
of_concept: lp-no-atoms-zero-functional
source_book: gtm036
source_chapter: "M"
source_section: "M(c)"
---

Suppose $\phi$ is a non-zero continuous linear functional on $L^p$ ($0 < p < 1$). Choose a bounded function $f_0$ vanishing outside a set $A_0$ of finite measure with $\phi(f_0) = 1$.

Since $X$ has no atoms, $A_0$ is not an atom, so there exist disjoint measurable subsets $B$ and $C$ of $A_0$ with $\mu(B) = \mu(C) = \frac{1}{2}\mu(A_0)$. Define $g = 2f_0 \cdot \chi_B$ and $h = 2f_0 \cdot \chi_C$ (equal to $2f_0$ on $B$ resp. $C$, zero elsewhere). Then
$$
\|g\|_p^p = 2^p \int_B |f_0|^p d\mu \leq 2^p \|f_0\|_\infty^p \cdot \frac{1}{2}\mu(A_0) = 2^{p-1} \|f_0\|_\infty^p \mu(A_0),
$$
and similarly for $h$. Since $\phi(g) + \phi(h) = \phi(2f_0 \chi_{B \cup C}) \neq \phi(f_0) = 1$ in general, at least one of $|\phi(g)|$ or $|\phi(h)|$ must be $\geq 1$. Suppose $|\phi(g)| \geq 1$; set $f_1 = g$ and $A_1 = B$.

Repeat this process inductively: given $f_n$ supported on $A_n$ with $|\phi(f_n)| \geq 1$, partition $A_n$ into two equal-measure halves. The function $f_{n+1}$ obtained by doubling $f_n$ on one half has $\|f_{n+1}\|_p^p = 2^{p-1} \|f_n\|_p^p$. Iterating,
$$
\|f_n\|_p^p = (2^{p-1})^n \|f_0\|_p^p.
$$
Since $0 < p < 1$, $2^{p-1} < 1$, so $\|f_n\|_p \to 0$. Yet $|\phi(f_n)| \geq 1$ for all $n$, contradicting the continuity of $\phi$. Hence $\phi$ must be the zero functional.
