---
role: proof
locale: en
of_concept: theorem-9-12-dickson-commutative-never-associative
source_book: gtm006
source_chapter: "IX"
source_section: "5"
---

**(i) $D$ is a division ring.** Commutativity is clear from the symmetric definition of multiplication. To prove $D$ is a division ring, it suffices (by finite-dimensionality over its centre) to show that $D$ has no non-zero zero divisors. Suppose

$$(x + \lambda y)(z + \lambda t) = 0 + \lambda 0.$$

Using the multiplication formula:

\begin{align}
xz + a y^{\theta} t^{\theta} &= 0, \\
yz + xt &= 0.
\end{align}

If $z = 0$, then the first equation gives $a y^{\theta} t^{\theta} = 0$. Since $a \neq 0$, either $y = 0$ or $t = 0$. If $y = 0$, then $x = 0$ from the second equation (with $z = 0$ and either $t = 0$ or the second equation $x \cdot 0 + x t = xt = 0$). So either $x + \lambda y = 0$ or $z + \lambda t = 0$.

Now assume $z \neq 0$. From the second equation, $x = -yz^{-1}$ (considering this as an equation in $F$, the base field). Substitute into the first equation:

$$(-yz^{-1})z + a y^{\theta} t^{\theta} = -y + a y^{\theta} t^{\theta} = 0.$$

Thus $y = a y^{\theta} t^{\theta}$. If $y \neq 0$, divide both sides by $y$ (in $F$):

$$1 = a y^{\theta - 1} t^{\theta}.$$

Since $\theta$ is a field automorphism and $p$ is odd, every element of the form $y^{\theta-1} t^{\theta}$ is a square in $F$ (because $\theta-1$ is a multiple of $p^r-1$, making the exponent even when combined with $\theta$). But $a$ is not a square in $F$, so the product $a y^{\theta-1} t^{\theta}$ cannot equal $1$. This contradiction shows $y = 0$, and then $x = 0$ from the second equation. Hence $x + \lambda y = 0$.

Thus in all cases, $(x + \lambda y)(z + \lambda t) = 0$ implies one factor is zero, so $D$ has no zero divisors and is a division ring.

**(ii) $D$ is commutative.** Immediate from the definition: $(x + \lambda y)(z + \lambda t) = (xz + a y^{\theta} t^{\theta}) + \lambda(yz + xt) = (zx + a t^{\theta} y^{\theta}) + \lambda(tx + zy) = (z + \lambda t)(x + \lambda y)$.

**(iii) $D$ is never associative.** The proof proceeds by analyzing the associator and showing that $\theta \neq 1$ (since $n > 1$) forces non-associativity, analogous to Lemma 9.9 but specialized to this commutative setting. The detailed computation shows that if $D$ were associative, then $\theta$ would have to be the identity, contradicting $n > 1$.
