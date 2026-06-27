---
role: proof
locale: en
of_concept: infinite-cardinal-sum
source_book: gtm055
source_chapter: "1"
source_section: "1"
---

The authors provide the following sketch: Let $X$ be a set with $\operatorname{card} X = c$. Consider the collection of all disjoint collections of countably infinite subsets of $X$. By Zorn's lemma (equivalently, the well-ordering principle), there exists a maximal such disjoint collection $\mathcal{F}$. Let $Y = \bigcup \mathcal{F}$. Then $\operatorname{card} Y = \aleph_0 \cdot \operatorname{card} \mathcal{F}$.

If $X \setminus Y$ is infinite, it contains a countably infinite subset, contradicting the maximality of $\mathcal{F}$. Hence $X \setminus Y$ is finite, and $c = \operatorname{card} X = \operatorname{card} Y = \aleph_0 \cdot \operatorname{card} \mathcal{F}$. By the associativity of cardinal multiplication, it follows that $\aleph_0 c = c$.

For the sum formula: if $c$ is infinite and $d \leq c$, then $c + d \leq c + c \leq c \cdot \aleph_0 = c$, so $c + d = c = c \vee d$. The finite collection case follows by induction.
