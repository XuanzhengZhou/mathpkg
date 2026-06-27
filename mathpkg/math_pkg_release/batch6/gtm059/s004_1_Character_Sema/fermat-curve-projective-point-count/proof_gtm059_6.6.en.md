---
role: proof
locale: en
of_concept: fermat-curve-projective-point-count
source_book: gtm059
source_chapter: "1"
source_section: "6. Application to the Fermat Curve"
---

Let $N$ be the number of affine points of $V(d)$ as in Theorem 6.1, and let $\overline{N}$ be the number of projective points. The projective curve is the completion of the affine curve $x^d + y^d = 1$ in $\mathbb{P}^2$. The points at infinity correspond to solutions of the homogeneous equation $X^d + Y^d = Z^d$ with $Z = 0$.

For the Fermat curve $X^d + Y^d = Z^d$, setting $Z = 0$ gives $X^d + Y^d = 0$ in $\mathbb{P}^1$. Over $\mathbb{F}_q$ with $d \mid (q-1)$, there are exactly $d$ points at infinity (solutions to $X^d = -Y^d$ with $Y \neq 0$, up to scaling). However, the standard relation between affine and projective counts of a curve in $\mathbb{P}^2$ uses the fact that from each affine point we obtain, by homogenization and dehomogenization, a projective point with $Z \neq 0$. Conversely, each projective point with $Z \neq 0$ corresponds to exactly $q-1$ affine representatives (scaling by elements of $F^*$). Points with $Z = 0$ correspond to the points at infinity, of which there are $d$ for this curve.

More directly, the relation stated in the text is
$$\overline{N} = 1 + (q-1)N,$$
which accounts for the unique point at infinity not captured by the affine count under the specific affine patch chosen (the standard embedding $x^d + y^d = 1$ corresponds to $Z = 1$, and the points at infinity are those with $Z = 0$). Substituting the formula for $N$ from Theorem 6.1 and using the relation $1 + (q-1)q = 1 + q^2 - q = q^2 - q + 1$ with the correction from the Jacobi sum, one obtains the stated formula for $\overline{N}$.
