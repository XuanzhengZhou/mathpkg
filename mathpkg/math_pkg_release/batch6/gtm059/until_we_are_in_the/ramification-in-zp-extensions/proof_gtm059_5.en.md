---
role: proof
locale: en
of_concept: ramification-in-zp-extensions
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

Let $S$ be the set of primes of $K$ that ramify in $K_\infty$. For each $n \geq 1$, let $S_n$ be the primes ramifying in $K_n/K$. Since $K_n/K$ is a finite extension, $S_n$ is finite. If a prime $\mathfrak{p}$ ramifies in $K_\infty$, then it must ramify in some finite layer $K_n$, hence $S = \bigcup_n S_n$.

We claim $S$ is finite. If a prime $\mathfrak{p}$ does not divide $p$, then its ramification index in $K_n/K$ divides the degree $p^n$, so either $\mathfrak{p}$ is unramified or its ramification index is a $p$-power. Since $K_\infty/K$ is a $\mathbb{Z}_p$-extension, the inertia group of any prime is a closed subgroup of $\mathbb{Z}_p$, hence either trivial or of finite index.

For primes dividing $p$, the local analysis using completions shows that the ramification is controlled by the $p$-adic logarithm. Over the completion $K_{\mathfrak{p}}$, the maximal abelian extension has a well-known structure, and the $\mathbb{Z}_p$-extension corresponds to a $\mathbb{Z}_p$-quotient of the local unit group. This quotient is finite except for finitely many primes.

Thus $S$ is finite. Moreover, for each $\mathfrak{p} \in S$, after passing to a sufficiently high finite layer $K_{n_0}$, the extension $K_\infty/K_{n_0}$ has the property that all ramified primes are totally ramified. This proves both statements of the lemma.
