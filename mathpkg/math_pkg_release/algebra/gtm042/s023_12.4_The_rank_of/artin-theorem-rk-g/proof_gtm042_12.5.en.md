---
role: proof
locale: en
of_concept: artin-theorem-rk-g
source_book: gtm042
source_chapter: "12"
source_section: "12.5"
---

The two proofs given in Chapter 9 apply without change.

**First proof (duality argument).** One must show that the mapping

$$\mathbb{Q} \otimes \operatorname{Res} : \mathbb{Q} \otimes R_K(G) \rightarrow \bigoplus_{H \in T} \mathbb{Q} \otimes R_K(H)$$

is injective, which is clear: if a virtual character restricts to zero on every cyclic subgroup, it must be zero.

**Second proof (explicit formula).** Using the formula

$$g = \sum_{H \in T} \operatorname{Ind}_H^G(\theta_H), \quad \text{cf. Proposition 27 (9.4)},$$

one proves that $\theta_H$ belongs to $R_K(H)$. The latter can be verified either by induction on the order of $H$, or by observing that $\theta_H$ has integer values and thus belongs to $\overline{R}_K(H)$; since $H$ is abelian we have $R_K(H) = \overline{R}_K(H)$. Now the identity above shows that the constant function $1$ belongs to the image of $\mathbb{Q} \otimes \operatorname{Ind}$. Since this image is an ideal, it must be the whole ring $\mathbb{Q} \otimes R_K(G)$.
