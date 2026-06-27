---
role: proof
locale: en
of_concept: locally-compact-hausdorff-closure-containment
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

If $A$ is an open set in $X$ and $a \in A$, then since $\langle X, T \rangle$ is locally compact, there exists $N(a)$ such that $N(a)^-$ is compact. Let

$$M = (N(a)^- \cap A)^0.$$

Then $M^-$ is also compact. Let

$$T' = \{M^- \cap A \mid A \in T\}.$$

Then $\langle M^-, T' \rangle$ is a compact Hausdorff space. In this space, $M^- - M$ is closed and hence compact.

Moreover,
$$(\forall y \in M^- - M)(\exists N(y))[N(y) \cap M = 0].$$
Since $M^- - M$ is compact, there exist $y_1, \ldots, y_n \in M^- - M$ such that
$$M^- - M \subseteq N(y_1) \cup \cdots \cup N(y_n).$$

Therefore there exists a set $M(a)$ with
$$M(a) \subseteq M^- - [N(y_1) \cup \cdots \cup N(y_n)].$$

Since $N(y_1) \cup \cdots \cup N(y_n)$ is open, $M^- - [N(y_1) \cup \cdots \cup N(y_n)]$ is closed. Hence
$$M(a)^- \subseteq M^- - [N(y_1) \cup \cdots \cup N(y_n)].$$

Therefore
$$M(a)^- \cap [N(y_1) \cup \cdots \cup N(y_n)] = 0$$
and
$$M(a)^- \subseteq M = (N(a)^- \cap A)^0 \subseteq A.$$

Moreover, $M(a) \in T$ (it is the intersection of $M$ with an open set from $T$), so taking $B = M(a)$ yields $a \in B$ and $B^- \subseteq A$.
