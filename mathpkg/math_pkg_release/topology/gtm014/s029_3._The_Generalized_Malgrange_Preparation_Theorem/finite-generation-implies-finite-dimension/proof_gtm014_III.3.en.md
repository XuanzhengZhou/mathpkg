---
role: proof
locale: en
of_concept: finite-generation-implies-finite-dimension
source_book: gtm014
source_chapter: "III"
source_section: "3. The Generalized Malgrange Preparation Theorem"
---

Let $a_1, \ldots, a_k$ be generators of $A$ as a $C_p^\infty(X)$-module. Consider the evaluation map $\operatorname{ev}_p: C_p^\infty(X) \to \mathbf{R}$ given by $[f]_p \mapsto f(p)$. This is a surjective ring homomorphism with kernel $\mathcal{M}_p(X)$, so $\mathbf{R} \cong C_p^\infty(X) / \mathcal{M}_p(X)$.

In the quotient $A / \mathcal{M}_p(X)A$, the action of $\mathcal{M}_p(X)$ annihilates everything, so $A / \mathcal{M}_p(X)A$ is naturally an $\mathbf{R}$-vector space. The images $[a_1], \ldots, [a_k]$ of the generators under the quotient map span $A / \mathcal{M}_p(X)A$ as an $\mathbf{R}$-vector space, since any element $\sum [f_i]_p a_i \in A$ reduces to $\sum f_i(p) [a_i]$ modulo $\mathcal{M}_p(X)A$. Thus $A / \mathcal{M}_p(X)A$ is a finite dimensional real vector space of dimension at most $k$.
