---
role: proof
locale: en
of_concept: biinvariant-metric-biuniform
source_book: gtm015
source_chapter: "10"
source_section: "Bi-uniform topological groups"
---

# Proof of Bi-invariant metric implies bi-uniform

Let $G$ be a group equipped with a bi-invariant metric $d$, meaning $d(ax, ay) = d(x, y) = d(xa, ya)$ for all $a, x, y \in G$. Equip $G$ with the topology derived from $d$.

We first verify that $G$ is a topological group. Since $d$ is bi-invariant, the left and right translations are isometries, hence homeomorphisms. Moreover,

$$d(x^{-1}, y^{-1}) = d(x^{-1}x, y^{-1}x) = d(e, y^{-1}x) = d(ye, yy^{-1}x) = d(y, x) = d(x, y),$$

so inversion is an isometry (hence continuous). For multiplication, if $d(x_n, x) \to 0$ and $d(y_n, y) \to 0$, then

$$d(x_n y_n, xy) \leq d(x_n y_n, x_n y) + d(x_n y, xy) = d(y_n, y) + d(x_n, x) \to 0$$

using right-invariance for the first term and left-invariance for the second. Thus $(x, y) \mapsto xy$ is continuous.

Now let $\mathcal{U}_s$ and $\mathcal{U}_r$ be the left and right uniformities of the topological group $G$. By (7.6), $\mathcal{U}_s = \mathcal{U}_d$, where $\mathcal{U}_d$ is the uniformity derived from $d$. Dually (replacing "left" by "right"), $\mathcal{U}_r = \mathcal{U}_d$. Therefore $\mathcal{U}_s = \mathcal{U}_r$, and $G$ is bi-uniform.
