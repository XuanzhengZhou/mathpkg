---
role: proof
locale: en
of_concept: union-intersection-of-ordered-pair
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Union and Intersection Properties of Ordered Pairs

**Theorem 50.** If $x$ and $y$ are sets, then:
$\bigcup(x,y) = \{x,y\}$, $\bigcap(x,y) = \{x\}$,
$\bigcup\bigcap(x,y) = x$, $\bigcap\bigcap(x,y) = x$,
$\bigcup\bigcup(x,y) = x \cup y$, and $\bigcap\bigcup(x,y) = x \cap y$.

If either $x$ or $y$ is not a set, then $\bigcup\bigcap(x,y) = 0$, $\bigcap\bigcap(x,y) = \mathcal{U}$, $\bigcup\bigcup(x,y) = \mathcal{U}$, and $\bigcap\bigcup(x,y) = 0$.

*Proof.* These identities follow directly from the definition of ordered pair $(x,y) = \{\{x\},\{x,y\}\}$ (Definition 48) and the properties of generalized union and intersection. When $x$ and $y$ are sets, $\{x\}$ and $\{x,y\}$ are sets (Theorem 42), so $(x,y)$ is a set whose only members are $\{x\}$ and $\{x,y\}$. Then $\bigcup(x,y) = \{x\} \cup \{x,y\} = \{x,y\}$, and $\bigcap(x,y) = \{x\} \cap \{x,y\} = \{x\}$. The remaining formulas follow by iterating these operations. When $x$ or $y$ is not a set, $(x,y) = \mathcal{U}$ (Theorem 49), and the formulas follow from Theorem 34.
