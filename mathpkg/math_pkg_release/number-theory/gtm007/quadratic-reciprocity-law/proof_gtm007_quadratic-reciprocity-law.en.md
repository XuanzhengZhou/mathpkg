---
role: proof
locale: en
of_concept: "$C"
source_book: gtm007
source_chapter: "I"
source_section: "3.3"
---
The proof uses Gauss sums. Let $\Omega$ be an algebraic closure of $\mathbb{F}_l$ and let $w \in \Omega$ be a primitive $p$-th root of unity. Define the Gauss sum

$$y = \sum_{x \in \mathbb{F}_p} \left(\frac{x}{p}\right) w^x \in \Omega.$$

**Lemma 1.** $y^2 = (-1)^{\varepsilon(p)} p$ in $\Omega$ (where $p$ is interpreted as the image of the integer $p$ in $\Omega$, which is nonzero since $l \neq p$).

**Lemma 2.** $-y^{p-1} = \left(\frac{p}{l}\right)$.

Since $\Omega$ has characteristic $l$, we have $y^l = \sum_{x \in \mathbb{F}_p} \left(\frac{x}{p}\right) w^{xl} = \sum_{z \in \mathbb{F}_p} \left(\frac{l^{-1}z}{p}\right) w^z = \left(\frac{l}{p}\right) y$. Hence $y^{l-1} = \left(\frac{l}{p}\right)$. By Lemma 1, $y^{p-1} = (y^2)^{(p-1)/2} = ((-1)^{\varepsilon(p)} p)^{(p-1)/2} = (-1)^{\varepsilon(p)\varepsilon(l)} \left(\frac{p}{l}\right)$. Combining with the expression from Lemma 2 gives the result. Lemma 1 is proved by evaluating the double sum:

$$y^2 = \sum_{x,z} \left(\frac{xz}{l}\right) w^{x+z} = \sum_u w^u \sum_t \left(\frac{t(u-t)}{l}\right).$$

Computing the inner sum yields $l-1$ for $u=0$ and $-1$ otherwise, giving $\sum_u C_u w^u = l$, which proves Lemma 1.
