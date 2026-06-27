---
role: proof
locale: en
of_concept: sl2-eigenvalue-corollary
source_book: gtm009
source_chapter: "3"
source_section: "7"
---

If $V = 0$, there is nothing to prove. Otherwise, by Weyl's Theorem (6.3), $V$ decomposes as a direct sum of irreducible submodules. Each irreducible is described by the classification theorem, which gives weights $m, m-2, \ldots, -m$ where $m \geq 0$ is an integer (the highest weight). Thus all eigenvalues of $h$ are integers. In each irreducible, the weights are symmetric about $0$, so $\mu$ and $-\mu$ occur equally often (each once per irreducible containing them).

For the second assertion, observe that each irreducible $L$-module of dimension $m+1$ has:
- $\dim V_0 = 1$ and $\dim V_1 = 0$ when $m$ is even,
- $\dim V_0 = 0$ and $\dim V_1 = 1$ when $m$ is odd.

Thus each irreducible contributes exactly $1$ to $\dim V_0 + \dim V_1$, so the total number of irreducible summands equals $\dim V_0 + \dim V_1$.
