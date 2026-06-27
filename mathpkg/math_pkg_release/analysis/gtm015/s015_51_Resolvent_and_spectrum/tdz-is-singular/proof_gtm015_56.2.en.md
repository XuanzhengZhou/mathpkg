---
role: proof
locale: en
of_concept: tdz-is-singular
source_book: gtm015
source_chapter: "56"
source_section: "56.2"
---

# Proof of Topological divisors of zero are singular

(56.2) Lemma. Every TDZ is singular. More precisely, if $x$ is a left [right] TDZ, then $x$ has no left [right] inverse.

Proof. Assuming $x$ is left-invertible, say $yx = 1$, it is to be shown that $x$ is not a left TDZ. Indeed, if $y_n$ is any sequence in $A$ with $\|y_n\| = 1$, it results from

$$1 = \|y_n\| = \|(yx)y_n\| = \|y(xy_n)\| \leq \|y\| \|xy_n\|$$

that $xy_n \not\to 0$.
