---
role: proof
locale: en
of_concept: composition-with-nuclear-map
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

**Nuclearity of $v \circ u$.** By (7.1), the nuclear map $v$ admits a representation $v(y) = \sum \lambda_n f_n(y) z_n$ with $\sum |\lambda_n| < +\infty$, $\{f_n\} \subset G'$ equicontinuous, and $\{z_n\}$ contained in a bounded subset $B$ of $H$ such that $H_B$ is complete. Then $v \circ u(x) = \sum \lambda_n (f_n \circ u)(x) z_n$, and the sequence $\{f_n \circ u\}$ is equicontinuous in $E'$ since $u$ is continuous. Hence $v \circ u$ is nuclear by the series characterization of (7.1).

**Nuclearity of $w \circ v$.** By Corollary 1, $v$ is compact, so there exists a convex, circled $0$-neighborhood $V$ in $F$ such that $\overline{v(V)} = B$ is compact in $G$. Then $B_1 = w(B)$ is compact in $H$, so $H_{B_1}$ is complete. Since the image of $V$ under $w \circ v$ is $w(v(V)) \subset w(B) = B_1$, the composition factors through $\tilde{F}_V$ and $H_{B_1}$, and is therefore nuclear by definition.

The composition $w \circ v \circ u$ is then nuclear by applying the two cases above in succession.
