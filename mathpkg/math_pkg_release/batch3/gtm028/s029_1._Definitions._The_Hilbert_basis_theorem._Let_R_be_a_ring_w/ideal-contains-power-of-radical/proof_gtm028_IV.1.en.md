---
role: proof
locale: en
of_concept: ideal-contains-power-of-radical
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

Let $\mathfrak{A}$ be an ideal of the noetherian ring $R$. By the finite basis condition, the radical $\sqrt{\mathfrak{A}}$ has a finite basis $\{c_1, \dots, c_h\}$. For each $i = 1, \dots, h$, there exists an integer $k_i$ such that $c_i^{k_i} \in \mathfrak{A}$; let $k = \max\{k_1, \dots, k_h\}$, so that $c_i^k \in \mathfrak{A}$ for all $i$.

Set $m = h(k-1) + 1$. A basis for the power $(\sqrt{\mathfrak{A}})^m$ is provided by the power products $\prod_{i=1}^h c_i^{e_i}$ where $\sum_{i=1}^h e_i = m$ and each $e_i \geq 0$. Since $m > h(k-1)$, at least one of the exponents $e_i$ must satisfy $e_i \geq k$. Consequently, $c_i^{e_i} \in \mathfrak{A}$, and therefore the entire product $\prod_i c_i^{e_i}$ lies in $\mathfrak{A}$. This shows that $(\sqrt{\mathfrak{A}})^m \subseteq \mathfrak{A}$.
