---
role: proof
locale: en
of_concept: esseens-inequality
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Esseen's Inequality

**Theorem (Esseen's Inequality).** Let $G(x)$ be a distribution function having derivative $G'(x)$ with $\sup_x |G'(x)| \leq C$. Then for every $T > 0$,

$$\sup_x |F(x) - G(x)| \leq \frac{2}{\pi} \int_0^T \left| \frac{f(t) - g(t)}{t} \right| dt + \frac{24}{\pi T} \sup_x |G'(x)|,$$

where $f(t)$ and $g(t)$ are the characteristic functions of $F$ and $G$, respectively.

*The proof is not included in the source text.*

**Significance:** Esseen's inequality is a fundamental smoothing inequality in probability theory. It provides a quantitative bound on the uniform distance between two distribution functions in terms of the $L^1$ distance (with weight $1/t$) of their characteristic functions over a finite interval $[0, T]$, plus a term of order $O(1/T)$. This inequality is central to proofs of the Central Limit Theorem with Berry-Esseen-type error bounds, where $G$ is taken to be the standard normal distribution (with $C = 1/\sqrt{2\pi}$) and $F$ is a normalized sum of i.i.d. random variables.

The inequality shows that to bound $\sup_x |F(x) - G(x)|$, it suffices to control the difference of characteristic functions near the origin (the integral term) and to choose $T$ appropriately to balance the two terms.
