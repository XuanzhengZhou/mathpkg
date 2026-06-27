---
role: proof
locale: en
of_concept: lemma-orthogonal-complement-included-in-degenerate-radical
source_book: gtm049
source_chapter: "5"
source_section: "5.2 Orthogonality"
---

Suppose $b \in M^{\perp}$ and $\sigma(M + V^{\perp}, b) = 0$. Then $\sigma(a, b) = 0$ for all $a \in M$ (by definition of $M^{\perp}$) and $\sigma(v, b) = 0$ for all $v \in V^{\perp}$ (since $b$ is orthogonal to $M + V^{\perp}$). This implies $b \in V^{\perp}$ (since $b$ is orthogonal to all of $V = M + V^{\perp}$... [text truncated in source]). Thus $M^{\perp} \subset V^{\perp}$.

Since $M$ is non-degenerate, $M \cap V^{\perp} = 0$ (as $V^{\perp}$ is contained in the radical, and non-degeneracy means the radical restricted to $M$ is trivial). Therefore $M \cap M^{\perp} \subset M \cap V^{\perp} = 0$, giving $M \cap M^{\perp} = 0$.

The same argument with $\top$ in place of $\perp$ yields $M \cap M^{\top} = 0$.
