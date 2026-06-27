---
role: proof
locale: en
of_concept: lemma-diagonal-neighborhood-composition
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof of Symmetric Diagonal Neighborhood with Composition Property

**Lemma 30.** Let $X$ be a topological space such that each open cover is even, and let $U$ be a neighborhood of the diagonal $\Delta$ in $X \times X$. Then there exists a symmetric neighborhood $V$ of the diagonal such that $V \circ V \subset U$, where

$$V \circ V = \{(x,z) : \exists y \in X \text{ with } (x,y) \in V \text{ and } (y,z) \in V\}.$$

*Proof.* Since $U$ is a neighborhood of the diagonal, for each point $x \in X$ there exists an open neighborhood $W(x)$ of $x$ such that $W(x) \times W(x) \subset U$. (This follows from the definition of the product topology: the diagonal has a basic open neighborhood contained in $U$, which is of the form $\bigcup_i (W_i \times W_i)$, so each $(x,x)$ lies in some $W_i \times W_i \subset U$.)

The family $\mathcal{W} = \{W(x) : x \in X\}$ is an open cover of $X$. By hypothesis, every open cover of $X$ is even (condition (d) of Theorem 28). Hence there exists a neighborhood $R$ of the diagonal such that for each $z \in X$, the set $R[z] = \{y : (z,y) \in R\}$ is contained in some $W(x_z)$. Consequently,

$$R[z] \times R[z] \subset W(x_z) \times W(x_z) \subset U$$

for each $z \in X$.

Now define $V = R \cap R^{-1}$, where $R^{-1} = \{(y,x) : (x,y) \in R\}$. Then $V$ is a symmetric neighborhood of the diagonal (as the intersection of two neighborhoods of the diagonal). Since $V \subset R$, we have $V[z] \subset R[z]$ for each $z$, and therefore $V[z] \times V[z] \subset U$.

Finally, $V \circ V$ is precisely the union $\bigcup_{z \in X} V[z] \times V[z]$ (if $(x,y) \in V$ and $(y,z) \in V$, then $x \in V^{-1}[y]$ and $z \in V[y]$, so by symmetry $x \in V[y]$ and thus $(x,z) \in V[y] \times V[y]$). Hence $V \circ V \subset U$, as required. $\square$

*Remark.* The intuitive content of this lemma: two points are "at most $U$-distance apart" if $(x,y) \in U$. Then there exists $V$ such that if $x$ and $y$ are at most $V$-distance apart, and $y$ and $z$ are at most $V$-distance apart, then $x$ and $z$ are at most $U$-distance apart. (Compare with the triangle inequality.)
