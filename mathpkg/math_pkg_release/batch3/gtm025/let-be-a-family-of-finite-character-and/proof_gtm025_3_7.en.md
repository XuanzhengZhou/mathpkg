---
role: proof
locale: en
of_concept: "let-be-a-family-of-finite-character-and"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "3.7"
---

It suffices to show that each finite subset of $\cup \mathcal{B}$ is in $\mathcal{F}$. Let $F = \{x_1, \ldots, x_n\} \subset \cup \mathcal{B}$. Then there exist sets $B_1, \ldots, B_n$ in $\mathcal{B}$ such that $x_j \in B_j$ ($j = 1, \ldots, n$). Since $\mathcal{B}$ is a chain there is a $j_0 \in \{1, \ldots, n\}$ such that $B_j \subset B_{j_0}$ for each $j = 1, \ldots, n$. Then $F \subset B_{j_0} \in \mathcal{F}$. But $\mathcal{F}$ is of finite character, and so $F \in \mathcal{F}$.

There are many problems in set theory, algebra, and analysis to which the axiom of choice in the form (3.2) is not immediately applicable, but to which one or another equivalent axiom is applicable at once. We next list four such statements. The names “lemma” and “theorem” are attached to them only for historical reasons, as they are all equivalent to Axiom (3.2).

(3.8) Tukey’s Lemma. Every nonvoid family of finite character has a maximal member.

(3.9) Hausdorff Maximality Principle. Every nonvoid partially ordered set contains a maximal chain.

(3.10) Zorn’s Lemma. Every nonvoid partially ordered set in which each chain has an upper bound has a maximal element.

(3.11) Well-ordering Theorem [ZERMELO]. Every set can be well ordered; i.e., if $S$ is a set, then there exists some well-ordering $\leq$ on $S$.
