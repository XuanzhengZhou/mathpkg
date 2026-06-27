---
role: proof
locale: en
of_concept: open-subgroup-of-reals-classification
source_book: gtm027
source_chapter: "1"
source_section: "J"
---

# Proof that an Open Subgroup of the Reals Is Necessarily All of $\mathbb{R}$

**Theorem.** An open subgroup of $\mathbb{R}$ is necessarily identical with $\mathbb{R}$.

*Proof.* Let $G$ be an open additive subgroup of $\mathbb{R}$.

Since $G$ is a subgroup, $0 \in G$. Since $G$ is open, there exists $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \subseteq G$.

Now, for any $x \in \mathbb{R}$, choose $n \in \mathbb{N}$ such that $|x|/n < \varepsilon$. Then $x/n \in (-\varepsilon, \varepsilon) \subseteq G$. Since $G$ is a group, $n \cdot (x/n) = x \in G$.

Thus every real number belongs to $G$, so $G = \mathbb{R}$. $\square$

This argument works for any open subgroup of a connected topological group: an open subgroup is necessarily also closed (its complement is a union of cosets, each of which is open), and in a connected group the only clopen subgroup is the whole group.
