---
role: proof
locale: en
of_concept: bounded-linear-operators-form-normed-algebra
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of The space of bounded linear operators on a normed space is a normed algebra

**Theorem (40.23).** If $E$ is a normed space, then $\mathcal{L}(E) = \mathcal{L}(E, E)$ is a normed algebra, with unity element the identity operator $I$ satisfying $\|I\| = 1$. If, moreover, $E$ is a Banach space, then $\mathcal{L}(E)$ is a Banach algebra.

**Proof.**

The linear operations on $\mathcal{L}(E)$ are the pointwise operations described in (40.4), the norm is the operator norm defined in (40.2), and the multiplication is composition of operators (40.16). The identity operator $I$ is defined by $Ix = x$ for all $x \in E$.

We verify the required properties:

1. *Normed vector space.* By (40.5), $\mathcal{L}(E)$ with the operator norm is a normed space.

2. *Associativity of multiplication.* Composition of linear mappings is associative: $(ST)U = S(TU)$ for all $S, T, U \in \mathcal{L}(E)$.

3. *Distributivity.* The distributive laws hold:
   $$S(T + U) = ST + SU, \quad (S + T)U = SU + TU$$
   for all $S, T, U \in \mathcal{L}(E)$.

4. *Compatibility with scalar multiplication.* For all $S, T \in \mathcal{L}(E)$ and $\lambda \in \mathbb{K}$:
   $$\lambda(ST) = (\lambda S)T = S(\lambda T).$$

5. *Submultiplicativity of the norm.* By (40.17), for all $S, T \in \mathcal{L}(E)$:
   $$\|ST\| \leq \|S\| \cdot \|T\|.$$

6. *Identity.* $Ix = x$ for all $x \in E$. Clearly $\|I\| = \sup\{\|Ix\| : \|x\| \leq 1\} = \sup\{\|x\| : \|x\| \leq 1\} = 1$. Moreover, $IT = TI = T$ for all $T \in \mathcal{L}(E)$.

Thus $\mathcal{L}(E)$ satisfies all axioms of a normed algebra. The completeness statement follows from Theorem (40.7): if $F$ is a Banach space then $\mathcal{L}(E, F)$ is a Banach space. Taking $F = E$, if $E$ is a Banach space then $\mathcal{L}(E)$ is complete in the operator norm, hence a Banach algebra.
