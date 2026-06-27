---
role: proof
locale: en
of_concept: balanced-hull-explicit-form
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "17. Balanced sets, absorbent sets"
---

# Proof of Explicit Form of the Balanced Hull

**Theorem (17.4).** If $S$ is a subset of a vector space $E$ over $\mathbb{K}$, then the balanced hull of $S$ is the set $\{\lambda x : x \in S, \lambda \in \mathbb{K}, |\lambda| \leq 1\}$.

*Proof.* Let $A$ be the balanced hull of $S$. Writing $D = \{\lambda \in \mathbb{K} : |\lambda| \leq 1\}$ ($D$ is a closed interval or a closed disc, according as $\mathbb{K} = \mathbb{R}$ or $\mathbb{K} = \mathbb{C}$), the problem is to show that $A = DS$.

Since $S \subset A$ (as $A$ contains $S$) and $A$ is balanced, we have $DS \subset DA \subset A$ by the definition of balanced set (a set $B$ is balanced if $DB \subset B$). On the other hand, it is clear that $DS$ is a balanced set containing $S$: if $|\mu| \leq 1$ and $\lambda x \in DS$ (with $|\lambda| \leq 1$, $x \in S$), then $\mu(\lambda x) = (\mu \lambda)x \in DS$ since $|\mu \lambda| \leq 1$. Therefore $A \subset DS$ by the definition of $A$ as the smallest balanced set containing $S$. Thus $A = DS$. $\square$
