---
role: proof
locale: en
of_concept: chain-cochain-conversion
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "1. Complexes"
---

# Proof of Conversion Between Chain and Cochain Complexes

**From chain to cochain.** Let $C = \{C_n, \partial_n\}_{n \in \mathbb{Z}}$ be a chain complex over $\Lambda$, so $\partial_{n-1} \partial_n = 0$ for all $n$. Define a cochain complex $D = \{D^n, \delta^n\}_{n \in \mathbb{Z}}$ by

$$
D^n = C_{-n}, \qquad \delta^n = \partial_{-n}: D^n \to D^{n+1}.
$$

We verify the cochain complex condition $\delta^{n+1} \delta^n = 0$ for all $n$:

$$
\delta^{n+1} \circ \delta^n = \partial_{-(n+1)} \circ \partial_{-n} = \partial_{-n-1} \partial_{-n} = 0,
$$

since $\partial_k \partial_{k+1} = 0$ for all $k$ (letting $k = -n-1$, we have $\partial_{-n-1} \partial_{-n} = 0$). Thus $\delta$ has degree $+1$ and satisfies $\delta \delta = 0$, so $D$ is indeed a cochain complex.

The homology of the original chain complex and the cohomology of the converted cochain complex are related by

$$
H^n(D) = \frac{\ker \delta^n}{\operatorname{im} \delta^{n-1}} = \frac{\ker \partial_{-n}}{\operatorname{im} \partial_{-n+1}} = H_{-n}(C).
$$

**From cochain to chain.** Conversely, given a cochain complex $D = \{D^n, \delta^n\}$ with $\delta^{n+1} \delta^n = 0$, define a chain complex $C = \{C_n, \partial_n\}$ by

$$
C_n = D^{-n}, \qquad \partial_n = \delta^{-n}: C_n \to C_{n-1}.
$$

Then $\partial_{n-1} \partial_n = \delta^{-n+1} \delta^{-n} = 0$, so $C$ is a chain complex. Moreover,

$$
H_n(C) = H^{-n}(D).
$$

Thus the two notions are completely equivalent via the formal reindexing $n \mapsto -n$.
