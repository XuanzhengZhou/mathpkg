---
role: proof
locale: en
of_concept: first-isomorphism-theorem-linear-spaces
source_book: gtm036
source_chapter: "0"
source_section: "F"
---

Define $\tilde{T} : E/N \to F$ by $\tilde{T}(x + N) = T(x)$.

**Well-defined:** If $x + N = y + N$, then $x - y \in N = \ker T$, so $T(x - y) = 0$, hence $T(x) = T(y)$. Thus $\tilde{T}(x + N)$ is independent of the representative chosen.

**Linearity:** For $x + N, y + N \in E/N$ and $\alpha \in K$,
$$
\tilde{T}((x + N) + (y + N)) = \tilde{T}(x + y + N) = T(x + y) = T(x) + T(y) = \tilde{T}(x + N) + \tilde{T}(y + N),
$$
$$
\tilde{T}(\alpha(x + N)) = \tilde{T}(\alpha x + N) = T(\alpha x) = \alpha T(x) = \alpha \tilde{T}(x + N).
$$

**Injectivity:** If $\tilde{T}(x + N) = 0$, then $T(x) = 0$, so $x \in N$, hence $x + N = N = 0_{E/N}$. Thus $\ker \tilde{T} = \{0\}$.

**Surjectivity onto $T(E)$:** For any $y \in T(E)$, there exists $x \in E$ with $T(x) = y$, so $\tilde{T}(x + N) = y$. Thus $\tilde{T} : E/N \to T(E)$ is surjective.

Therefore $\tilde{T} : E/N \to T(E)$ is a linear isomorphism.
