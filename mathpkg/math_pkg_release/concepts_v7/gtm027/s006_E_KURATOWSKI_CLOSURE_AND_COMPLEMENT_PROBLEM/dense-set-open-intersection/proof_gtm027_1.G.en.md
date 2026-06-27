---
role: proof
locale: en
of_concept: dense-set-open-intersection
source_book: gtm027
source_chapter: "1"
source_section: "G"
---

# Proof of Dense Set Intersection with Open Set

**Theorem.** If $A$ is dense in a topological space $X$ and $U$ is open, then $U \subseteq (A \cap U)^-$.

*Proof.* Let $x \in U$ and let $V$ be any open neighborhood of $x$. Since $U$ is open, $V \cap U$ is an open neighborhood of $x$. Because $A$ is dense in $X$, every nonempty open set intersects $A$. In particular, $(V \cap U) \cap A \neq \emptyset$.

Thus $V \cap (A \cap U) \neq \emptyset$ for every open neighborhood $V$ of $x$. This means that $x$ belongs to the closure of $A \cap U$; i.e., $x \in (A \cap U)^-$.

Since $x \in U$ was arbitrary, we have $U \subseteq (A \cap U)^-$. $\square$

This result shows that the trace of a dense set on any open set is dense in that open set (with respect to the subspace topology).
