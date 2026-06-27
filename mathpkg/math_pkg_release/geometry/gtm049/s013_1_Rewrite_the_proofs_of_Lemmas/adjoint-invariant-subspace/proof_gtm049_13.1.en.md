---
role: proof
locale: en
of_concept: adjoint-invariant-subspace
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

Assume $[w]f \subseteq [w]$, which means $w f = \lambda w$ for some scalar $\lambda$ (i.e., $w$ is an eigenvector of $f$). Let $v \in [w]^\perp$, so $\sigma(v, w) = 0$. We must show that $v f \in [w]^\perp$, i.e., $\sigma(v f, w) = 0$.

Using the adjoint property:

$$
\sigma(v f, w) = \sigma(v, w f^*).
$$

By part (ii) of this exercise, $w$ is an eigenvector of $f^*$ with eigenvalue $\bar{\lambda}$. Hence $w f^* = \bar{\lambda} w$, and

$$
\sigma(v f, w) = \sigma(v, \bar{\lambda} w) = \lambda \sigma(v, w) = \lambda \cdot 0 = 0.
$$

Thus $v f \in [w]^\perp$, completing the proof. (This is left as Exercise 4(iii) in the source text.)
