---
role: proof
locale: en
of_concept: spanning-set-epimorphism
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

For each $x \in X$, the right multiplication map $\rho_x: R \to M$ defined by $\rho_x(r) = rx$ is a homomorphism of left $R$-modules. Taking the direct sum over all $x \in X$ yields a homomorphism

$$f = \bigoplus_{x \in X} \rho_x: R^{(X)} \to M.$$

Since $X$ spans $M$, every element of $M$ is a finite $R$-linear combination of elements of $X$, hence lies in the image of $f$. Therefore $f$ is surjective, i.e., an epimorphism

$$R^{(X)} \rightarrow M \rightarrow 0.$$
