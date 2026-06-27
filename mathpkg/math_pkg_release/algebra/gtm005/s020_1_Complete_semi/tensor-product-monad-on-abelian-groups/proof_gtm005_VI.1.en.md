---
role: proof
locale: en
of_concept: tensor-product-monad-on-abelian-groups
source_book: gtm005
source_chapter: "VI"
source_section: "1"
---

The adjunction $R \otimes_{\mathbb{Z}} - \dashv \operatorname{Hom}_{\mathbb{Z}}(R, -): \mathbf{Ab} \to \mathbf{Ab}$ (for a fixed ring $R$) induces a monad $(T, \eta, \mu)$ on $\mathbf{Ab}$ where $T(A) = R \otimes_{\mathbb{Z}} A$.

- $\eta_A: A \to R \otimes A$, $a \mapsto 1 \otimes a$.
- $\mu_A: R \otimes (R \otimes A) \to R \otimes A$, $r \otimes (s \otimes a) \mapsto (rs) \otimes a$ (using ring multiplication).

Monad laws follow from associativity and unit of $R$: $\mu \circ (\eta T) = 1_T$ (since $1 \otimes (r \otimes a) \mapsto r \otimes a$), $\mu \circ (T \mu) = \mu \circ (\mu T)$ (since $(r_1 r_2) r_3 = r_1 (r_2 r_3)$). Algebras for this monad are left $R$-modules: $h: R \otimes A \to A$ gives scalar multiplication $r \cdot a = h(r \otimes a)$.
