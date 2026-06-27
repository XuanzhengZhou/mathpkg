---
role: proof
locale: en
of_concept: additive-residue-group
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 83: Additive Group of Residue Classes modulo an Ideal

The $N(\mathfrak{a})$ residue classes modulo $\mathfrak{a}$ form an Abelian
group under addition, denoted $\mathfrak{G}(\mathfrak{a})$, of order
$N(\mathfrak{a})$.

**Proof.** Define the composition of two residue classes
$\bar{\alpha}, \bar{\beta}$ (represented by integers $\alpha, \beta$ of $K$)
as the residue class of $\alpha + \beta$. This is well-defined: if
$\alpha \equiv \alpha' \pmod{\mathfrak{a}}$ and
$\beta \equiv \beta' \pmod{\mathfrak{a}}$, then
$\mathfrak{a} \mid (\alpha - \alpha')$ and
$\mathfrak{a} \mid (\beta - \beta')$, so
$\mathfrak{a} \mid (\alpha + \beta) - (\alpha' + \beta')$; hence
$\alpha + \beta \equiv \alpha' + \beta' \pmod{\mathfrak{a}}$.

The group axioms follow immediately from the additive structure of the ring of
integers:
- **Associativity:** $\bar{\alpha} + (\bar{\beta} + \bar{\gamma}) =
  (\bar{\alpha} + \bar{\beta}) + \bar{\gamma}$, inherited from addition in $K$.
- **Identity:** $\bar{0}$, the residue class of $0$, satisfies
  $\bar{0} + \bar{\alpha} = \bar{\alpha}$ for all $\bar{\alpha}$.
- **Inverse:** For each $\bar{\alpha}$, the class $\overline{-\alpha}$ satisfies
  $\bar{\alpha} + \overline{-\alpha} = \bar{0}$.
- **Commutativity:** $\bar{\alpha} + \bar{\beta} = \bar{\beta} + \bar{\alpha}$.

The order of this group is $N(\mathfrak{a})$, the number of residue classes, as
established in Theorem 76. By Theorem 19 of group theory (in a finite group of
order $h$, every element raised to the $h$-th power equals the identity), we
have for all $\alpha$

$$\alpha \cdot N(\mathfrak{a}) \equiv 0 \pmod{\mathfrak{a}}.$$

In particular, for $\alpha = 1$,
$N(\mathfrak{a}) \equiv 0 \pmod{\mathfrak{a}}$, which means
$\mathfrak{a} \mid N(\mathfrak{a})$.

For a prime ideal $\mathfrak{p}$ of degree $1$, $N(\mathfrak{p}) = p$ is a
rational prime, and the additive group $\mathfrak{G}(\mathfrak{p})$ is cyclic
of prime order.
