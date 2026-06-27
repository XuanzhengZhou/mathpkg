---
role: proof
locale: en
of_concept: bounding-existential-quantifier-corollary
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

By Theorem 9.14, for each fixed tuple $a_1, \ldots, a_n \in M_{\alpha}$, there exists $\beta$ such that $\llbracket (\exists y)\varphi(a_1, \ldots, a_n, y) \rrbracket = \sum_{a \in M_{\beta}} \llbracket \varphi(a_1, \ldots, a_n, a) \rrbracket$. The set of all such tuples from $M_{\alpha}$ forms a set (since $M_{\alpha}$ is a set). By taking the supremum of the corresponding $\beta$'s, one obtains a single $\beta$ that works uniformly for all $a_1, \ldots, a_n \in M_{\alpha}$. This uses the fact that $B$ is a set and the construction of $M$ ensures that the required supremum exists.
