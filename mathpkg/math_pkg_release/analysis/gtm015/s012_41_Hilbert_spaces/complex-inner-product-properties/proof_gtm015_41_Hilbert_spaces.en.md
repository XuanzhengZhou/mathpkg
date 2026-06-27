---
role: proof
locale: en
of_concept: complex-inner-product-properties
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Properties of the inner product in a complex pre-Hilbert space

Regard the complex pre-Hilbert space $E$ as a real pre-Hilbert space.  By Theorem 41.5, the real polarization formula

$$(x, y) = \tfrac{1}{4}\bigl\{\|x+y\|^2 - \|x-y\|^2\bigr\}$$

defines an $\mathbb{R}$-bilinear form on $E$ with $(x,x) = \|x\|^2$ and $(y,x) = (x,y)$.

The complex inner product $(x|y)$ is defined by formula (2) of (41.4), which can be rewritten as

$$(x|y) = (x, y) + i(x, iy). \tag{2'}$$

From $\mathbb{R}$-bilinearity of $(\cdot,\cdot)$, it follows immediately that $(x|y)$ is also $\mathbb{R}$-bilinear.  In particular, conditions **(iii)** and **(v)** hold.

**(i)**  $(x|x) = (x,x) + i(x,ix)$.  In the real inner product, $(x, ix) = \frac{1}{4}\{\|x+ix\|^2 - \|x-ix\|^2\} = \frac{1}{4}\{|1+i|^2\|x\|^2 - |1-i|^2\|x\|^2\} = 0$, since $|1+i| = |1-i| = \sqrt{2}$.  Hence $(x|y)$ at $y=x$ reduces to $(x,x) = \|x\|^2$, giving the required positive definiteness.

**(ii) Hermitian symmetry.**  We first note the key invariance property

$$\tag{†} (\mu x, \mu y) = (x, y) \qquad \text{for all } \mu \in \mathbb{C} \text{ with } |\mu| = 1.$$

This is immediate from formula (1) together with the absolute homogeneity $\|\mu z\| = \|z\|$ of the norm.

To prove $(y|x) = (x|y)^*$, compute

$$
\begin{aligned}
(x|y)^* &= (x,y) - i(x,iy) & \text{(from (2′))}\\
&= (y,x) - i(iy, x) & \text{(symmetry of the real inner product)}\\
&= (y,x) + i\,(y, ix). & \text{(since } (iy,x) = -(y,ix) \text{; see below)}
\end{aligned}
$$

The last expression is precisely $(y|x)$ by formula (2′).  To justify $(iy, x) = -(y, ix)$, expand both sides using definition (1):

$$
\begin{aligned}
4(iy, x) &= \|iy+x\|^2 - \|iy-x\|^2 = \|x+iy\|^2 - \|x-iy\|^2,\\
4(y, ix) &= \|y+ix\|^2 - \|y-ix\|^2 = \|i(x-iy)\|^2 - \|i(x+iy)\|^2 \\
&= \|x-iy\|^2 - \|x+iy\|^2 = -4(iy, x),
\end{aligned}
$$

where absolute homogeneity ($|i| = 1$) was used in the penultimate step.  Thus $(iy, x) = -(y, ix)$, confirming the derivation.

**(iv) Complex homogeneity.**  It suffices to prove $(\lambda x|y) = \lambda(x|y)$ for all $\lambda \in \mathbb{C}$.  By $\mathbb{R}$-bilinearity it is enough to verify the case $\lambda = i$:

$$
\begin{aligned}
(ix|y) &= (ix, y) + i(ix, iy) & \text{(by (2′))}\\
&= (ix, y) + i(x, y) & \text{(by (†) with } \mu = i\text{)}\\
&= -(x, iy) + i(x, y) & \text{(since } (ix,y) = -(x,iy)\text{)}\\[4pt]
i(x|y) &= i\bigl[(x,y) + i(x,iy)\bigr] = i(x,y) - (x,iy).
\end{aligned}
$$

The two right-hand sides agree, so $(ix|y) = i(x|y)$.  Together with $\mathbb{R}$-bilinearity this yields (iv) for all $\lambda \in \mathbb{C}$.

Conditions **(v)** and **(vi)** follow from (ii)–(iv).  $\square$
