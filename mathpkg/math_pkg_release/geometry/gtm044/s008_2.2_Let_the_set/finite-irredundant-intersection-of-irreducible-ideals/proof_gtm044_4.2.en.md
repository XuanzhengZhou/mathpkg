---
role: proof
locale: en
of_concept: finite-irredundant-intersection-of-irreducible-ideals
source_book: gtm044
source_chapter: "4"
source_section: "4.2"
---

# Proof of Finite Irredundant Intersection Decomposition of Ideals

**Theorem 4.2.** Every ideal $\mathfrak{a} \subset \mathbb{C}[X_1, \ldots, X_n]$ is a finite irredundant intersection $\mathfrak{a} = \mathfrak{a}_1 \cap \cdots \cap \mathfrak{a}_s$ of irreducible ideals $\mathfrak{a}_i$.

**Proof.** By Corollary 3.6, $\mathbb{C}[X_1, \ldots, X_n]$ is Noetherian; hence its lattice of ideals $(\mathcal{I}, \subset)$ satisfies the a.c.c. Let $\mathcal{S}$ be the set of all ideals of $\mathbb{C}[X_1, \ldots, X_n]$ that do **not** admit a representation as a finite irredundant intersection of irreducible ideals. If $\mathcal{S}$ is nonempty, then by the a.c.c. (equivalently, the maximal condition), $\mathcal{S}$ contains a maximal element $\mathfrak{m}$.

The ideal $\mathfrak{m}$ cannot be irreducible, for otherwise it would be its own (trivial) irredundant intersection representation and would not belong to $\mathcal{S}$. Hence there exist ideals $\mathfrak{b}, \mathfrak{c}$ strictly larger than $\mathfrak{m}$ such that $\mathfrak{m} = \mathfrak{b} \cap \mathfrak{c}$.

Since $\mathfrak{b} \supsetneq \mathfrak{m}$ and $\mathfrak{c} \supsetneq \mathfrak{m}$, the maximality of $\mathfrak{m}$ in $\mathcal{S}$ implies that neither $\mathfrak{b}$ nor $\mathfrak{c}$ belongs to $\mathcal{S}$. Therefore each admits a finite irredundant intersection decomposition into irreducible ideals:

$$\mathfrak{b} = \mathfrak{b}_1 \cap \cdots \cap \mathfrak{b}_p, \qquad \mathfrak{c} = \mathfrak{c}_1 \cap \cdots \cap \mathfrak{c}_q,$$

where each $\mathfrak{b}_i$ and $\mathfrak{c}_j$ is irreducible. Then

$$\mathfrak{m} = \mathfrak{b} \cap \mathfrak{c} = \mathfrak{b}_1 \cap \cdots \cap \mathfrak{b}_p \cap \mathfrak{c}_1 \cap \cdots \cap \mathfrak{c}_q$$

is a finite intersection of irreducible ideals. Although this representation may be redundant (some $\mathfrak{b}_i$ or $\mathfrak{c}_j$ might contain the intersection of the remaining ones), we can remove redundant components one by one to obtain an **irredundant** intersection. This contradicts $\mathfrak{m} \in \mathcal{S}$.

Hence $\mathcal{S}$ must be empty; every ideal of $\mathbb{C}[X_1, \ldots, X_n]$ admits a finite irredundant intersection decomposition into irreducible ideals. $\square$

**Remark.** The above representation need not be unique; see Exercise 4.4 for a counterexample.
