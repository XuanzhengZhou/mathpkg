---
role: proof
locale: en
of_concept: every-family-is-a-subbase
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Every Non-Empty Family is a Subbase for Some Topology

**Proposition.** Every non-empty family $s$ of sets is the subbase for some topology, and this topology is uniquely determined by $s$. It is the smallest topology containing $s$ (that is, it is a topology containing $s$ and is a subfamily of every topology containing $s$).

**Proof.** Let $s$ be a non-empty family of sets and let $\mathcal{B}$ be the family of all finite intersections of members of $s$. By the preceding theorem, $\mathcal{B}$ is a base for some topology $\mathcal{J}$ on $X = igcup \{S : S \in s\}$. By definition, $s$ is a subbase for $\mathcal{J}$, since the family of finite intersections of $s$ (namely $\mathcal{B}$) is a base for $\mathcal{J}$.

This topology $\mathcal{J}$ is uniquely determined by $s$ because the family of finite intersections is uniquely determined, and a base uniquely determines the topology (as the family of all unions of members of the base).

To see that $\mathcal{J}$ is the smallest topology containing $s$: any topology containing $s$ must contain all finite intersections of members of $s$ (by the finite intersection axiom), hence must contain $\mathcal{B}$. And any topology containing $\mathcal{B}$ must contain all unions of members of $\mathcal{B}$, hence must contain $\mathcal{J}$. Therefore $\mathcal{J}$ is contained in every topology containing $s$. $\square$