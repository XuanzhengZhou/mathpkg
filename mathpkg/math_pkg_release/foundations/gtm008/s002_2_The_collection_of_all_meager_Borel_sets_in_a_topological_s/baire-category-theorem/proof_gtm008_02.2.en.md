---
role: proof
locale: en
of_concept: baire-category-theorem
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

If $B$ is an open meager set in the locally compact Hausdorff space $\langle X, T \rangle$, then there exists an $\omega$-sequence of nowhere dense sets $A_0, A_1, \ldots$ such that
$$B = \bigcup_{\alpha < \omega} A_\alpha.$$

If $B \neq 0$, then by Theorem 3.22,
$$(\exists N_1 \in T)[N_1^- \subseteq B].$$
Since $A_0$ is nowhere dense,
$$(\exists N_2 \subseteq N_1)[N_2 \cap A_0 = 0],$$
for otherwise $N_1 \subseteq A_0^{-0}$, contradicting that $A_0$ is nowhere dense. Then by Theorem 3.22 again,
$$(\exists N_3 \in T)[N_3^- \subseteq N_2].$$

Inductively we define a nested sequence of nonempty open neighborhoods
$$N_{2n+1} \subseteq N_{2n}^- \subseteq N_{2n-1}$$
such that $N_{2n+1} \cap A_n = 0$ and each $N_{2n+1}^-$ is compact.

The family $\{N_{2n+1}^-\}$ has the finite intersection property, so by compactness $\bigcap N_{2n+1}^- \neq 0$. Pick $x \in \bigcap N_{2n+1}^-$. Then for all $n \in \omega$,
$$x \in N_{2n+1} \land N_{2n+1} \cap A_n = 0.$$
Therefore $x \notin \bigcup_{\alpha \in \omega} A_\alpha = B$. This contradicts $x \in N_1^- \subseteq B$, compelling the conclusion $B = 0$.
