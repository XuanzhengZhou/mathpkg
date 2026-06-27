---
role: proof
locale: en
of_concept: finite-subring-of-ptr-is-planar
source_book: gtm006
source_chapter: "5"
source_section: "4"
---

**Proof.** Let $(R, T)$ be a PTR and let $(R_0, T)$ be a finite non-empty ternary subring with $R_0 \neq \{0\}$. Since $(R_0, T)$ is a subring of a PTR, it inherits conditions (A) and (B) of Theorem 5.1.

We must show that $(R_0, T)$ satisfies conditions (C), (D), and (E), making it planar.

By Lemma 5.6, equations of the form $T(x, a, b) = T(x, c, d)$ with $a \neq c$ have exactly one solution for $x$ in $R_0$. This gives condition (C) in the case $a \neq 0$ and $c = 0$ (with appropriate choice of $b$ and $d$).

Conditions (D) and (E) follow from Theorem 5.4, since $(R_0, T)$ is a finite ternary ring satisfying (C) and (D) if and only if it also satisfies (E). The verification that (D) holds in $R_0$ uses the fact that $R_0$ is a subring of $(R, T)$, which already satisfies (D).

Finally, since $T(x, a, 0) = T(x, 0, a)$ for $a \in R_0$, $a \neq 0$ has the unique solution $1$ in $R$, we conclude that $1 \in R_0$. Therefore $(R_0, T)$ is a finite ternary ring satisfying conditions (A)–(E), and by Theorem 5.4 and Lemma 5.6, it is planar. $\square$
