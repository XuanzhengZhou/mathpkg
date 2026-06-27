---
role: proof
locale: en
of_concept: decomposition-formulas-moments-semiinvariants
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Decomposition formulas for simple moments and semi-invariants

Let $\xi = (\xi_1, \ldots, \xi_k)^*$ be a random vector and $I_\xi = \{1, 2, \ldots, k\}$ its set of indices. For $I \subseteq I_\xi$, let $\xi_I$ denote the subvector consisting of the components of $\xi$ whose indices belong to $I$. Let $\chi(I)$ be the vector $(\chi_1, \ldots, \chi_k)$ where $\chi_i = 1$ if $i \in I$ and $\chi_i = 0$ otherwise. Define

$$m_\xi(I) = m_\xi^{(\chi(I))}, \quad s_\xi(I) = s_\xi^{(\chi(I))}.$$

That is, $m_\xi(I)$ and $s_\xi(I)$ are the **simple** moments and **simple** semi-invariants of the subvector $\xi_I$.

A decomposition of a set $I$ is an unordered collection of disjoint nonempty sets $I_p$ such that $\bigcup_p I_p = I$.

The decomposition formulas are:

$$m_\xi(I) = \sum_{\Sigma_{p=1}^q I_p = I} \prod_{p=1}^q s_\xi(I_p), \tag{46}$$

$$s_\xi(I) = \sum_{\Sigma_{p=1}^q I_p = I} (-1)^{q-1}(q-1)! \prod_{p=1}^q m_\xi(I_p), \tag{47}$$

where $\sum_{\Sigma_{p=1}^q I_p = I}$ denotes summation over all decompositions of $I$, $1 \leq q \leq N(I)$, with $N(I)$ being the number of elements of $I$.

## Proof

We derive (46) from (44) of Corollary 1. Set $\nu = \chi(I)$. Then in (44), the vectors $\lambda^{(j)}$ appearing in the sum must satisfy $\lambda^{(j)}_i \in \{0, 1\}$ for all $i$, since their sum is $\nu = \chi(I)$ whose components are 0 or 1. Hence each $\lambda^{(j)} = \chi(I_p)$ for some nonempty $I_p \subseteq I$, and the condition $r_1 \lambda^{(1)} + \cdots + r_x \lambda^{(x)} = \nu$ forces each $r_j = 1$ (otherwise some component would exceed 1) and the $I_p$ to be disjoint with union $I$.

Under these simplifications: $\nu! = 1$, $\lambda^{(j)}! = 1$, $r_j = 1$ for all $j$, so $r_j! = 1$, and $x = q$. Formula (44) then reduces to:

$$m_\xi^{(\chi(I))} = \sum_{\Sigma_{p=1}^q I_p = I} \prod_{p=1}^q s_\xi^{(\chi(I_p))},$$

which is exactly (46). Formula (47) is derived analogously from (45), with the factor $(-1)^{q-1}(q-1)!$ replacing $1/q!$ when all $r_j = 1$.
