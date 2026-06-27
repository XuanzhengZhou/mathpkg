---
role: proof
locale: en
of_concept: existence-of-nonassociative-division-ring
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

Since $n > 1$, $\mathrm{GF}(p^n)$ has a non-trivial Galois automorphism. Let $\theta$ be the Frobenius automorphism $x \mapsto x^p$ (or any non-identity power). Then $\theta$ has order $m$ where $m \mid n$ and $m > 1$.

Condition (1): $x x^\theta = x^{1+p}$ lies in the subfield fixed by $\theta$, which is contained in the centre (which is all of $F$ since $F$ is a field). So condition (1) is satisfied.

Condition (2): We need to choose $a \in F$ such that $a = x^{1+\theta} + xb$ has no solution. When $F$ is finite, the map $x \mapsto x^{1+\theta}$ (the norm map from $F$ to the fixed field $K = \mathrm{GF}(p^d)$ where $d = \gcd(n, \text{order of }\theta)$) is surjective onto $K$. If we choose $a \notin K + Fb$, then the equation has no solution. Specifically, one can choose $b = 0$ and $a$ to be any element of $F \setminus K$ (since $x^{1+\theta} \in K$ for all $x$). Since $F$ is strictly larger than $K$ when $m > 1$, such an $a$ exists.

With these choices, $D$ is a non-associative division ring by Lemma 9.9 and Theorem 9.7. $\square$
