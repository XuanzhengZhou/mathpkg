---
role: proof
locale: en
of_concept: fermat-generalization-for-ideals
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of the Generalization of Fermat's Theorem to Ideals

**Theorem.** For a prime ideal $\mathfrak{p}$ and every integer $\alpha$ of the
field $K$,

$$\alpha^{N(\mathfrak{p})} \equiv \alpha \pmod{\mathfrak{p}}.$$

If $\alpha$ is not divisible by $\mathfrak{p}$ (i.e. $(\alpha, \mathfrak{p}) = 1$),
then

$$\alpha^{N(\mathfrak{p}) - 1} \equiv 1 \pmod{\mathfrak{p}}.$$

**Proof.** The residue class ring $\mathfrak{o}_K / \mathfrak{p}$ is a finite
field with $N(\mathfrak{p})$ elements. Its multiplicative group
$\mathfrak{R}(\mathfrak{p})$ has order $N(\mathfrak{p}) - 1$, consisting of all
non-zero residue classes.

If $\alpha$ is not divisible by $\mathfrak{p}$, then its residue class
$\bar{\alpha}$ belongs to $\mathfrak{R}(\mathfrak{p})$. By Lagrange's Theorem
(applied to the finite group $\mathfrak{R}(\mathfrak{p})$), the order of any
element divides the group order, so

$$\bar{\alpha}^{N(\mathfrak{p}) - 1} = \bar{1} \quad \text{in } \mathfrak{R}(\mathfrak{p}).$$

In terms of congruences, this means

$$\alpha^{N(\mathfrak{p}) - 1} \equiv 1 \pmod{\mathfrak{p}}.$$

Multiplying both sides by $\alpha$ yields

$$\alpha^{N(\mathfrak{p})} \equiv \alpha \pmod{\mathfrak{p}},$$

which also holds trivially when $\mathfrak{p} \mid \alpha$, since then both
sides are $\equiv 0 \pmod{\mathfrak{p}}$. This completes the proof.
