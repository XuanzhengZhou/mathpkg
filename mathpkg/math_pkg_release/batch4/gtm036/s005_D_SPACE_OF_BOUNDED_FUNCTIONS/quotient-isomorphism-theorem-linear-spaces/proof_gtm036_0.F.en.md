---
role: proof
locale: en
of_concept: quotient-isomorphism-theorem-linear-spaces
source_book: gtm036
source_chapter: "0"
source_section: "F"
---

Define $I : G/N \to F/M$ by $I(x + N) = \mathcal{J}(x) + M$ for each coset $x + N \in G/N$.

**Well-defined:** If $x + N = y + N$, then $x - y \in N$. Since $\mathcal{J}(N) \subseteq M$, we have $\mathcal{J}(x - y) \in M$, so $\mathcal{J}(x) - \mathcal{J}(y) \in M$, hence $\mathcal{J}(x) + M = \mathcal{J}(y) + M$. Thus $I(x + N)$ is independent of the representative chosen.

**Linearity:** For $x + N, y + N \in G/N$ and $\alpha \in K$,
$$
I((x + N) + (y + N)) = I(x + y + N) = \mathcal{J}(x + y) + M = (\mathcal{J}(x) + \mathcal{J}(y)) + M = I(x + N) + I(y + N),
$$
$$
I(\alpha(x + N)) = I(\alpha x + N) = \mathcal{J}(\alpha x) + M = \alpha \mathcal{J}(x) + M = \alpha I(x + N).
$$

**Injectivity:** Suppose $I(x + N) = M$ (the zero coset in $F/M$). Then $\mathcal{J}(x) \in M$. If we assume the condition $\mathcal{J}^{-1}(M) = N$ (which holds when the mapping is "non-degenerate" in the appropriate sense), then $x \in N$, so $x + N = N = 0_{G/N}$. Thus $I$ is injective.

**Surjectivity:** For any $z + M \in F/M$, choose a representative $w \in z + M$. If $\mathcal{J}$ maps onto a subspace complementary to $M$ (or more generally, if every coset of $M$ in $F$ is hit by $\mathcal{J}$), then there exists $y \in G$ with $\mathcal{J}(y) + M = z + M$, so $I(y + N) = z + M$.

Under the stated conditions, $I$ is an isomorphism $G/N \cong F/M$.
