---
role: proof
locale: en
of_concept: compact-set-closed-in-hausdorff
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

Let $\langle X, T \rangle$ be Hausdorff and $A \subseteq X$ compact. Suppose $b \in A^-$. For each $a \in A$, since $a \neq b$, there exist disjoint neighborhoods $N(a)$ and $N(b)$. The collection $\{N(a) \mid a \in A\}$ covers $A$, so by compactness there is a finite subcover
$$A \subseteq N(a_1) \cup \cdots \cup N(a_n).$$
Moreover $b \notin N(a_1)^-, b \notin N(a_2)^-, \cdots, b \notin N(a_n)^-$. Therefore there exist neighborhoods
$$(\exists N_1(b))[N_1(b) \cap N(a_1) = 0],$$
$$(\exists N_2(b))[N_2(b) \cap N(a_2) = 0],$$
$$\vdots$$
$$(\exists N_n(b))[N_n(b) \cap N(a_n) = 0].$$

If $N(b) = N_1(b) \cap \cdots \cap N_n(b)$, then $N(b) \cap A = 0$. But this contradicts the fact that $b \in A^-$. Therefore $A^- - A = 0$, i.e., $A$ is closed.
