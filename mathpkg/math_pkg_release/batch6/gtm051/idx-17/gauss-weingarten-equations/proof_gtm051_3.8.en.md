---
role: proof
locale: en
of_concept: gauss-weingarten-equations
source_book: gtm051
source_chapter: "3"
source_section: "3.8"
---

**Proof of Theorem 3.8.1 (Gauss-Weingarten Equations).**

Write the second partial derivatives $f_{ik}$ in the basis $\{f_1, f_2, n\}$ of $\mathbb{R}^3$:

$$
f_{ik} = \sum_l a_{ik}^l f_l + b_{ik} n.
$$

Taking the inner product with $n$ and using $f_l \cdot n = 0$, $n \cdot n = 1$, we obtain

$$
f_{ik} \cdot n = b_{ik}.
$$

But by definition of the second fundamental form, $h_{ik} = f_{ik} \cdot n$, hence $b_{ik} = h_{ik}$. This gives the normal component.

Now take the inner product with $f_j$:

$$
f_{ik} \cdot f_j = \sum_l a_{ik}^l (f_l \cdot f_j) = \sum_l a_{ik}^l g_{lj}.
$$

Multiplying by $g^{jm}$ and summing over $j$ yields

$$
a_{ik}^m = \sum_j g^{mj} (f_{ik} \cdot f_j) =: \Gamma_{ik}^m.
$$

Thus $f_{ik} = \sum_l \Gamma_{ik}^l f_l + h_{ik} n$, which is the first equation (the Gauss formula).

To obtain the explicit formula for $\Gamma_{ik}^l$ in terms of $g_{ij}$ and its derivatives, differentiate $g_{ij} = f_i \cdot f_j$:

$$
g_{ij,k} = (f_i \cdot f_j)_k = f_{ik} \cdot f_j + f_i \cdot f_{jk}.
$$

Substituting the expressions for $f_{ik}$ and $f_{jk}$:

$$
g_{ij,k} = \sum_l \Gamma_{ik}^l g_{lj} + \sum_l \Gamma_{jk}^l g_{li}. \tag{α}
$$

Cyclically permuting the indices yields:

$$
g_{ki,j} = \sum_l \Gamma_{kj}^l g_{li} + \sum_l \Gamma_{ij}^l g_{lk}, \tag{β}
$$

$$
g_{jk,i} = \sum_l \Gamma_{ji}^l g_{lk} + \sum_l \Gamma_{ki}^l g_{lj}. \tag{γ}
$$

Forming (α) − (β) + (γ) and using the symmetry $\Gamma_{ij}^l = \Gamma_{ji}^l$, we obtain

$$
\Gamma_{ik}^l = \frac{1}{2} \sum_j g^{lj} (g_{ij,k} + g_{jk,i} - g_{ki,j}),
$$

which is the expression $(**)$ and gives the Christoffel symbols purely in terms of the first fundamental form.

For the second equation (the Weingarten formula), the expression for $n_i = n_{u^i}$ follows from equation (3.5.5), which gives $n_i = -\sum_{l,k} h_{il} g^{lk} f_k$.
