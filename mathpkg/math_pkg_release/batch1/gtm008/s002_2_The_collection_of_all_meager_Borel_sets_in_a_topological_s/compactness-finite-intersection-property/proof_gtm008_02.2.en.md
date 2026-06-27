---
role: proof
locale: en
of_concept: compactness-finite-intersection-property
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

($\Rightarrow$) Suppose $\langle X, T \rangle$ is compact and $S$ is a collection of closed sets with the finite intersection property. Assume $\bigcap(S) = 0$. Then
$$\bigcup\{X - A \mid A \in S\} = X.$$
Since each $X - A$ is open, this is an open cover of $X$. By compactness, there exist $A_1, \ldots, A_n \in S$ such that
$$X = \bigcup_{i \leq n} (X - A_i) = X - \bigcap_{i \leq n} A_i.$$
Therefore $\bigcap_{i \leq n} A_i = 0$, contradicting the finite intersection property.

($\Leftarrow$) Conversely, suppose every collection of closed sets with the finite intersection property has nonempty intersection. If $T'$ is an open cover of $X$ with no finite subcover, then for all $A_1, \ldots, A_n \in T'$,
$$X \not\subseteq \bigcup_{i \leq n} A_i.$$
Equivalently,
$$\bigcap_{i \leq n} (X - A_i) = X - \bigcup_{i \leq n} A_i \neq 0.$$
Thus $\{X - A \mid A \in T'\}$ is a collection of closed sets with the finite intersection property. Then
$$X - \bigcup_{A \in T'} A = \bigcap_{A \in T'} (X - A) \neq 0,$$
i.e., $X \not\subseteq \bigcup(T')$, contradiction. Hence every open cover has a finite subcover.
