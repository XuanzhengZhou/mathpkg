---
role: proof
locale: en
of_concept: multiplicative-residue-group
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 84: Multiplicative Group of Residue Classes modulo an Ideal

The residue classes modulo $\mathfrak{a}$ that are relatively prime to
$\mathfrak{a}$ form a finite Abelian group under multiplication, denoted
$\mathfrak{R}(\mathfrak{a})$, of order $\varphi(\mathfrak{a})$. For a prime
ideal $\mathfrak{p}$, $\mathfrak{R}(\mathfrak{p})$ is cyclic.

**Proof.** Let $\bar{\alpha}$ denote the residue class of an integer $\alpha$
modulo $\mathfrak{a}$. We consider only those classes for which
$(\alpha, \mathfrak{a}) = 1$.

*Well-definedness of multiplication.* If
$\alpha \equiv \alpha' \pmod{\mathfrak{a}}$ and
$\beta \equiv \beta' \pmod{\mathfrak{a}}$, then
$\mathfrak{a} \mid \alpha - \alpha'$ and
$\mathfrak{a} \mid \beta - \beta'$. Hence
$\alpha\beta - \alpha'\beta' = \alpha(\beta - \beta') + (\alpha - \alpha')\beta'$
is divisible by $\mathfrak{a}$. Moreover, if $(\alpha, \mathfrak{a}) = 1$ and
$(\beta, \mathfrak{a}) = 1$, then $(\alpha\beta, \mathfrak{a}) = 1$, so the
product class is also in the set.

*Group axioms:*
- **Associativity:** Inherited from multiplication in $K$.
- **Identity:** $\bar{1}$, the class of $1$, satisfies
  $\bar{1} \cdot \bar{\alpha} = \bar{\alpha}$.
- **Inverse:** For $\bar{\alpha}$ with $(\alpha, \mathfrak{a}) = 1$, Theorem 78
  with $\beta = 1$ guarantees the existence of $\xi$ such that
  $\alpha\xi \equiv 1 \pmod{\mathfrak{a}}$. Then $\bar{\xi} = \bar{\alpha}^{-1}$.
  Also $(\xi, \mathfrak{a}) = 1$, so the inverse lies in the set.
- **Commutativity:** $\bar{\alpha} \cdot \bar{\beta} = \bar{\beta} \cdot \bar{\alpha}$.

*Order.* By Theorem 80, the number of residue classes relatively prime to
$\mathfrak{a}$ is $\varphi(\mathfrak{a})$, so $|\mathfrak{R}(\mathfrak{a})| = \varphi(\mathfrak{a})$.

*Cyclicity for prime ideals.* For a prime ideal $\mathfrak{p}$, the residue
class ring $\mathfrak{o}_K / \mathfrak{p}$ is a finite field. The
multiplicative group of a finite field is always cyclic, so
$\mathfrak{R}(\mathfrak{p})$ is cyclic. A generator of this group is called a
primitive root modulo $\mathfrak{p}$.
