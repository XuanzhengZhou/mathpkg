---
role: proof
locale: en
of_concept: duality-saturated-family
source_book: gtm003
source_chapter: "IV"
source_section: "6"
---

We can assume $S \in \mathfrak{S}$ is convex, circled, and $\sigma(F, G)$-closed (saturated). Let $f \in F^*$ and let $f_S$ be $\mathfrak{S}$-continuous at $0 \in S$; there exists a convex, circled, closed (hence $\sigma(F, G)$-closed) $\mathfrak{S}$-neighborhood $U$ of $0$ such that $|f(x)| \leq \varepsilon$ whenever $x \in S \cap U$. This is equivalent to $f \in \varepsilon(S \cap U)^\circ$, where the polar is taken with respect to $\langle F, F^* \rangle$. Since $S$ and $U$ are a fortiori $\sigma(F, F^*)$-closed, it follows from (1.5), Corollary 2, that $(S \cap U)^\circ$ is contained in the $\sigma(F^*, F)$-closure of $U^\circ + S^\circ$. But $U^\circ$ is compact and $S^\circ$ closed for $\sigma(F^*, F)$, hence by (I, 1.1) $U^\circ + S^\circ$ is closed, and hence $f \in \varepsilon(U^\circ + S^\circ)$. It follows that for some $g \in \varepsilon U^\circ \subset G$, $f - g \in \varepsilon S^\circ$, which means that $|f(x) - g(x)| \leq \varepsilon$ whenever $x \in S$, completing the proof that $G$ is dense in $G_1$ and $G_1$ is complete.
