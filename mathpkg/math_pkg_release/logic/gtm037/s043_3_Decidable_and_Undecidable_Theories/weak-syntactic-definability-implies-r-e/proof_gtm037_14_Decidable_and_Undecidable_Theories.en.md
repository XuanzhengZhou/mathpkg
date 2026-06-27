---
role: proof
locale: en
of_concept: weak-syntactic-definability-implies-r-e
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

Say $\Gamma$ is recursively axiomatized by $\Delta$. Let $T_m^{\Delta}$ be as in the proof of Theorem 14.5. Let $R$ be weakly syntactically defined in $\Gamma$ by $\varphi$, and let $e = g^{+} \varphi$. Clearly for all $x_0, \ldots, x_{m-1} \in \omega$ we have

$$\langle x_0, \ldots, x_{m-1} \rangle \in R \quad \text{iff} \quad \exists y ((e, x_0, \ldots, x_{m-1}, y) \in T_m^{\Delta}),$$

so $R$ is r.e.

The intuitive basis of this theorem is as follows: given $R$, unary, weakly syntactically defined by $\varphi$ in $\Gamma$, where $\Gamma$ is axiomatized by an effective set $\Delta$, first start listing out all $\Delta$-theorems. Whenever $\varphi(\mathbf{x})$ appears on the list, give output $x$. In this way $R$ will be effectively enumerated.
