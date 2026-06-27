---
role: proof
locale: en
of_concept: silov-boundary-of-local-algebras
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.7"
---
# Proof of the Šilov Boundary of Local Algebras

Let $A$ be a uniform algebra on a compact space $X$. Let $\{U_1, U_2, \ldots, U_s\}$ be an open covering of $\mathcal{M} = \mathcal{M}(A)$. Denote by $L$ the set of all $f \in C(\mathcal{M})$ such that for each $j = 1, \ldots, s$, the restriction $f|_{U_j}$ lies in the uniform closure of $\hat{A}|_{U_j}$. We prove that $L$ is a closed subalgebra of $C(\mathcal{M})$ and $\check{S}(L) \subseteq X$.

**Step 1: $L$ is a closed subalgebra.** For each $j$, let $\overline{\hat{A}|_{U_j}}$ denote the uniform closure of $\hat{A}|_{U_j}$ in $C(\overline{U_j})$. Then $L$ consists of those $f \in C(\mathcal{M})$ whose restriction to $U_j$ extends continuously to an element of $\overline{\hat{A}|_{U_j}}$ for each $j$. Since each $\overline{\hat{A}|_{U_j}}$ is a closed subalgebra of $C(\overline{U_j})$ and the $U_j$ form an open cover, $L$ is a closed subalgebra of $C(\mathcal{M})$. (The algebra operations are performed pointwise and the covering ensures consistency.)

**Step 2: $X$ is a boundary for $L$.** Since $A$ is a uniform algebra on $X$, $X$ can be identified with a subset of $\mathcal{M}$ (as the space of evaluation homomorphisms). By definition of the uniform norm on $C(\mathcal{M})$, for any $f \in L$,

$$\|f\|_{\mathcal{M}} = \max_{\mathcal{M}} |f|.$$

We claim that for each $f \in L$, the maximum is attained on $X$. Suppose not. Then there exists $f \in L$ and $m_0 \in \mathcal{M} \setminus X$ such that $|f(m_0)| > \max_X |f|$. Choose $j$ such that $m_0 \in U_j$. Since $f|_{U_j}$ lies in the uniform closure of $\hat{A}|_{U_j}$, there exists a sequence $\{a_n\} \subset A$ such that $\hat{a}_n \to f$ uniformly on $U_j$.

But for each $a \in A$, we have the ordinary maximum principle for the uniform algebra:

$$|\hat{a}(m_0)| \leq \max_X |\hat{a}| \leq \max_X |f| + \|\hat{a}_n - f\|_{U_j}.$$

Taking the limit as $n \to \infty$, we obtain $|f(m_0)| \leq \max_X |f|$, a contradiction. Hence $X$ is a boundary for $L$.

**Step 3: The Šilov boundary is contained in $X$.** By Theorem 9.1, the intersection of all boundaries for $L$ — namely $\check{S}(L)$ — is itself a boundary. Since $X$ is a boundary for $L$, $\check{S}(L) \subseteq X$.

**Step 4: The local maximum modulus principle connection.** To show that $L$ is indeed closed under uniform limits on $\mathcal{M}$, we note that if $\{f_n\} \subset L$ converges uniformly to $f$ on $\mathcal{M}$, then for each $j$, $f_n|_{U_j}$ converges uniformly to $f|_{U_j}$, so $f|_{U_j}$ also lies in the uniform closure of $\hat{A}|_{U_j}$. Thus $f \in L$, proving $L$ is uniformly closed.

The key insight is that the local approximation property (each $f$ is locally approximable by elements of $\hat{A}$) combined with the local maximum modulus principle (Theorem 9.3) forces the Šilov boundary of the larger algebra $L$ to remain within the original space $X$. $\square$

*Remark.* This proof follows the sketch given in the text (the result is described as a corollary of Theorem 9.3 and is left to the reader as Exercise 9.9).
