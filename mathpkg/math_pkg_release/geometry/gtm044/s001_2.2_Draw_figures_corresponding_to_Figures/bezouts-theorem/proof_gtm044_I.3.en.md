---
role: proof
locale: en
of_concept: bezouts-theorem
source_book: gtm044
source_chapter: "I"
source_section: "3"
---

# Proof of Bézout's theorem

**Bézout's Theorem.** Let $C_1 = V(p_1)$ and $C_2 = V(p_2)$ be two algebraic curves in $\mathbb{P}^2(\mathbb{C})$, where $p_1, p_2 \in \mathbb{C}[X,Y,Z]$ are homogeneous polynomials with no repeated factors and no common factor. Let $P_1, \ldots, P_k$ be all the points of intersection of $C_1$ and $C_2$. Let $n_{P_i}$ denote the intersection multiplicity of $C_1$ and $C_2$ at $P_i$. Then

$$\sum_{i=1}^{k} n_{P_i} = (\deg p_1) \cdot (\deg p_2).$$

Equivalently, the degree of the intersection is

$$\deg(V(p_1) \cap V(p_2)) = (\deg p_1) \cdot (\deg p_2).$$

**Geometric motivation.** The proof idea is motivated by the fundamental theorem of algebra. Consider a polynomial $q(X) \in \mathbb{C}[X]$: the graph $V(Y - q(X))$ and the line $V(Y)$ intersect at points $(c_i, 0)$ where $q(c_i) = 0$. The multiplicity $r_i$ of a root $c_i$ can be seen geometrically: for sufficiently small $a \neq 0$, the line $L_a = V(Y - a)$ intersects $V(Y - q(X))$ in exactly $r_i$ distinct points clustered near $(c_i, 0)$. The total number of intersection points counted with multiplicity is $\deg q(X)$.

For two curves $C_1, C_2$ in $\mathbb{C}^2$, the intersection multiplicity $n_P$ at an isolated intersection point $P$ is defined analogously: for "most" small translates of one curve, the intersection near $P$ separates into $n_P$ distinct points. Perturbing one curve slightly separates all intersection points, and the total number of distinct points obtained (counted with multiplicity) equals $(\deg p_1) \cdot (\deg p_2)$.

The formal definition of intersection multiplicity and the complete proof of Bézout's theorem are developed in Chapter IV, where the geometric perturbation idea is translated into rigorous algebraic terms using local rings and the resultant.

**Remarks.**
1. The assumption that $p_i$ has no repeated factors is essential: e.g., $V(Y)$ and $V(X^2)$ intersect in only one point ($1 \cdot 2$ would give $2$), but using $V(X)$ instead yields $1 \cdot 1 = 1$ point, which is correct.
2. The assumption that $p_1$ and $p_2$ have no common factor ensures that $V(p_1) \cap V(p_2)$ is a finite set of points (otherwise the curves would share a component).
