---
role: proof
locale: en
of_concept: multiplicativity-of-separable-and-inseparable-degrees
source_book: gtm028
source_chapter: "II"
source_section: "6. Splitting fields and normal extensions"
---

It is sufficient to prove the formula for the separable degree, since the product of the right-hand sides of the two formulas is equal to the product of the left-hand sides, in view of the relation $[\Delta:k] = [\Delta:k]_s \cdot [\Delta:k]_i$ and the multiplicativity of the ordinary degree.

Let $m_0 = [L:k]_s$, $n_0 = [\Delta:L]_s$. By Theorem 16, $n_0$ is the number of $L$-isomorphisms of $\Delta$ into a normal extension $K$ of $k$ containing $\Delta$, and $m_0$ is the number of $k$-isomorphisms of $L$ into $K$. By Lemma 2, each of the $m_0$ $k$-isomorphisms of $L$ has exactly $n_0$ extensions to $k$-isomorphisms of $\Delta$, so the total number of $k$-isomorphisms of $\Delta$ into $K$ is $m_0 n_0$. But by Theorem 16, this number is also $[\Delta:k]_s$. Hence $[\Delta:k]_s = m_0 n_0 = [\Delta:L]_s [L:k]_s$, as required.
