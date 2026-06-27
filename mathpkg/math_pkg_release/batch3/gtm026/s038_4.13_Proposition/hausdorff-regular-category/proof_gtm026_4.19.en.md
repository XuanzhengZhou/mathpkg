---
role: proof
locale: en
of_concept: hausdorff-regular-category
source_book: gtm026
source_chapter: "4"
source_section: "4.19"
---

The statement that all three image factorization systems on $\mathbf{Hausdorff}$ from 4.8 yield regular categories is presented as a claim supported by a hint for the $E$-co-well-poweredness condition.

For $E = \{\text{maps with dense image}\}$, the proof of $E$-co-well-poweredness proceeds as follows: Let $X$ be a Hausdorff space and let $A$ be a dense subset of $X$. For each $x \in X$, since $A$ is dense, there exists an ultrafilter $\mathcal{U}_x$ on $A$ converging to $x$. Because $X$ is Hausdorff, limits of ultrafilters are unique. Thus the map $x \mapsto \mathcal{U}_x$ is an injection from $X$ into the set of all ultrafilters on $A$. Hence $|X| \leq 2^{2^{|A|}}$, establishing a bound on the cardinality of any $E$-quotient of a given object $A$. Since for a fixed $A$, representatives of $E$-quotients can be chosen to have cardinality bounded in this way, the class of $E$-quotient objects forms a small set.
