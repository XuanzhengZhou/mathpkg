---
role: proof
locale: en
of_concept: boundary-of-singular-set-is-tdz
source_book: gtm015
source_chapter: "56"
source_section: "56.3"
---

# Proof of Boundary of singular set consists of TDZ

(56.3) Lemma. Let $S$ be the set of singular elements of $A$ and let $\partial S$ be the boundary of $S$. Every element of $\partial S$ is a two-sided TDZ in $A$.

Proof. Let $x \in \partial S = \overline{S} \cap \overline{\mathbb{C}S}$. Since $S = \mathbb{C}U$ is closed (50.6), we have $\partial S = S \cap \overline{U}$. Thus $x$ is singular, but there exists a sequence of invertible elements $x_n$ such that $\|x_n - x\| \rightarrow 0$. Let $y_n = x_n^{-1}$ and define $z_n = \|y_n\|^{-1}y_n$; it will be shown that $xz_n \rightarrow 0$ and $z_nx \rightarrow 0$. At any rate,

$$xz_n = (x - x_n)z_n + x_n
