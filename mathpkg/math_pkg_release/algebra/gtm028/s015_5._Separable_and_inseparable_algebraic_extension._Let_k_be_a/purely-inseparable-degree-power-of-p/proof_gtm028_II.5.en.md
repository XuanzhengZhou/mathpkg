---
role: proof
locale: en
of_concept: purely-inseparable-degree-power-of-p
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

Let $x$ be purely inseparable over $k$ (so $\operatorname{char}(k) = p \neq 0$). Let $e$ be the least non-negative integer such that $x^{p^e} \in k$, and set $a = x^{p^e}$. Then $a \in k$ and $\sqrt[p]{a} = x^{p^{e-1}} \notin k$ (by minimality of $e$). By Theorem 7, the polynomial $X^{p^e} - a$ is irreducible in $k[X]$. Since $x$ is a root of this polynomial, $X^{p^e} - a$ is the minimal polynomial of $x$ over $k$. By the corollary to Theorem 2 of §2, the degree $[k(x) : k]$ equals the degree of the minimal polynomial, which is $p^e$. Hence every purely inseparable element has degree a power of $p$ over $k$, and every purely inseparable finite extension has degree a power of $p$.
