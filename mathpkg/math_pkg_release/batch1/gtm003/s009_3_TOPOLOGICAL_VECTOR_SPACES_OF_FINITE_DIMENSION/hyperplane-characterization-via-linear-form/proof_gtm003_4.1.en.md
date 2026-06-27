---
role: proof
locale: en
of_concept: hyperplane-characterization-via-linear-form
source_book: gtm003
source_chapter: "1"
source_section: "4.1"
---

If $f \in L^*$ is non-zero, then $M = f^{-1}(0)$ is a maximal proper subspace of $L$ (since $f$ is a linear surjection onto $K$, its kernel has codimension $1$). If, moreover, $x_0 \in L$ is such that $f(x_0) = \alpha$, then $f^{-1}(\alpha) = x_0 + M$ is a hyperplane in $L$. Thus every set $\{x: f(x) = \alpha\}$ with $f \neq 0$ is a hyperplane.

Conversely, if $H$ is a hyperplane, there exist $x_0 \in L$ and a subspace $M$ of codimension $1$ such that $H = x_0 + M$. Choose a linear form $f \in L^*$ with $\ker f = M$ (such an $f$ exists since $M$ has codimension $1$: pick a basis of $L$ extending a basis of $M$ and define $f$ to be $1$ on the additional basis vector and $0$ on $M$). Then $H = \{x: f(x) = f(x_0)\}$. If $g$ is another non-zero linear form and $\beta \in K$ satisfy $H = \{x: g(x) = \beta\}$, then $\ker f = M = \ker g$, which implies $g = \beta' f$ for some $\beta' \neq 0$ in $K$, and $\beta = \beta' \alpha$. Hence $f$ and $\alpha$ are determined up to a common non-zero factor.
