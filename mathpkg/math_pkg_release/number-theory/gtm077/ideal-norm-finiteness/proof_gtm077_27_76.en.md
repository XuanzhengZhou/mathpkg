---
role: proof
locale: en
of_concept: ideal-norm-finiteness
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 76: Finiteness of the Residue Class Number (Ideal Norm)

Let $\mathfrak{G}$ be the additive group of all integers of the field $K$. The
numbers of $\mathfrak{a}$ form a subgroup of $\mathfrak{G}$ (since $\mathfrak{a}$
is an ideal). The distinct residue classes modulo $\mathfrak{a}$ are precisely
the distinct cosets of $\mathfrak{a}$ in $\mathfrak{G}$.

Since $\mathfrak{a}$ has a finite basis $\alpha_1, \ldots, \alpha_n$ (where
$n = [K : \mathbb{Q}]$), the index $[\mathfrak{G} : \mathfrak{a}]$ is finite
and equals the absolute value of the determinant of the basis of $\mathfrak{a}$
divided by $\sqrt{d}$, where $d$ is the field discriminant:

$$N(\mathfrak{a}) = \left| \frac{\Delta(\alpha_1, \ldots, \alpha_n)}{\sqrt{d}} \right|.$$

For a principal ideal $\mathfrak{a} = (\alpha)$, we obtain a basis of the form
$\alpha\omega_1, \ldots, \alpha\omega_n$, where $\omega_1, \ldots, \omega_n$ is
an integral basis of $K$. Then

$$\Delta(\alpha\omega_1, \ldots, \alpha\omega_n) = N(\alpha) \cdot \Delta(\omega_1, \ldots, \omega_n) = N(\alpha) \cdot d,$$

and consequently

$$N((\alpha)) = \left| \frac{N(\alpha) \cdot d}{\sqrt{d}} \right| = |N(\alpha)|.$$

Thus the number of residue classes modulo $\mathfrak{a}$ is finite, and we denote
this invariant by $N(\mathfrak{a})$ -- the norm of the ideal $\mathfrak{a}$.
