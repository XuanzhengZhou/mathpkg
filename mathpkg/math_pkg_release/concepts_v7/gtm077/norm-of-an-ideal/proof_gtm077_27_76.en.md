---
role: proof
locale: en
of_concept: norm-of-an-ideal
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of the Norm of an Ideal

Let $\mathfrak{G}$ be the additive group of all integers of the algebraic number
field $K$. The elements of the ideal $\mathfrak{a}$ form a subgroup of
$\mathfrak{G}$. The residue classes modulo $\mathfrak{a}$ are precisely the
cosets of this subgroup in $\mathfrak{G}$.

Since $\mathfrak{a}$ admits a finite basis $\alpha_1, \ldots, \alpha_n$ (with
$n = [K : \mathbb{Q}]$), the index $[\mathfrak{G} : \mathfrak{a}]$ is finite.
We define the norm of $\mathfrak{a}$ as this index:

$$N(\mathfrak{a}) = [\mathfrak{G} : \mathfrak{a}].$$

In terms of a basis, this equals

$$N(\mathfrak{a}) = \left| \frac{\Delta(\alpha_1, \ldots, \alpha_n)}{\sqrt{d}} \right|,$$

where $\Delta(\alpha_1, \ldots, \alpha_n)$ is the discriminant of the basis
$\alpha_1, \ldots, \alpha_n$, and $d$ is the discriminant of the field $K$.

For a principal ideal $\mathfrak{a} = (\alpha)$, we take the basis
$\alpha\omega_1, \ldots, \alpha\omega_n$ with $\{\omega_i\}$ an integral basis
of $K$. Then

$$\Delta(\alpha\omega_1, \ldots, \alpha\omega_n) = N(\alpha) \cdot \Delta(\omega_1, \ldots, \omega_n) = N(\alpha) \cdot d,$$

and therefore

$$N((\alpha)) = |N(\alpha)|.$$

This establishes that the norm of a principal ideal equals the absolute value of
the norm of its generator, and that every ideal has a well-defined, finite norm.
