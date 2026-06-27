---
role: proof
locale: en
of_concept: continuity-positive-linear-forms
source_book: gtm003
source_chapter: "V"
source_section: "5"
---

It is sufficient to consider real linear forms on $E$.

\textbf{(i)} If $C$ has non-empty interior and $f$ is positive, then $f^{-1}(0)$ is a hyperplane in $E$ lying on one side of the convex body $C$, and hence $f^{-1}(0)$ is closed. Therefore $f$ is continuous.

\textbf{(ii)} Suppose $E$ is metrizable and complete and $E = C - C$, but $f$ is a positive linear form on $E$ which is not continuous. Then there exists a bounded sequence $\{x_n\}$ in $C$ such that $f(x_n) > n$ for all $n \in \mathbb{N}$. Since $E$ is locally convex by definition, we conclude that $\{n^{-2}x_n : n \in \mathbb{N}\}$ is a summable sequence in $C$ with sum $z \in C$, say, and it follows that
$$f(z) \geq \sum_{n=1}^{p} n^{-2}f(x_n) > \sum_{n=1}^{p} n^{-1} \quad \text{for all } p,$$
which is impossible. The proof is complete.
