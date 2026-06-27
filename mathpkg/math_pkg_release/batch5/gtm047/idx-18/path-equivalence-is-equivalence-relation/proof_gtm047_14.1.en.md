---
role: proof
locale: en
of_concept: path-equivalence-is-equivalence-relation
source_book: gtm047
source_chapter: "14"
source_section: "14"
---

**Proof.** Reflexivity: For any $p \in \operatorname{CP}(X, P_0)$, define $f(t, y) = p(t)$ for all $(t, y) \in D$. Then $f(t, 0) = f(t, 1) = p(t)$ and $f(0, y) = f(1, y) = P_0$, so $p \cong p$.

Symmetry: If $p \cong q$ via a homotopy $f(t, y)$, then define $g(t, y) = f(t, 1-y)$. Then $g(t, 0) = f(t, 1) = q(t)$ and $g(t, 1) = f(t, 0) = p(t)$, with $g(0, y) = g(1, y) = P_0$, so $q \cong p$.

Transitivity: If $p \cong q$ via $f$ and $q \cong r$ via $g$, define

$$h(t, y) = \begin{cases} f(t, 2y) & 0 \leqslant y \leqslant \frac{1}{2}, \\ g(t, 2y-1) & \frac{1}{2} \leqslant y \leqslant 1. \end{cases}$$

Then $h(t, 0) = f(t, 0) = p(t)$, $h(t, 1) = g(t, 1) = r(t)$, and $h(0, y) = h(1, y) = P_0$. The pasting lemma ensures continuity at $y = \frac{1}{2}$, so $p \cong r$.
