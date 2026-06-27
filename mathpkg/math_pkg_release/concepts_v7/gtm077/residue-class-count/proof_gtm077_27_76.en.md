---
role: proof
locale: en
of_concept: residue-class-count
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 76

Let $\mathfrak{G}$ be the additive group of all integers of the field $K$. The
numbers of $\mathfrak{a}$ form a subgroup of $\mathfrak{G}$ (since $\mathfrak{a}$
is an ideal, it is closed under addition and subtraction). The distinct residue
classes modulo $\mathfrak{a}$ are precisely the distinct cosets of $\mathfrak{a}$
in $\mathfrak{G}$.

Since $\mathfrak{a}$ has a finite basis $\alpha_1, \ldots, \alpha_n$ (where
$n = [K : \mathbb{Q}]$ is the degree of the field), the index
$[\mathfrak{G} : \mathfrak{a}]$ is finite. Specifically, the number of residue
classes is

$$N(\mathfrak{a}) = \left| \frac{\Delta(\alpha_1, \ldots, \alpha_n)}{\sqrt{d}} \right|,$$

where $\Delta(\alpha_1, \ldots, \alpha_n)$ is the discriminant of the basis and
$d$ is the field discriminant.

For a principal ideal $\mathfrak{a} = (\alpha)$, a basis is given by
$\alpha\omega_1, \ldots, \alpha\omega_n$, where $\omega_1, \ldots, \omega_n$ is
an integral basis. Then

$$\Delta(\alpha\omega_1, \ldots, \alpha\omega_n) = N(\alpha) \cdot \Delta(\omega_1, \ldots, \omega_n),$$

and

$$N((\alpha)) = \left| \frac{N(\alpha) \cdot \Delta(\omega_1, \ldots, \omega_n)}{\sqrt{d}} \right| = |N(\alpha)|.$$

Hence the residue class count $N(\mathfrak{a})$ is always a finite positive integer.
