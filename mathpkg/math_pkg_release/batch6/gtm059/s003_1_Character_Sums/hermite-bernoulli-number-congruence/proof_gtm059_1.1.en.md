---
role: proof
locale: en
of_concept: hermite-bernoulli-number-congruence
source_book: gtm059
source_chapter: "1"
source_section: "1. Character Sums"
---

The proof uses the congruence relation established in Corollary 1 for the generalized Bernoulli numbers. By Theorem 2.5 (proved in the next chapter), one has the congruence

$$\frac{1}{k} B_{1,\chi} \equiv \frac{1}{p-1+k} B_{1,\chi} \pmod{p}$$

for $k$ in the range $2 \leq k \leq p-3$. Since $B_{1,\chi}$ annihilates $\varphi(\chi^2)$ and satisfies the relation $B_{1,\chi} \equiv a_{p,1} + B_{1,\chi}/p \pmod{p}$, it follows that when $p \nmid B_{1,\chi}$, the value $\varphi(\chi^2) = 0$. Translating back to ordinary Bernoulli numbers via the standard relations between $B_k$ and generalized Bernoulli numbers yields Hermite's classical congruence.
