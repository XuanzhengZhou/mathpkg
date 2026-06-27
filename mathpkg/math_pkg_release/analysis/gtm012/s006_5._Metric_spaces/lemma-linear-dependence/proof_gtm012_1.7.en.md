---
role: proof
locale: en
of_concept: lemma-linear-dependence
source_book: gtm012
source_chapter: "1"
source_section: "7. Vector spaces"
---

# Proof of Lemma 7.2: Characterization of Linear Dependence

Let $X$ be a vector space and $x_1, x_2, \ldots, x_n \in X$, $n \geq 2$.

**($\Rightarrow$)** If $x_1, x_2, \ldots, x_n$ are linearly dependent, there are scalars $a_1, a_2, \ldots, a_n$, not all $0$, such that $\sum_{j=1}^{n} a_j x_j = 0$. Renumbering, we may suppose $a_1 \neq 0$. Then

$$x_1 = \sum_{j=2}^{n} (-a_1^{-1} a_j) x_j.$$

Thus $x_1$ is a linear combination of the others.

**($\Leftarrow$)** Conversely, suppose some $x_k$ is a linear combination of the others. Renumbering, we may assume $x_1 = \sum_{j=2}^{n} b_j x_j$ for some scalars $b_2, \ldots, b_n$. Then

$$(-1) \cdot x_1 + \sum_{j=2}^{n} b_j x_j = 0,$$

which is a nontrivial linear combination (the coefficient of $x_1$ is $-1 \neq 0$) equal to the zero vector. Hence $x_1, x_2, \ldots, x_n$ are linearly dependent. $\square$
