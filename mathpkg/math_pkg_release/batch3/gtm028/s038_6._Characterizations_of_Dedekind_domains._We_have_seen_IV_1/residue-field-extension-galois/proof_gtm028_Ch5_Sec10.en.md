---
role: proof
locale: en
of_concept: residue-field-extension-galois
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

Since $L$ is normal over $K$, for any $x \in R'$, its minimal polynomial $X^q + a_{q-1}X^{q-1} + \cdots + a_0$ over $K$ has coefficients in $R$ (since $R$ is integrally closed and $x$ is integral) and factors into linear factors in $R'$: $\prod_i (X - x_i)$ with $x = x_1$ (II, Section 6). Reducing modulo $\mathfrak{P}$, the polynomial $\prod_i (X - \bar{x}_i)$ has coefficients in $R/\mathfrak{p}$ and all its roots in $R'/\mathfrak{P}$. Thus the minimal polynomial of $\bar{x}$ over $R/\mathfrak{p}$ splits completely in $R'/\mathfrak{P}$, proving that $R'/\mathfrak{P}$ is normal over $R/\mathfrak{p}$.

To prove that $G_Z/G_T$ is the Galois group, it suffices to show it is the Galois group of the maximal separable extension $S$ of $R/\mathfrak{p}$ in $R'/\mathfrak{P}$. Taking a primitive element $\bar{x}$ of $S$ over $R/\mathfrak{p}$ (II, Section 9, Theorem 19), every automorphism $s'$ of $S$ is determined by the image of $\bar{x}$. By applying the preceding reasoning to $K_Z, R_Z, \mathfrak{P}_Z$ instead of $K, R, \mathfrak{p}$ (so that $G_Z$ replaces $G$), we see that the conjugates of $\bar{x}$ are exactly the residue classes of the $G_Z$-conjugates of a lift $x$, and the action of $G_Z$ on these conjugates factors through $G_Z/G_T$, giving the desired isomorphism.

The final statement about the separable case is an immediate corollary.
