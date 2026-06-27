---
role: proof
locale: en
of_concept: liouville-numbers-residual
source_book: gtm002
source_chapter: "2"
source_section: "2. Liouville Numbers"
---

Let $E$ denote the set of Liouville numbers and $Q$ the set of rational numbers. From the definition of a Liouville number, we have

$$E = Q' \cap \bigcap_{n=1}^{\infty} G_n, \tag{5}$$

where

$$G_n = \bigcup_{q=2}^{\infty} \bigcup_{p=-\infty}^{\infty} \left( \frac{p}{q} - \frac{1}{q^n}, \frac{p}{q} + \frac{1}{q^n} \right).$$

Each $G_n$ is a union of open intervals, hence $G_n$ is open. Moreover, $G_n$ contains every rational number of the form $p/q$ with $q \geq 2$, so $G_n \supset Q$. Since $Q$ is dense in $\mathbb{R}$, $G_n$ is a dense open set, and therefore its complement $G_n'$ is nowhere dense.

From (5), taking complements,

$$E' = Q \cup \bigcup_{n=1}^{\infty} G_n'.$$

The set $Q$ is countable (hence of first category), and each $G_n'$ is nowhere dense (hence of first category). A countable union of first-category sets is of first category, so $E'$ is of first category.

It follows that $E$ is residual. By Baire's category theorem, a residual subset of a complete metric space is dense. Therefore $E$ (and hence the set of transcendental Liouville numbers) intersects every nonempty interval.
