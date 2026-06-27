---
role: proof
locale: en
of_concept: composition-formula-for-internal-category-in-grp
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

Let an internal category in Grp be given with groups $C_0$ and $C_1$ and structure homomorphisms $d_0, d_1, i, \gamma$. For composable morphisms $a \xrightarrow{f} b \xrightarrow{g} c$, the composition is denoted $g \circ f = \gamma(g, f)$.

Since $\gamma$ is a group homomorphism when written multiplicatively (with the group product in $C_1$ denoted by juxtaposition), we have the interchange law: for composable pairs $(f_1, g_1)$ and $(f_2, g_2)$,

$$(g_1 g_2) \circ (f_1 f_2) = (g_1 \circ f_1)(g_2 \circ f_2)$$

whenever both composites on the right are defined. This is the middle four exchange property.

Apply this to the identity arrow $1_b$ of $b$. Write $1_b^{-1}$ for its group inverse in $C_1$. Then

$$g \circ f = (1_b 1_b^{-1} g) \circ (f 1_b^{-1} 1_b).$$

Using the interchange law:

$$= (1_b \circ f)(1_b^{-1} \circ 1_b^{-1})(g \circ 1_b).$$

Since $1_b$ is the identity at $b$, we have $1_b \circ f = f$ and $g \circ 1_b = g$. Thus

$$g \circ f = f (1_b^{-1} \circ 1_b^{-1}) g.$$

Setting $f = g = 1_b$ yields

$$1_b = 1_b (1_b^{-1} \circ 1_b^{-1}) 1_b,$$

hence $1_b^{-1} \circ 1_b^{-1} = 1_b^{-1}$. (This also follows from the fact that the inversion map $(\cdot)^{-1} : C \to C$ is a functor when $C$ is a group object.)

Substituting back gives the first formula:

$$g \circ f = f 1_b^{-1} g.$$

Alternatively, one may factor as

$$g \circ f = (g 1_b^{-1} 1_b) \circ (1_b 1_b^{-1} f) = (g \circ 1_b)(1_b^{-1} \circ 1_b^{-1})(1_b \circ f) = g 1_b^{-1} f.$$

Thus both expressions are valid, and equating them yields

$$f 1_b^{-1} g = g 1_b^{-1} f.$$

In the special case where $b$ is the unit element of the group $C_0$, the identity $1_b = i(b)$ is the unit element of $C_1$, so the formula reduces to $f g = g f$ for all $f$ with $d_0(f) = b$ (i.e., $f \in \ker d_0$) and all $g$ with $d_1(g) = b$ (i.e., $g \in \ker d_1$). This is precisely the commutator condition $[\ker d_0, \ker d_1] = 1$.

Conversely, given a diagram $d_0, d_1 : C_1 \rightrightarrows C_0$ with $i : C_0 \to C_1$ satisfying $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$, one can define a categorical composition $\gamma : C_1 \times_{C_0} C_1 \to C_1$ by setting $\gamma(g, f) = f 1_b^{-1} g$ (or equivalently $g 1_b^{-1} f$). A straightforward calculation verifies that this $\gamma$ satisfies the axioms for an internal category in Grp.
