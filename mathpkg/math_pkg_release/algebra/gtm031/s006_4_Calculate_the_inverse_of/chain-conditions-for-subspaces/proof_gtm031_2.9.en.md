---
role: proof
locale: en
of_concept: chain-conditions-for-subspaces
source_book: gtm031
source_chapter: "II: Finite Dimensional Vector Spaces"
source_section: "9: Factor Spaces"
---

Both chain conditions follow immediately from the fact that the dimension of a subspace is a non-negative integer and that proper inclusion forces a strict change in dimension.

For the descending chain condition: suppose $\mathfrak{S}_1 \supseteq \mathfrak{S}_2 \supseteq \cdots$ is an infinite descending chain of subspaces. Then for each $i$, either $\mathfrak{S}_i = \mathfrak{S}_{i+1}$ or $\mathfrak{S}_i \supset \mathfrak{S}_{i+1}$. If $\mathfrak{S}_i \supset \mathfrak{S}_{i+1}$, then $\dim \mathfrak{S}_i > \dim \mathfrak{S}_{i+1}$ (since a proper subspace has strictly smaller dimension than the containing space in the finite-dimensional case). Because the dimensions are non-negative integers, there can be at most $\dim \mathfrak{S}_1 + 1$ strict inclusions before the dimension reaches $0$. Hence there exists an integer $r$ after which all inclusions are equalities: $\mathfrak{S}_r = \mathfrak{S}_{r+1} = \cdots$.

For the ascending chain condition: suppose $\mathfrak{S}_1 \subseteq \mathfrak{S}_2 \subseteq \cdots$ is an infinite ascending chain. If $\mathfrak{S}_i \subset \mathfrak{S}_{i+1}$, then $\dim \mathfrak{S}_i < \dim \mathfrak{S}_{i+1}$. Since $\dim \mathfrak{S}_i \leq \dim \mathfrak{R} = n$ for all $i$, there can be at most $n$ strict inclusions. Hence the chain stabilizes at some finite $r$: $\mathfrak{S}_r = \mathfrak{S}_{r+1} = \cdots$.
