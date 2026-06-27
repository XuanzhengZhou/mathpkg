---
role: proof
locale: en
of_concept: faithfully-balanced-generator
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** ($\Rightarrow$). Since right multiplication $\\rho: S \\rightarrow \\operatorname{End}({}_R Q)$ is a ring isomorphism, as right $S$-modules

$$\\operatorname{Hom}_R(Q, Q_S) \\cong S_S.$$

Also by (17.6), since ${}_R Q$ is a generator,

$${}_R Q^{(n)} \\cong R \\oplus R'$$

for some left $R$-module $R'$. Applying (16.3) and (4.5) we get right $S$-isomorphisms

$$S^{(n)} \\cong \\operatorname{Hom}_R(Q, Q_S)^{(n)} \\cong \\operatorname{Hom}_R(Q^{(n)}, Q_S)$$

$$\\cong \\operatorname{Hom}_R(R \\oplus R', Q_S) \\cong \\operatorname{Hom}_R(R, Q_S) \\oplus \\operatorname{Hom}_R(R', Q_S)$$

$$\\cong Q \\oplus Q',$$

so that, by (17.3), $Q_S$ is finitely generated and projective.

($\Leftarrow$). This follows from (17.3) and (17.6) since

$${}_R Q^{(n)} \\cong \\operatorname{Hom}_S(S, {}_R Q^{(n)}) \\cong \\operatorname{Hom}_S(S^{(n)}, {}_R Q)$$

$$\\cong \\operatorname{Hom}_S(Q \\oplus Q', {}_R Q) \\cong \\operatorname{Hom}_S(Q, {}_R Q) \\oplus \\operatorname{Hom}_S(Q', {}_R Q)$$

$$\\cong R \\oplus \\operatorname{Hom}_S(Q', {}_R Q).$$
