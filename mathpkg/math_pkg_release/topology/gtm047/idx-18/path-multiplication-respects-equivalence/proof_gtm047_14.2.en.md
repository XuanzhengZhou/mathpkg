---
role: proof
locale: en
of_concept: path-multiplication-respects-equivalence
source_book: gtm047
source_chapter: "14"
source_section: "14"
---

**Proof.** Let $f$ be a homotopy witnessing $p \cong p'$ and $g$ a homotopy witnessing $q \cong q'$. Define $h: D \to X$ by

$$h(t, y) = \begin{cases} f(2t, y) & 0 \leqslant t \leqslant \frac{1}{2}, \\ g(2t-1, y) & \frac{1}{2} \leqslant t \leqslant 1. \end{cases}$$

Then $h(t, 0) = pq(t)$ (since $f(\cdot, 0) = p$ and $g(\cdot, 0) = q$) and $h(t, 1) = p'q'(t)$. Moreover, $h(0, y) = f(0, y) = P_0$ and $h(1, y) = g(1, y) = P_0$. The pasting lemma ensures $h$ is continuous at $t = \frac{1}{2}$, so $pq \cong p'q'$.
