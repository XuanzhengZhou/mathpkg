---
role: proof
locale: en
of_concept: simply-connected-primitive-existence
source_book: gtm011
source_chapter: "IV"
source_section: "6.16"
---

Fix a point $a$ in $G$ and define $F(z) = \int_{\gamma_z} f(w)\,dw$ where $\gamma_z$ is any rectifiable curve in $G$ from $a$ to $z$. Since $G$ is simply connected, by Cauchy's Theorem (Fourth Version, 6.15), $\int_{\gamma} f = 0$ for every closed rectifiable curve $\gamma$ in $G$. It follows that $F(z)$ is well-defined (independent of the choice of path $\gamma_z$ from $a$ to $z$). Standard arguments then show that $F'(z) = f(z)$ for all $z \in G$, so $F$ is a primitive of $f$ in $G$.
