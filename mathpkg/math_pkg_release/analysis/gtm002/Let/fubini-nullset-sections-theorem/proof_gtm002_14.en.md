---
role: proof
locale: en
of_concept: fubini-nullset-sections-theorem
source_book: gtm002
source_chapter: "14"
source_section: "14. Fubini's Theorem"
---

For any $\varepsilon > 0$ let $I_i \times J_i$ be a sequence of rectangles, with $I_i$ and $J_i$ half-open on the left, such that

(1) the sequence $I_i \times J_i$ covers $E$ infinitely many times, and
(2) $\sum_i |I_i| |J_i| \leq \varepsilon$.

By further subdividing each interval $I_i$ we can insure also that
(3) for each $i > 1$, $I_i$ is contained in a single interval of the subdivision of the line determined by the endpoints of $I_1, I_2, \ldots, I_{i-1}$.

Define $\phi_0(x) = 0$ and $\phi_n(x) = \sum_{x \in I_i, i \leq n} |J_i|$. Let $A_i = \{x : \phi_{i-1}(x) < 1 \leq \phi_i(x)\}$. Then $A_i$ is either empty or equal to $I_i$, and the intervals $A_i$ are disjoint. Since $\phi_n(x) \geq 1$ on $A_i$ for $n \geq i$, we have $\sum_1^n |A_i| \leq \int \phi_n dx$ for each $n$, and therefore $\sum_1^\infty |A_i| \leq \varepsilon$.

Let $A = \{x : E_x \text{ is not a nullset}\}$. For each $x \in A$ we have $(x, y) \in E$ for some $y$, and therefore $(x, y) \in I_i \times J_i$ for infinitely many $i$. Let $\{i_k\}$ be the sequence of indices such that $x \in I_{i_k}$. If $y \in E_x$, then $y \in J_{i_k}$ for infinitely many $k$, by (1). Thus, the sequence $\{J_{i_k}\}$ covers $E_x$ infinitely many times. Since $E_x$ is not a nullset, by Lemma 14.1 the series $\sum |J_{i_k}|$ must diverge. Hence, for each $x \in A$, we have $\lim_{n \to \infty} \phi_n(x) = \infty$, and therefore $x \in A_i$ for some $i$. This shows that the sequence of intervals $A_1, A_2, \ldots$ covers the set $A$. From $\sum |A_i| \leq \varepsilon$, it follows that $A$ is a linear nullset.
