---
role: proof
locale: en
of_concept: composition-formula-internal-category-grp
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

Write the composition of a composable pair $a \xrightarrow{f} b \xrightarrow{g} c$ as $g \circ f$. Since composition is a morphism of the group product, one has the middle four exchange:

$$(g_1 g_2) \circ (f_1 f_2) = (g_1 \circ f_1)(g_2 \circ f_2)$$

whenever both composites on the right are defined. Applying this to the identity arrow $1_b$ of $b$:

$$g \circ f = (1_b 1_b^{-1} g) \circ (f 1_b^{-1} 1_b)$$
$$= (1_b \circ f)(1_b^{-1} \circ 1_b^{-1})(g \circ 1_b)$$
$$= f(1_b^{-1} \circ 1_b^{-1}) g.$$

Setting $f = g = 1_b$ gives

$$1_b = 1_b(1_b^{-1} \circ 1_b^{-1}) 1_b,$$

hence $(1_b^{-1} \circ 1_b^{-1}) = 1_b^{-1}$. (This also follows from the fact that $(\cdot)^{-1}: C \to C$ is a functor where $C$ is a group object.)

Substituting this back gives

$$g \circ f = f 1_b^{-1} g.$$

Alternatively, one may compute

$$g \circ f = (g 1_b^{-1} 1_b) \circ (1_b 1_b^{-1} f)$$
$$= (g \circ 1_b)(1_b^{-1} \circ 1_b^{-1})(1_b \circ f)$$
$$= g 1_b^{-1} f.$$

Hence the group product satisfies $f 1_b^{-1} g = g 1_b^{-1} f$. In particular, if the object $b$ of $C_0$ is the unit element in the group $C_0$, then $1_b = i(b)$ is the unit element in $C_1$, and $fg = gf$. Since $g$ with domain $b$ (the unit of $C_0$) must lie in $\ker d_0$, and $f$ similarly lies in $\ker d_1$, the equality $fg = gf$ means the commutator $[\ker d_0, \ker d_1]$ must be the identity.
