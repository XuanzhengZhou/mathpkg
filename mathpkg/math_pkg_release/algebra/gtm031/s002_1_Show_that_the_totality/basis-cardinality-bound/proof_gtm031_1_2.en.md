---
role: proof
locale: en
of_concept: basis-cardinality-bound
source_book: gtm031
source_chapter: "1"
source_section: "2"
---

We prove the theorem by induction on $n$.

Let $e_1, e_2, \cdots, e_n$ be a basis and let $x_1, x_2, \cdots, x_{n+1}$ be vectors in $\mathfrak{R}$.

**Base case $n = 1$:** Here $x_1 = \alpha_1 e_1$, $x_2 = \alpha_2 e_1$. Either $x_1 = 0$ (in which case the set is dependent) or $x_2 = \alpha_2 \alpha_1^{-1} x_1$, so $x_1, x_2$ are linearly dependent.

**Inductive step:** Assume the result holds for spaces with bases of $n - 1$ vectors. Suppose the vectors $x_1, x_2, \cdots, x_{n+1}$ are linearly independent. Write each $x_j$ in terms of the basis:

$$
x_j = \alpha_{j1} e_1 + \alpha_{j2} e_2 + \cdots + \alpha_{jn} e_n, \quad j = 1, 2, \ldots, n+1.
$$

Since the $x_j$ are independent, $x_1 \neq 0$, so some $\alpha_{1i} \neq 0$. Without loss, assume $\alpha_{1n} \neq 0$. Define

$$
x_1' = x_1, \qquad x_j' = x_j - \alpha_{jn} \alpha_{1n}^{-1} x_1 \quad (j = 2, \ldots, n+1).
$$

By Lemma 2 (applied repeatedly, or more precisely by elementary transformations), the $x_j'$ are linearly independent. Moreover, $x_2', \ldots, x_{n+1}'$ involve only $e_1, \ldots, e_{n-1}$ (the $e_n$-terms cancel). Thus we have $n$ vectors in the subspace spanned by $e_1, \ldots, e_{n-1}$, which has a basis of $n-1$ elements. By the induction hypothesis, these $n$ vectors are linearly dependent---a contradiction. Hence $x_1, \ldots, x_{n+1}$ must be linearly dependent.

**Corollary of the method:** Any linearly independent subset of a set of vectors $S$ can be embedded in a maximal linearly independent subset of $S$.
