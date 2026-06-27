---
locale: en
of_concept: we-have-pxzp-0x-p-inftyxpxz-for-all-x-in-x-and-z1-and-p-0x-a
role: proof
source_book: gtm020
source_chapter: 11. Bott Periodicity in the Complex Case
source_section: '4'
---

First, there is the following relation for $z \neq w$.

$$(aw + b)^{-1} a(az + b)^{-1} = (az + b)^{-1} a(aw + b)^{-1}$$

$$= \frac{(az + b)^{-1}}{w - z} + \frac{(aw + b)^{-1}}{z - w}$$

(R)

To see this, we make the following calculation:

$$\frac{(az + b)^{-1}}{w - z} + \frac{(aw + b)^{-1}}{z - w} = (aw + b)^{-1} \frac{aw + b}{w - z}(az + b)^{-1}$$

$$+ (aw + b)^{-1} \frac{az + b}{z - w}(az + b)^{-1}$$

$$= (aw + b)^{-1} a(az + b)^{-1}$$

Now we use the symmetry between $z$ and $w$. It should be noted that the first equality in relation (R) holds also for $z = w$.

To derive the relation $p(x,z)p_0(x) = p_\infty(x)p(x

4. Analysis of Linear Clutching Maps

$$= \frac{1}{2\pi i} \int_{|w|=r_2} (aw + b)^{-1} a dw$$
$$= p_0$$

Observe that

$$\int_{|w|=r_2} \frac{dw}{w - z} = 0 \quad \text{for } |z| = r_1 > r_2$$

A similar calculation yields the relation $p_\infty p_\infty = p_\infty$. This proves the proposition.

4.3 Remark. The vector bundle projections $p_0: \zeta \rightarrow \zeta$ and $p_\infty: \zeta \rightarrow \zeta$ are of constant rank. This is a general property of projections and is easily seen by considering local cross sections $s_1, \ldots, s_n$ of $\zeta$ such that $s_1(x), \ldots, s_r(x)$ is a basis of $\ker(p_0)_x$ and $s_{r+1}(x), \ldots, s_n(x)$ is a basis of $\imath(p_0)_x$. Then $(1 - p_0)s_1(y), \ldots, (1 - p_0)s_r(y)$ is a basis of $\ker(p_0)_y$ near $x$, and $p_0s_{r+1}(y), \ldots, p_0s_n(y)$ is a basis of $\imath(p_0)_y$ for $y$ near $x$ in the base space of $\zeta$.

4.4 Notations. We denote the vector bundle $\imath p_0$ by $\zeta_+^0$, $\imath p_\infty$ by $\zeta_+^\infty$, $\ker p_0$ by $\zeta_-^0$, and $\ker p_\infty$ by $\zeta_-^\infty$. The relation $p(x,z)p_0(x) = p_\infty(x)p(x,z)$ implies that the following restrictions of $p(x,z)$ are defined:

$$p_+(-,z): \zeta_+^0 \rightarrow \zeta_+^\infty$$
$$p_-(-,z): \zeta_-

$a_+z + b_-$ to $p$. Moreover, the bundles $[\zeta,p]$ and $[\zeta_+^0,z] \oplus [\zeta_-^0,1]$ are isomorphic.

Proof. By (4.5), $p_+^t$ and $p_-^t$ are isomorphisms onto their images for all $t$, $0 \leq t \leq 1$. Then $[\zeta,p]$ and $\left(\zeta_+^0 \bigcup_{a+z} \zeta_+^0\right) \oplus \left(\zeta_-^0 \bigcup_{b} \zeta_-^0\right)$ are isomorphic bundles over $X \times S^2$. Since $a_+: \zeta_+^0 \rightarrow \zeta_+^0$ and $b_-: \zeta_-^0 \rightarrow \zeta_-^0$ are isomorphisms, there are isomorphisms between $[\zeta_+^0,z]$ and $\zeta_+^0 \bigcup_{a+z} \zeta_+^0$ and between $[\zeta_-^0,1]$ and $\zeta_-^0 \bigcup_{b} \zeta_-^0$. This proves the proposition.

4.7 Notation. Let $p$ be a polynomial clutching map for $\zeta$ of degree $\leq n$. Then the bundle $L^n(\zeta) = (n+1)\zeta$ decomposes with respect to the linear clutching map $L^n(p)$, as in (4.6). We denote this as follows:

$$L^n(\zeta) = L^n(\zeta,p)_+ \oplus L^n(\zeta,p)_-$$

Then (4.6) says that the bundles $[L^n(\zeta),L^n(p)]$ and $[L^n(\zeta,p)_+,z] \oplus [L^n(\zeta,p)_-,1]$ are isomorphic.

From the results of (3.3) and (3.4) and the above analysis, we have the following result.

4.
