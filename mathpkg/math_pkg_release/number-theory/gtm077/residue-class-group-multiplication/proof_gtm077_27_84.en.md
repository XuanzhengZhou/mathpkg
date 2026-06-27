---
role: proof
locale: en
of_concept: residue-class-group-multiplication
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 84

The system of residue classes modulo $\mathfrak{a}$ that are relatively prime
to $\mathfrak{a}$ forms a finite Abelian group under multiplication, of order
$\varphi(\mathfrak{a})$.

**Proof.** Define multiplication of residue classes by
$\bar{\alpha} \cdot \bar{\beta} = \overline{\alpha\beta}$.

*Well-defined:* If $\alpha \equiv \alpha' \pmod{\mathfrak{a}}$ and
$\beta \equiv \beta' \pmod{\mathfrak{a}}$, then from the distributive law,
$\alpha\beta - \alpha'\beta' = \alpha(\beta - \beta') + (\alpha - \alpha')\beta'$,
which is divisible by $\mathfrak{a}$. Moreover, if $(\alpha, \mathfrak{a}) = 1$
and $(\beta, \mathfrak{a}) = 1$, then $(\alpha\beta, \mathfrak{a}) = 1$, so
the multiplication stays within the set of classes relatively prime to
$\mathfrak{a}$.

*Group structure:* Associativity and commutativity are inherited from
multiplication in $K$. The class $\bar{1}$ serves as the identity element.
For any class $\bar{\alpha}$ with $(\alpha, \mathfrak{a}) = 1$, Theorem 78
provides a solution $\xi$ to $\alpha\xi \equiv 1 \pmod{\mathfrak{a}}$, and
$\bar{\xi}$ is the multiplicative inverse.

*Order:* By Theorem 80, there are $\varphi(\mathfrak{a})$ residue classes
relatively prime to $\mathfrak{a}$, so $|\mathfrak{R}(\mathfrak{a})| = \varphi(\mathfrak{a})$.

*Prime ideal case:* If $\mathfrak{a} = \mathfrak{p}$ is a prime ideal,
$\mathfrak{o}_K / \mathfrak{p}$ is a finite field, and its multiplicative
group is cyclic. Hence $\mathfrak{R}(\mathfrak{p})$ is cyclic.
