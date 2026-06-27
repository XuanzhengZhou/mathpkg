---
role: proof
locale: en
of_concept: open-set-decomposition-into-domains
source_book: gtm055
source_chapter: "3"
source_section: "General topology"
---

The empty set is the empty union of domains. If $U$ is a nonempty open set in $\mathbb{C}$, and if $\lambda_0$ is an element of some component $U_0$ of $U$, then there is an open disc $D_r(\lambda_0)$ about $\lambda_0$ ($r > 0$) such that $D_r(\lambda_0) \subset U$. Since discs are (arcwise) connected, it is clear that $D_r(\lambda_0) \subset U_0$, and hence the components of $U$ are open. That no collection of disjoint open sets in $\mathbb{C}$ can be uncountable follows from the fact that $\mathbb{C}$ satisfies the second axiom of countability. To complete the proof it suffices to observe that if $\{U_n\}$ is a disjoint (countable) collection of nonempty domains such that $U = \bigcup_n U_n$, and if $V$ is a connected component of $U$ that meets some one $U_n$, then $V \cap \partial U_n = \emptyset$, and therefore $V = U_n$ (by Proposition 3.6).
