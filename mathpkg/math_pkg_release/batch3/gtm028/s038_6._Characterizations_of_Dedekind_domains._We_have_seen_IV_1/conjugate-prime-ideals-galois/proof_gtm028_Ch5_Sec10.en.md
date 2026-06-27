---
role: proof
locale: en
of_concept: conjugate-prime-ideals-galois
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

By Theorem 3 of Section 2, there exists a prime ideal $\mathfrak{P}$ of $R'$ which lies over $\mathfrak{p}$. We denote by $\mathfrak{P}^{(j)}$ $(1 \leq j \leq q)$ the conjugates of $\mathfrak{P}$, that is, the ideals of the form $s(\mathfrak{P})$ where $s$ is a $K$-automorphism of $L$. Since $R'$ is the integral closure of a subring of $K$, we have $s(R') = R'$ for any $K$-automorphism $s$ of $L$. Hence each $s(\mathfrak{P})$ is also a prime ideal in $R'$ lying over $\mathfrak{p}$.

Suppose there exists a prime ideal $\mathfrak{Q}$ of $R'$ lying over $\mathfrak{p}$ distinct from all $\mathfrak{P}^{(j)}$. Then $\mathfrak{Q}$ cannot be contained in any $\mathfrak{P}^{(j)}$ by complement 1) to Theorem 3 of Section 2, and there exists an element $x \in \mathfrak{Q}$ not in any $\mathfrak{P}^{(j)}$ (see IV, Section 6, Remark at end of section, p. 215). But then none of the conjugates of $x$ is in $\mathfrak{P}$; hence neither is any power of their product. Some such power, however, is in $K$, hence also in $R$ (since $R$ is integrally closed), and hence finally also in $\mathfrak{p} = \mathfrak{Q} \cap R$. Since $\mathfrak{p} \subset \mathfrak{P}$, this is a contradiction.

Thus the primes lying over $\mathfrak{p}$ are exactly the conjugates of $\mathfrak{P}$. For the inequality $efg \leq n$, see Lemma 2 and Theorem 21. Equality in the separable case follows from the fact that the sum of $e_i f_i$ equals $[L:K]$ when $R'_M$ is a finite $R_M$-module (which is guaranteed by separability, Corollary 1 to Theorem 7 of Section 4).
