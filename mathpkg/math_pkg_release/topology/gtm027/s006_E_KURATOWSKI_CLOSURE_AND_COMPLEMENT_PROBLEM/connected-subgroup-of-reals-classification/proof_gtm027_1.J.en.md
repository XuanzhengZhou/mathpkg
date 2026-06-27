---
role: proof
locale: en
of_concept: connected-subgroup-of-reals-classification
source_book: gtm027
source_chapter: "1"
source_section: "J"
---

# Proof of Classification of Connected Subgroups of the Reals

**Theorem.** A connected subgroup of $\mathbb{R}$ is either $\{0\}$ or $\mathbb{R}$.

*Proof.* Let $G$ be a connected additive subgroup of $\mathbb{R}$.

If $G = \{0\}$, we are done.

If $G \neq \{0\}$, then by the classification of additive subgroups (Problem J(a)), either $G$ has a smallest positive element $a > 0$, in which case $G = a\mathbb{Z}$; or $G$ is dense in $\mathbb{R}$.

**Case 1:** $G = a\mathbb{Z}$ for some $a > 0$. Then $G$ is a discrete subgroup. In this case $G$ is not connected: for instance, $\{0\}$ is both open and closed in the subspace topology on $a\mathbb{Z}$ (it is the intersection of $a\mathbb{Z}$ with $(-a/2, a/2)$). This contradicts the assumption that $G$ is connected.

**Case 2:** $G$ is dense in $\mathbb{R}$. Since the only nontrivial connected subgroups of $\mathbb{R}$ are intervals, and a dense subgroup must be all of $\mathbb{R}$, we have $G = \mathbb{R}$. More formally: $\mathbb{R}$ is connected, and a dense connected subspace of a connected space need not be the whole space, but a subgroup that is dense must contain $0$ and being a subspace of $\mathbb{R}$, if it were a proper dense subgroup, it would be totally disconnected (like $\mathbb{Q}$). The only way a subgroup of $\mathbb{R}$ can be connected is if it equals $\{0\}$ or $\mathbb{R}$.

Thus a connected subgroup of $\mathbb{R}$ is either $\{0\}$ or $\mathbb{R}$. $\square$
