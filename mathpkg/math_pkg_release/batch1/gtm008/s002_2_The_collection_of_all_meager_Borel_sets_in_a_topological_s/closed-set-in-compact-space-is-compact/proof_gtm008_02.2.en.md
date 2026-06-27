---
role: proof
locale: en
of_concept: closed-set-in-compact-space-is-compact
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

If $A$ is a closed set in the compact space $\langle X, T \rangle$ and if
$$[S \subseteq T] \wedge [A \subseteq \bigcup(S)],$$
then
$$(\forall a \in X - A)[\exists N(a) \subseteq X - A].$$

Consequently
$$X \subseteq \bigcup(S) \cup \bigcup\{N(a) \mid a \in X - A \land N(a) \subseteq X - A\}.$$
Since $\langle X, T \rangle$ is compact there exists a finite collection of sets in $S$,
$$D_1, \ldots, D_n,$$
and a finite collection of sets in $\{N(a) \mid [a \in X - A] \land [N(a) \subseteq X - A]\}$,
$$N(a_1), \ldots, N(a_m),$$
such that
$$X \subseteq D_1 \cup \cdots \cup D_n \cup N(a_1) \cup \cdots \cup N(a_m).$$

Then $A \subseteq D_1 \cup \cdots \cup D_n$, since $A \cap N(a_i) = 0$ for all $i$. Thus $A$ is compact.
