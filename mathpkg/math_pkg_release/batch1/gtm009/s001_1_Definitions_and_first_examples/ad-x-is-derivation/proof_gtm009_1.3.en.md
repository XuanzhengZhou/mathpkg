---
role: proof
locale: en
of_concept: ad-x-is-derivation
source_book: gtm009
source_chapter: "1"
source_section: "1.3"
---

We need to verify that $\operatorname{ad} x$ satisfies the derivation property for the Lie bracket. For any $y, z \in L$:

$$\operatorname{ad} x([yz]) = [x[yz]].$$

Using the Jacobi identity (L3):
$$[x[yz]] + [y[zx]] + [z[xy]] = 0,$$
we obtain
$$[x[yz]] = -[y[zx]] - [z[xy]].$$

Now apply anticommutativity (L2') to the right-hand side:
$$-[y[zx]] = [[zx]y] = -[[xz]y],$$
$$-[z[xy]] = [[xy]z].$$

Wait, let us use the reformulation directly. Using (L2'), rewrite the Jacobi identity:

$$[x[yz]] = -[y[zx]] - [z[xy]] = [y[-zx]] + [-z[xy]] = [y[xz]] + [[xy]z].$$

But $[y[xz]] = [y[xz]]$ and $[[xy]z] = [(\operatorname{ad} x(y))z]$. And $[y[xz]] = [y, \operatorname{ad} x(z)]$. Thus:

$$\operatorname{ad} x([yz]) = [(\operatorname{ad} x(y))z] + [y(\operatorname{ad} x(z))].$$

This is precisely the derivation condition: $\delta([yz]) = [\delta(y), z] + [y, \delta(z)]$ with $\delta = \operatorname{ad} x$. Hence $\operatorname{ad} x \in \operatorname{Der} L$.
