---
role: proof
locale: en
of_concept: nonempty-sets-lack-equalizers
source_book: gtm026
source_chapter: "1"
source_section: "1.16"
---

Let $f, g: A \to B$ be a pair of functions between nonempty sets which do not agree on any element of $A$. Such a pair always exists: take $A$ and $B$ to be any nonempty sets with at least two elements each, and define $f$ and $g$ to differ at every point.

Suppose, for contradiction, that $i: E \to A$ is an equalizer of $f$ and $g$. Then $i.f = i.g$, so for every $x \in E$, we have $f(i(x)) = g(i(x))$. Since all objects in this category are nonempty sets, $E$ is nonempty, so there exists $x \in E$. Then $f$ and $g$ agree on $i(x) \in A$, contradicting the choice of $f$ and $g$. Hence no equalizer exists.
