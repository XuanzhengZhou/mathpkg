---
role: proof
locale: en
of_concept: sum-of-closed-and-finite-dimensional-is-closed
source_book: gtm003
source_chapter: "1"
source_section: "3.3"
---

Let $\phi$ denote the natural map of $L$ onto $L/M$. Since $M$ is closed, $L/M$ is Hausdorff by (2.3). The subspace $\phi(N)$ is a finite-dimensional subspace of the Hausdorff t.v.s. $L/M$, hence $\phi(N)$ is isomorphic to $K_0^{\dim \phi(N)}$ by (3.2). Since $K$ is complete, $K_0^{\dim \phi(N)}$ is complete, so $\phi(N)$ is complete and therefore closed in $L/M$.

Now $M + N = \phi^{-1}(\phi(N))$: indeed, $x \in M + N$ means $x = m + n$ for some $m \in M$, $n \in N$, and then $\phi(x) = \phi(n) \in \phi(N)$; conversely, if $\phi(x) \in \phi(N)$, then $x - n \in M$ for some $n \in N$, so $x \in M + N$. Since $\phi$ is continuous and $\phi(N)$ is closed, $\phi^{-1}(\phi(N)) = M + N$ is closed in $L$.
