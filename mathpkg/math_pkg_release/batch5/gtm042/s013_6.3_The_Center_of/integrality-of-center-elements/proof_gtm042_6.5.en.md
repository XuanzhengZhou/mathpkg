---
role: proof
locale: en
of_concept: integrality-of-center-elements
source_book: gtm042
source_chapter: "6"
source_section: "6.5"
---

Let $c_i$ ($1 \leqslant i \leqslant h$) be the conjugacy classes of $G$ and set $e_i = \sum_{s \in c_i} s$. For $s_i \in c_i$, write $u$ as
$$u = \sum_{i=1}^{h} u(s_i) e_i.$$

By hypothesis, each $u(s_i)$ is an algebraic integer. It suffices to show the $e_i$ are integral over $\mathbb{Z}$ (by corollaries to Proposition 14).

Consider $R = \mathbb{Z}e_1 \oplus \cdots \oplus \mathbb{Z}e_h \subset \text{Cent. } C[G]$. Each product $e_i e_j$ is a $\mathbb{Z}$-linear combination of the $e_k$, so $R$ is a subring, finitely generated as a $\mathbb{Z}$-module. By Corollary 1 to Proposition 14, every element of $R$ is integral over $\mathbb{Z}$. In particular each $e_i$ is integral.

Since the $u(s_i)$ are algebraic integers and the $e_i$ are integral over $\mathbb{Z}$, their product $u(s_i)e_i$ is integral, and the sum $u = \sum u(s_i)e_i$ is integral over $\mathbb{Z}$.
