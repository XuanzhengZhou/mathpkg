---
role: proof
locale: en
of_concept: canonical-well-ordering-well-orders-product
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Canonical Well-Ordering Well-Orders R x R

**Theorem 177.** The canonical ordering $\ll$ well-orders $R \times R$.

*Proof.* (Described in the text as "a straightforward but tedious application of the definitions.") The ordering $\ll$ is defined on $R \times R$ by: $(u,v) \ll (x,y)$ iff either $\max[u,v] < \max[x,y]$, or $\max[u,v] = \max[x,y]$ and $u < x$, or $\max[u,v] = \max[x,y]$ and $u = x$ and $v < y$, where $\max[x,y] = x \cup y$ (Definition 175).

To show $\ll$ well-orders $R \times R$, one must verify: (1) $\ll$ connects $R \times R$ (any two pairs are comparable), which follows because ordinals are well-ordered by $<$ and the three cases exhaust all possibilities; (2) every non-empty subclass of $R \times R$ has a $\ll$-first member, which follows by taking the minimum of $\max[u,v]$ over the subclass, then the minimum of the first coordinate among those, then the minimum of the second coordinate. The key property is that the class of $\ll$-predecessors of any $(u,v)$ is a subset of $(\max[u,v] + 1) \times (\max[u,v] + 1)$, which is a set.
