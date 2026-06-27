---
role: proof
locale: en
of_concept: fubini-theorem-for-nullsets
source_book: gtm002
source_chapter: "14"
source_section: "14"
---

For any $\varepsilon > 0$, let $I_i \times J_i$ be a sequence of rectangles (with $I_i$ and $J_i$ half-open on the left) such that:
(1) the sequence $I_i \times J_i$ covers $E$ infinitely many times,
(2) $\sum_i |I_i| |J_i| \leq \varepsilon$,
(3) for each $i > 1$, $I_i$ is contained in a single interval of the subdivision determined by the endpoints of $I_1, \ldots, I_{i-1}$.

Define $\phi_0(x) = 0$ and
$$\phi_n(x) = \sum_{i=1}^n \frac{|J_i|}{|I_i|} \chi_{I_i}(x),$$
where $\chi_{I_i}$ is the characteristic function of $I_i$. Then the sequence $\{\phi_n\}$ is increasing and
$$\int \phi_n(x) \, dx = \sum_{i=1}^n |J_i| |I_i|/|I_i| = \sum_{i=1}^n |J_i| |I_i| \leq \varepsilon.$$

Let $A_i$ be the set of $x \in I_i$ such that $\sup_n \phi_n(x) \geq 1$. $A_i$ is either empty or equal to $I_i$, and the $A_i$ are disjoint. Since $\phi_n(x) \geq 1$ on $A_i$ for $n \geq i$, we have
$$\sum_{i=1}^n |A_i| \leq \int \phi_n \, dx \leq \varepsilon.$$

Let $A = \{x : E_x \text{ is not a nullset}\}$. For each $x \in A$ there exists $y$ with $(x, y) \in E$, hence $(x, y) \in I_i \times J_i$ for infinitely many $i$. Let $\{i_k\}$ be indices with $x \in I_{i_k}$. By (1), the sequence $\{J_{i_k}\}$ covers $E_x$ infinitely many times. Since $E_x$ is not a nullset, by Lemma 14.1 the series $\sum |J_{i_k}|$ diverges. Hence $\phi_n(x) \to \infty$ and $x \in A_i$ for some $i$. Thus the $A_i$ cover $A$, and $\sum |A_i| \leq \varepsilon$. Since $\varepsilon > 0$ was arbitrary, $A$ is a linear nullset.
