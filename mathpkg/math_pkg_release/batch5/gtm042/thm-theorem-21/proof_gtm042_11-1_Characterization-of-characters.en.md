---
role: proof
locale: en
of_concept: thm-theorem-21
source_book: gtm042
source_chapter: "11.1"
source_section: "Characterization of characters"
---

Let X be the set of all elementary subgroups of G. By th. 11, we can write the constant function 1 in the form

$$1 = \sum_{H \in X} \text{Ind}_H^G f_H, \quad \text{with} \ f_H \in R(H).$$

Multiplying by $\varphi$, this gives

$$\varphi = \sum_{H \in X} \varphi \cdot \text{Ind}_H^G f_H = \sum_{H \in X} \text{Ind}_H^G (f_H \cdot \text{Res}_H^G \varphi).$$

Since $f_H$ belongs to $R(H)$ and $\text{Res}_H^G \varphi$ belongs to $B \otimes R(H)$, their product belongs to $B \otimes R(H)$. It follows that $\varphi$ belongs to $B \otimes R(G)$.

A similar argument, using Artin's theorem (ch. 9) gives:
