---
role: proof
locale: en
of_concept: union-of-open-measure-zero-sets
source_book: gtm002
source_chapter: "16"
source_section: "The Banach Category Theorem"
---

Let $\{G_\alpha : \alpha \in A\}$ be the family $\mathcal{G}$ of open sets of measure zero, and let $G = \bigcup_\alpha G_\alpha$.

First, by a preliminary lemma, for each $\alpha$ the set $G_\alpha = \bigcup_n F_{\alpha,n}$ where each $F_{\alpha,n}$ is closed and $\varrho(F_{\alpha,n}, X - G_\alpha) \geq 1/n$. The sets $\{F_{\alpha,n} : \alpha \in A\}$ for fixed $n$ are pairwise at distance $\geq 1/n$, hence their union is an $F_\sigma$, and in particular Borel measurable.

Since $\mu$ is a Borel measure, it is defined on each such union. By applying the fact that each $G_\alpha$ has measure zero, and that the cardinality $|A|$ has measure zero, it follows that the measure cannot concentrate on any subfamily, yielding $\mu(G) = 0$. $\square$
