---
role: proof
locale: en
of_concept: theorem-76
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 76: Number of Residue Classes modulo an Ideal

**Theorem 76.** The number of residue classes modulo an ideal $\mathfrak{a} 
eq 0$ is finite. Denoting this number by $N(\mathfrak{a})$, if $lpha_1, \ldots, lpha_n$ is a basis for $\mathfrak{a}$, then

$$N(\mathfrak{a}) = \left| rac{\Delta(lpha_1, \ldots, lpha_n)}{\sqrt{d}} ight|,$$

where $d$ is the discriminant of the field. For a principal ideal $\mathfrak{a} = (lpha)$, we have $N(\mathfrak{a}) = |N(lpha)|$.

*Proof.* The integers of $\mathfrak{a}$ form a subgroup of the additive group $\mathfrak{G}$ of all integers of the field $K$. The different cosets of $\mathfrak{a}$ in $\mathfrak{G}$ correspond precisely to the distinct residue classes modulo $\mathfrak{a}$. Hence the number $N(\mathfrak{a})$ of residue classes is the index $[\mathfrak{G} : \mathfrak{a}]$.

If $\omega_1, \ldots, \omega_n$ is an integral basis of $K$ (so that every integer of $K$ is uniquely representable as $\sum x_i \omega_i$ with $x_i \in \mathbb{Z}$) and $lpha_1, \ldots, lpha_n$ is a basis for the ideal $\mathfrak{a}$, then the transition matrix between these two bases has determinant whose absolute value equals the index $[\mathfrak{G} : \mathfrak{a}]$. By the theory of modules, this index is given by

$$N(\mathfrak{a}) = [\mathfrak{G} : \mathfrak{a}] = \left| rac{\Delta(lpha_1, \ldots, lpha_n)}{\sqrt{d}} ight|,$$

where $\Delta(lpha_1, \ldots, lpha_n)$ denotes the discriminant of the basis elements and $d = \Delta(\omega_1, \ldots, \omega_n)$ is the field discriminant.

For a principal ideal $\mathfrak{a} = (lpha)$, a basis is given by $lpha \omega_1, \ldots, lpha \omega_n$. Their discriminant is

$$\Delta(lpha \omega_1, \ldots, lpha \omega_n) = N(lpha)^2 