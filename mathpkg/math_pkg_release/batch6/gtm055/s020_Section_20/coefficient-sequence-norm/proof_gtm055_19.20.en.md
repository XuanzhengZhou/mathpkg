---
role: proof
locale: en
of_concept: coefficient-sequence-norm
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

It is an immediate consequence of Proposition 19.1 that $\mathcal{L}$ is a linear space with respect to termwise linear operations. The function $\|a\| = \sup_N \|\sum_{n=0}^{N} \alpha_n x_n\|$ is finite-valued on $\mathcal{L}$ (since a convergent sequence is bounded) and is easily seen to be a pseudonorm. Moreover, if $a = \{\alpha_n\} \neq 0$ and $\alpha_N$ is the first nonzero term, then $\sum_{n=0}^{N} \alpha_n x_n \neq 0$, so $\|a\| > 0$. Thus it is a norm.

To show completeness: if $a = \{\alpha_n\} \in \mathcal{L}$ and $M < N$, then
$$\sum_{n=M+1}^{N} \alpha_n x_n = \sum_{n=0}^{N} \alpha_n x_n - \sum_{n=0}^{M} \alpha_n x_n,$$
so $\|\sum_{n=M+1}^{N} \alpha_n x_n\| \leq 2\|a\|$. In particular, $|\alpha_N| \|x_N\| \leq 2\|a\|$, showing each coordinate functional is bounded on $\mathcal{L}$. If $\{a^{(q)}\}$ is Cauchy in $\mathcal{L}$, then for each fixed $n$, $\{\alpha_n^{(q)}\}$ is Cauchy in $\mathbb{C}$, hence converges to some $\alpha_n$. A standard argument using the uniform bounds shows that $a = \{\alpha_n\} \in \mathcal{L}$ and $a^{(q)} \to a$ in the norm of $\mathcal{L}$.
