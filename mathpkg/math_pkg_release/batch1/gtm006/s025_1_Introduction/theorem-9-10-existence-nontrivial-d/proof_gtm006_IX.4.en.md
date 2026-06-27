---
role: proof
locale: en
of_concept: theorem-9-10-existence-nontrivial-d
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

Since $n > 1$, the field $F = GF(p^n)$ admits a non-identity automorphism. Let $\theta$ be the Frobenius automorphism $x \mapsto x^p$, which has order $n$. The fixed field of $\theta$ is $GF(p)$.

We need to find elements $a, b \in F$ satisfying conditions (1) and (2) of the construction. Condition (1) is automatic for finite fields: $F$ has finite dimension over its centre $Z = F$, and $xx^{\theta} \in Z$ holds since the centre is all of $F$.

For condition (2), we need $a = x^{1+\theta} + xb$ to have no solution. Since $\theta \neq 1$, the norm map $x \mapsto x^{1+\theta}$ is not surjective onto $F$. Choose $a$ outside the image of the map $x \mapsto x^{1+\theta} + xb$ for a suitable choice of $b$. Since the equation $x^{1+\theta} + xb = a$ is a polynomial equation of degree $p+1$ in $x$, and $F$ is finite, one can select $a$ and $b$ such that the equation has no solution — for instance, by choosing $b = 0$ and $a$ not in the image of the norm map.

With such choices, the construction yields a division ring $D$ that is not associative (by Lemma 9.9, since $\theta \neq 1$), providing the required non-trivial example.
