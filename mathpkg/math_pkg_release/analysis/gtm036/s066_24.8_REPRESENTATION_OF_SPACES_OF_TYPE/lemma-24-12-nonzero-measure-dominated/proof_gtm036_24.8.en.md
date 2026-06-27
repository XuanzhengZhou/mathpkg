---
role: proof
locale: en
of_concept: lemma-24-12-nonzero-measure-dominated
source_book: gtm036
source_chapter: "24"
source_section: "24.8"
---

As a preliminary, it is to be observed that, if $A$ is a Borel subset of $X$, then there is an open and closed subset $A'$ of $X$ such that the symmetric difference $(A \sim A') \cup (A' \sim A)$ is of category one. This may be proved by showing that the class $\mathcal{A}$ of all sets $A$ such that, for some open set $C$, the symmetric difference of $A$ and $C$ is of first category, is closed under countable union and complementation, and contains all compact sets and hence all Borel sets (this is a well-known lemma of set theory). Since each open set $C$ differs from the open and closed set $C^-$ by a nowhere dense set, the stated result follows.

Turning to the proof of the lemma, it is first shown that if $p$ is a positive measure belonging to $E$ (more precisely, if $p = m_x$ for some $x \in E$), and if $U$ is an open subset of $X$ on which $n$ vanishes, then the measure $p_U$ defined by $p_U(B) = p(B \cap U)$ also belongs to $E$.

Since $n$ vanishes on each compact subset of $U$, $n(U) = 0$. It follows that $n(U^-) = 0$. Let $A$ be the complement of $U^-$ in $X$; then $A$ is open and closed, and it has the properties: $n(X \sim A) = 0$, and if $B$ is a non-void open subset of $A$, then $n(B) > 0$.

From this fact it follows that a Borel subset $B$ of $A$ is of category one if and only if $n(B) = 0$, for given such a set $B$ there is an open set $B'$ such that $(B \sim B') \cup (B' \sim B)$ is of category one, hence $n(B) = n(B') = 0$, therefore $B'$ is disjoint from $A$, and consequently $B$ is a subset of the first category set $B \sim B'$. It follows that a Borel set $B$ in $X$ is of $n$-measure $0$ if and only if $B \cap A$ is of the first category.

Finally, let $f$ be the characteristic function of $A$, and choose a positive measure $p$ in $E$ such that $\int f\,dp \neq 0$. Then, applying the result of the second paragraph, $p_A \in E$, and clearly $p_A \neq 0$. In view of the characterization of the null sets of $n$, $p_A$ is absolutely continuous with respect to $n$, and by virtue of the Radon-Nikodym theorem there is a non-negative Borel function $g$ such that $p_A(B) = \int_B g\,dn$ for any Borel set $B$ in $X$. For some positive integer $r$ the set $C = \{x: g(x) \leq r\}$ has a positive $p_A$-measure. Then $p_A \cap C$ is a non-zero element of $E$ and is dominated by $rn$; the lemma is proved.
