---
role: proof
locale: en
of_concept: "every-sequentially-compact-metric-space-is-separable"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.36"
---

Let $X$ be a sequentially compact metric space. Tukey's lemma (3.8) shows that for each positive integer $n$ there is a maximal subset $A_n$ of $X$ having the property that $\varrho(x, y) \geq \frac{1}{n}$ for each pair of distinct points $x, y \in A_n$. Each $A_n$ is a finite set since otherwise, for some $n, A_n$ would have an infinite sequence of distinct points with no convergent subsequence. Thus the set $A = \bigcup_{n=1}^{\infty} A_n$ is countable. We assert that $A$ is dense in $X$. If this is not the case, then there exists an $x \in X \cap A^{-'}$. Since $A^{-'}$ is open, there is an $\varepsilon > 0$ such that $B_\varepsilon(x

Then the subsequence $(x_{n_k})$ converges to $x$. Thus (ii) implies (iii). Next suppose that (iii) holds. According to (6.36) $X$ is separable so, by (6.23), $X$ has a countable base $\mathcal{B}$. Now let $\mathcal{U}$ be any open cover of $X$. Let $\mathcal{A} = \{B \in \mathcal{B} : B \subset U$ for some $U \in \mathcal{U}\}$. For each $B \in \mathcal{A}$, choose $U_B \in \mathcal{U}$ such that $B \subset U_B$ and let $\mathcal{V} = \{U_B : B \in \mathcal{A}\}$. Clearly $\mathcal{V}$ is a countable family. If $x \in X$, then $x \in U$ for some $U \in \mathcal{U}$, and since $\mathcal{B}$ is a base, there is a $B \in \mathcal{B}$ such that $x \in B \subset U$. Then $B \in \mathcal{A}$ and $x \in B \subset U_B$. We conclude that $\mathcal{V}$ is a countable subcover of $\mathcal{U}$. Enumerate $\mathcal{V}$ in a sequence $\mathcal{V} = (V_n)$. For each $k \in N$ let $W_k = \bigcup_{n=1}^k V_n$. To prove (i), we need only show that $W_k = X$ for some $k \in N$. Assume that this is false. For each $k$ choose $x_k \in X \cap W_k'$. Then $(x_k)$ has a subsequence $(x_{k_j})$ converging to some $x \in X$. Since $\mathcal{V}$ is a cover there exists a $k_0 \in N$ such that $x \in V_{k_0} \subset W_{k_0}$. Thus $W_{k_0}$ is a neighborhood of $x$ which contains $x_k$ for only finitely many $k$. This contradiction establishes the fact that (iii) implies (i).
