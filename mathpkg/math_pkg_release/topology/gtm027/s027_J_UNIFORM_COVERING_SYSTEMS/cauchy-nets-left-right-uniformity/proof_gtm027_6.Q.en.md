---
role: proof
locale: en
of_concept: cauchy-nets-left-right-uniformity
source_book: gtm027
source_chapter: "6"
source_section: "Q"
---

# Proof: Cauchy Nets Under Left and Right Uniformities

Let $(G, \mathcal{J})$ be a topological group with left uniformity $\mathcal{L}$ and right uniformity $\mathcal{R}$.

Let $\{x_n, n \in D\}$ be a Cauchy net relative to $\mathcal{L}$. This means that for each neighborhood $U$ of the identity, there exists $n_0 \in D$ such that for all $m, n \geq n_0$, we have $x_m^{-1}x_n \in U$.

We need to show that $\{x_n^{-1}, n \in D\}$ is Cauchy relative to $\mathcal{L}$ (equivalently, $\mathcal{L}$ and $\mathcal{R}$ have the same Cauchy nets).

For $\mathcal{L}$-Cauchy condition on $\{x_n^{-1}\}$: we need $(x_m^{-1})^{-1}(x_n^{-1}) = x_m x_n^{-1} \in U$ for large $m, n$. But $x_m x_n^{-1}$ is the $\mathcal{R}$-condition. To relate it to the $\mathcal{L}$-condition, note that

$$x_m x_n^{-1} = x_m (x_m^{-1}x_n)^{-1} x_m^{-1}$$

using the fact that inversion is continuous. More directly, the continuity of the inverse map ensures that if $x_m^{-1}x_n \to e$ (in the $\mathcal{L}$ sense), then $x_n^{-1}x_m \to e$ also. Then $x_m x_n^{-1} = (x_n x_m^{-1})^{-1} \to e$.

Thus $\mathcal{L}$ and $\mathcal{R}$ have the same Cauchy nets. Left translation is $\mathcal{R}$-uniformly continuous, right translation is $\mathcal{L}$-uniformly continuous, and inversion is $\mathcal{U}$-uniformly continuous. However, multiplication is usually *not* uniformly continuous relative to the product uniformity $\mathcal{L} \times \mathcal{L}$ or $\mathcal{R} \times \mathcal{R}$.
