---
role: proof
locale: en
of_concept: lemma-rank-of-unit-chi-eigenspace
source_book: gtm059
source_chapter: "Iwasawa Theory of Local Units"
source_section: "1"
---

**Proof.** For the first assertion, the integers $U_n$ contain a free submodule over the group ring $\mathbb{Z}_p[G_n]$ of full rank. More precisely, the cyclotomic units generate a free $\mathbb{Z}_p[G_n]$-submodule which, by the exponential map (or the $p$-adic logarithm), maps isomorphically onto a submodule of $U_n$ of finite index. Taking $\chi$-eigenspaces preserves the rank, yielding $\operatorname{rank}_{\mathbb{Z}_p} U_n(\chi) = p^n$ for $\chi \neq 1$.

For the second part, the only torsion in $U_n$ consists of the roots of unity $W_n = \mu_{p^n}$, which lie in the $\omega$-eigenspace (where $\omega$ is the Teichm\"uller character). Hence if $\chi \neq 1$ and $\chi \neq \omega$, the eigenspace $U_n(\chi)$ is torsion-free over $\mathbb{Z}_p$. Since $\mathbb{Z}_p$ is a principal ideal domain, a finitely generated torsion-free $\mathbb{Z}_p$-module is free, so $U_n(\chi)$ is free. The inclusion $U_n(\chi) \subseteq \mathbb{Z}_p^{p^n}$ follows from the rank calculation. $\square$
