---
role: proof
locale: en
of_concept: one-form-dz-dzbar-representation
source_book: gtm035
source_chapter: "Chapter 5"
source_section: "5.1"
---
# Proof of Representation of 1-Forms with $dz$ and $d\bar{z}$

We work on an open set $\Omega \subseteq \mathbb{C}^n$. Recall that $x_j = \operatorname{Re}(z_j)$ and $y_j = \operatorname{Im}(z_j)$ give real coordinates on $\mathbb{C}^n \cong \mathbb{R}^{2n}$, so that $(dx_1)_x, \ldots, (dx_n)_x, (dy_1)_x, \ldots, (dy_n)_x$ form a basis for $T_x^*$ at each $x \in \Omega$.

Every 1-form $\omega \in \wedge^1(\Omega)$ admits a unique representation with respect to this basis:

$$\omega = \sum_{j=1}^{n} \big( C_j \, dx_j + D_j \, dy_j \big),$$

where $C_j, D_j$ are scalar functions on $\Omega$. (This is Lemma 4.2 applied to $\mathbb{R}^{2n}$.)

Now use the relations between the real and complex bases:

$$dx_j = \frac{1}{2}(dz_j + d\bar{z}_j), \qquad dy_j = \frac{1}{2i}(dz_j - d\bar{z}_j).$$

Substituting these into the representation of $\omega$ yields

$$\omega = \sum_{j=1}^{n} \left[ C_j \cdot \frac{1}{2}(dz_j + d\bar{z}_j) + D_j \cdot \frac{1}{2i}(dz_j - d\bar{z}_j) \right].$$

Collecting the coefficients of $dz_j$ and $d\bar{z}_j$:

$$\omega = \sum_{j=1}^{n} \left[ \left( \frac{C_j}{2} + \frac{D_j}{2i} \right) dz_j + \left( \frac{C_j}{2} - \frac{D_j}{2i} \right) d\bar{z}_j \right].$$

Define

$$a_j = \frac{C_j}{2} + \frac{D_j}{2i}, \qquad b_j = \frac{C_j}{2} - \frac{D_j}{2i}.$$

Since $C_j, D_j \in C^\infty(\Omega)$, we have $a_j, b_j \in C^\infty(\Omega)$ as well. Then

$$\omega = \sum_{j=1}^{n} \big( a_j \, dz_j + b_j \, d\bar{z}_j \big),$$

which is the desired representation. Uniqueness follows from the fact that $\{dz_j, d\bar{z}_j\}_{j=1}^n$ forms a basis for $T_x^*$, as established by observing that the transformation from $\{dx_j, dy_j\}$ to $\{dz_j, d\bar{z}_j\}$ is invertible (the matrix has determinant $(-i/2)^n \neq 0$).
