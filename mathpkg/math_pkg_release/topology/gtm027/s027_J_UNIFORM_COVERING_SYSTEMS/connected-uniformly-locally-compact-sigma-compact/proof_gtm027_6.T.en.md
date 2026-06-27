---
role: proof
locale: en
of_concept: connected-uniformly-locally-compact-sigma-compact
source_book: gtm027
source_chapter: "6"
source_section: "T"
---

# Proof: Connected Uniformly Locally Compact Spaces Are $\sigma$-Compact

Let $(X, \mathfrak{U})$ be a connected uniformly locally compact space. There exists $U \in \mathfrak{U}$ such that $U[x]$ is compact for each $x \in X$.

Fix $x_0 \in X$ and define $K_0 = \overline{U[x_0]}$, which is compact. Inductively define

$$K_{n+1} = U[K_n].$$

By part (b), since each $K_n$ is compact and $U \circ U[x]$ is compact for each $x$ (by local compactness), each $K_n$ is compact.

Now $\bigcup_{n \in \omega} K_n$ is a $\sigma$-compact set. By part (a), $\bigcup_n U^n[x_0]$ is both open and closed. Since $X$ is connected, this clopen set must be all of $X$. Thus $X = \bigcup_n K_n$ is $\sigma$-compact.

This is the chain argument of 5.T applied to the uniformly locally compact setting.
