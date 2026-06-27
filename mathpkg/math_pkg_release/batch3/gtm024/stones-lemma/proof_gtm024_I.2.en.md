---
role: proof
locale: en
of_concept: stones-lemma
source_book: gtm024
source_chapter: "I"
source_section: "§2. Convex Sets"
---

Let $\mathcal{C}$ be the class of all convex sets in $X$ disjoint from $B$ and containing $A$. Since $A \cap B = \emptyset$ and $A$ is convex, $A \in \mathcal{C} \neq \emptyset$. Partially order $\mathcal{C}$ by inclusion. Any chain in $\mathcal{C}$ has an upper bound (its union, which is convex and still disjoint from $B$). By Zorn's lemma, $\mathcal{C}$ has a maximal element $C$. Set $D = X \setminus C$. We claim $D$ is convex.

Suppose $D$ is not convex. Then there exist $x, z \in D$ and $v \in (x, z) \cap C$. Since $C$ is maximal in $\mathcal{C}$, the convex hull $\operatorname{co}(C \cup \{x\})$ must intersect $B$; let $b_1$ be in this intersection. Similarly, $\operatorname{co}(C \cup \{z\})$ intersects $B$ at some $b_2$. One can then show that a convex combination of $b_1$ and $b_2$ lies in $B \cap C$, contradicting $C \cap B = \emptyset$. Hence $D$ is convex, and $C, D$ are complementary convex sets with $A \subset C$, $B \subset D$.
