---
role: proof
locale: en
of_concept: real-inner-product-properties
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Properties of the inner product in a real pre-Hilbert space

Recall the defining formula

$$(x, y) = \frac{1}{4}\bigl\{\|x + y\|^2 - \|x - y\|^2\bigr\}.$$

**(i)**  From the formula,
$$(x, x) = \tfrac{1}{4}\bigl\{\|2x\|^2 - \|\theta\|^2\bigr\} = \tfrac{1}{4} \cdot 4\|x\|^2 = \|x\|^2.$$
Hence $(x, x) \geq 0$, and $(x, x) = 0$ iff $\|x\| = 0$ iff $x = \theta$.

**(ii)** Symmetry is immediate because $\|x-y\| = \|y-x\|$ (the norm is absolutely homogeneous):
$$(y, x) = \tfrac{1}{4}\bigl\{\|y+x\|^2 - \|y-x\|^2\bigr\} = \tfrac{1}{4}\bigl\{\|x+y\|^2 - \|x-y\|^2\bigr\} = (x, y).$$

It remains to prove additivity in the first argument (iii) and homogeneity in the first argument (iv); the corresponding properties (v) and (vi) for the second argument then follow from symmetry.

**A key identity.**  For any $u, v, z \in E$ we assert

$$(u+v, z) + (u-v, z) = 2(u, z). \tag{*}$$

To prove $(*)$, expand using the defining formula:

$$
\begin{aligned}
4\bigl[(u+v, z) + (u-v, z)\bigr]
&= \bigl[\|u+v+z\|^2 - \|u+v-z\|^2\bigr] + \bigl[\|u-v+z\|^2 - \|u-v-z\|^2\bigr] \\[4pt]
&= \bigl[\|u+v+z\|^2 + \|u-v+z\|^2\bigr] - \bigl[\|u+v-z\|^2 + \|u-v-z\|^2\bigr].
\end{aligned}
$$

Apply the parallelogram law to each bracketed pair.  In the first bracket,
$u+v+z$ and $u-v+z$ have sum $2(u+z)$ and difference $2v$, so

$$\|u+v+z\|^2 + \|u-v+z\|^2 = 2\|u+z\|^2 + 2\|v\|^2.$$

In the second bracket, $u+v-z$ and $u-v-z$ have sum $2(u-z)$ and difference $2v$, so

$$\|u+v-z\|^2 + \|u-v-z\|^2 = 2\|u-z\|^2 + 2\|v\|^2.$$

Subtracting, the $2\|v\|^2$ terms cancel and we obtain

$$4\bigl[(u+v, z) + (u-v, z)\bigr] = 2\|u+z\|^2 - 2\|u-z\|^2 = 8(u, z),$$

which is exactly $(*)$.

**Consequence.**  Setting $u = v = \theta$ in $(*)$ gives $(\theta, z) = 0$ for all $z$.  Setting $v = u$ yields $(2u, z) = 2(u, z)$.  Setting $u = x+y$, $v = x-y$ gives

$$(2x, z) + (2y, z) = 2(x+y, z).$$

Using $(2x, z) = 2(x, z)$ and $(2y, z) = 2(y, z)$ we obtain

$$2(x, z) + 2(y, z) = 2(x+y, z),$$

hence

$$(x+y, z) = (x, z) + (y, z),$$

which is condition **(iii)**.

**(iv) Homogeneity in the first argument.**  From (iii) and $(\theta, y) = 0$ we obtain $(-x, y) = -(x, y)$; by induction,
$(nx, y) = n(x, y)$ for all $n \in \mathbb{Z}$.

If $\alpha = p/q \in \mathbb{Q}$ with $q > 0$, then

$$q\bigl(\tfrac{p}{q}x, y\bigr) = (px, y) = p(x, y),$$

so $(\alpha x, y) = \alpha(x, y)$ for all rational $\alpha$.

For an arbitrary real $\alpha$, choose a sequence of rational numbers $r_n \to \alpha$.  Using the identity $(*)$ one can show that the map $x \mapsto (x, z)$ is continuous (it is an $\mathbb{R}$-linear combination of the continuous norm function).  Hence

$$(\alpha x, y) = \lim_{n \to \infty} (r_n x, y) = \lim_{n \to \infty} r_n (x, y) = \alpha (x, y).$$

This establishes (iv).  Conditions (v) and (vi) follow from symmetry (ii) together with (iii) and (iv).  $\square$
