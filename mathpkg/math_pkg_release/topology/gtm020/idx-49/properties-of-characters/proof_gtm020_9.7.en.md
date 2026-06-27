---
role: proof
locale: en
of_concept: properties-of-characters
source_book: gtm020
source_chapter: "9"
source_section: "7"
---

**Proof.** All statements follow from elementary properties of the trace operator $\operatorname{Tr}$.

(1) If $\phi: M \to N$ is a $G$-module isomorphism, then for each $s \in G$, the linear maps $s_M$ and $s_N$ are related by $s_N = \phi \circ s_M \circ \phi^{-1}$. Since similar matrices have equal trace, $\chi_M(s) = \operatorname{Tr}(s_M) = \operatorname{Tr}(s_N) = \chi_N(s)$.

(2) The linear transformation $s_{M \oplus N}$ on $M \oplus N$ is represented by a block diagonal matrix $\begin{pmatrix} s_M & 0 \\ 0 & s_N \end{pmatrix}$, so $\operatorname{Tr}(s_{M \oplus N}) = \operatorname{Tr}(s_M) + \operatorname{Tr}(s_N)$. Hence $\chi_{M \oplus N} = \chi_M + \chi_N$.

(3) The linear transformation $s_{M \otimes N}$ on $M \otimes N$ has trace $\operatorname{Tr}(s_M \otimes s_N) = \operatorname{Tr}(s_M) \cdot \operatorname{Tr}(s_N)$. Hence $\chi_{M \otimes N}(s) = \chi_M(s) \cdot \chi_N(s)$. $\square$
