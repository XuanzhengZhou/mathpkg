---
role: proof
locale: en
of_concept: net-continuity-characterization
source_book: gtm036
source_chapter: "2"
source_section: "4"
---
If $f$ is continuous at $x'$ and $\{x_\alpha\}$ is a net converging to $x'$, then for any neighborhood $V$ of $f(x')$, $f^{-1}[V]$ is a neighborhood of $x'$. Since the net eventually lies in $f^{-1}[V]$, its image eventually lies in $V$, so $f(x_\alpha) \to f(x')$.

Conversely, suppose $f$ preserves convergence of all nets but is not continuous at $x'$. Then there exists a neighborhood $V$ of $f(x')$ such that $f^{-1}[V]$ is not a neighborhood of $x'$. This means for every neighborhood $U$ of $x'$, there exists $x_U \in U \setminus f^{-1}[V]$. The family of neighborhoods of $x'$, directed by reverse inclusion, gives a net $\{x_U\}$ converging to $x'$, but $f(x_U) \notin V$ for all $U$, contradicting $f(x_U) \to f(x')$. Thus $f$ must be continuous.
