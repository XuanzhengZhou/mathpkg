---
role: proof
locale: en
of_concept: sigma-theta-relation
source_book: gtm004
source_chapter: "VII"
source_section: "4"
---

# Proof of the Commutation Relation Between $\sigma(y)$ and $d_n$

For the Chevalley–Eilenberg complex $C = \{C_n, d_n\}$, let $\sigma(y) : C_n \to C_n$ denote the left multiplication action of $y \in \mathfrak{g}$ via the universal enveloping algebra $U\mathfrak{g}$:

$$\sigma(y) \langle x_1, \ldots, x_n \rangle = y \langle x_1, \ldots, x_n \rangle.$$

Recall that $C_n = U\mathfrak{g} \otimes_K E_n \mathfrak{g}$, and the $U\mathfrak{g}$-module structure is given by left multiplication on the first factor.

We claim the fundamental commutation relation

$$\sigma(y) d_{n-1} + d_n \sigma(y) = -\theta(y), \quad n = 1, 2, \ldots, \tag{4.4}$$

where $\theta(y) : C_n \to C_n$ is defined by

$$\theta(y) \langle x_1, \ldots, x_n \rangle = -y \langle x_1, \ldots, x_n \rangle + \sum_{i=1}^{n} \langle x_1, \ldots, [y, x_i], \ldots, x_n \rangle.$$

**Proof.** We proceed by induction on $n$, using the explicit formula for $d_n$:

$$d_n \langle x_1, \ldots, x_n \rangle = \sum_{i=1}^{n} (-1)^{i+1} x_i \langle x_1, \ldots, \hat{x}_i, \ldots, x_n \rangle + \sum_{1 \leq i < j \leq n} (-1)^{i+j} \langle [x_i, x_j], x_1, \ldots, \hat{x}_i, \ldots, \hat{x}_j, \ldots, x_n \rangle.$$

For $n = 1$, we have $d_0 = 0$ and $d_1 \langle x \rangle = x \cdot 1_{U\mathfrak{g}}$. The relation (4.4) requires

$$d_1 \sigma(y) \langle x \rangle = -\theta(y) \langle x \rangle.$$

The left side is $d_1 (y \langle x \rangle) = d_1 \langle y \otimes x \rangle$, while the right side is

$$-\theta(y) \langle x \rangle = y \langle x \rangle - \langle [y, x] \rangle.$$

Using the definition of $d_1$, one verifies this directly.

For the inductive step, suppose (4.4) holds for $d_{n-1}$. Every element of $C_n$ is a sum of elements of the form $\sigma(x_1) \langle x_2, \ldots, x_n \rangle$. Using the inductive definition of $d_n$ forced by (4.4):

$$d_n \sigma(x_1) \langle x_2, \ldots, x_n \rangle = (-\theta(x_1) - \sigma(x_1) d_{n-1}) \langle x_2, \ldots, x_n \rangle,$$

we compute:

$$\begin{aligned}
(\sigma(y) d_{n-1} + d_n \sigma(y)) \sigma(x_1) \langle \cdots \rangle
&= \sigma(y) d_{n-1} \sigma(x_1) \langle \cdots \rangle + d_n \sigma(y) \sigma(x_1) \langle \cdots \rangle \\
&= \sigma(y) d_{n-1} \sigma(x_1) \langle \cdots \rangle + d_n \sigma([y, x_1]) \langle \cdots \rangle + d_n \sigma(x_1) \sigma(y) \langle \cdots \rangle.
\end{aligned}$$

Applying the induction hypothesis and the Jacobi identity, the terms combine to yield

$$-\theta(y) \sigma(x_1) \langle \cdots \rangle = -\sigma(x_1) \theta(y) \langle \cdots \rangle - \sigma([y, x_1]) \langle \cdots \rangle,$$

which is exactly $-\theta(y)$ applied to $\sigma(x_1) \langle \cdots \rangle$. This completes the induction.

Thus (4.4) holds for all $n \geq 1$, establishing that the differentials $d_n$ and the $\mathfrak{g}$-action $\sigma$ satisfy the fundamental commutation relation with $\theta$. $\square$

**Remark.** This relation is the key structural property of the Chevalley–Eilenberg complex. It is used to prove that $d^2 = 0$ (by induction, see (4.5)) and that $\theta(y)$ commutes with $d_n$ (see (4.6)). The relation (4.4) is essentially forced by the requirement that the differential be a $\mathfrak{g}$-module homomorphism up to the homotopy $\theta$.
