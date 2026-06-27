---
role: proof
locale: en
of_concept: arithmetic-hierarchy-strictness
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

The assertion that $\Sigma_1 \setminus \Pi_1 \neq \varnothing$ is precisely the theorem on the existence of undecidable enumerable sets (Theorem 5.8 of Chapter V). We prove the general case by an analogous diagonal process applied to a versal family.

Let $\{E_k\}$ be a versal family of enumerable $(n+1)$-sets over $\mathbf{Z}^+$, and let $E$ be its total space. Define the diagonal set

$$D = \{ \langle x_1, \ldots, x_n \rangle \mid \langle x_1, \ldots, x_n, x_1, \ldots, x_n \rangle \notin E \}.$$

The set $D$ is clearly $\Pi_n$ (since $E$ is $\Sigma_1$). On the other hand, if $D$ were also $\Sigma_n$, then its complement would be $\Pi_n$, and by the versality property, $D$ would coincide with some $E_k$. The diagonal construction then yields a contradiction:

$$\langle k, \ldots, k \rangle \in D \iff \langle k, \ldots, k \rangle \notin D.$$

Hence $D \in \Pi_n \setminus \Sigma_n$. Taking complements yields sets in $\Sigma_n \setminus \Pi_n$. The strictness follows immediately: $\Sigma_n \neq \Pi_n$ for all $n \geq 1$, which implies $\Sigma_n \subsetneq \Sigma_{n+1}$ and $\Pi_n \subsetneq \Pi_{n+1}$ for all $n$.
