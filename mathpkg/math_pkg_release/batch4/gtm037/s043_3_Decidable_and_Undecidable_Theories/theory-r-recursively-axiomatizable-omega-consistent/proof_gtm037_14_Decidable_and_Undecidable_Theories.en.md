---
role: proof
locale: en
of_concept: theory-r-recursively-axiomatizable-omega-consistent
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

Condition (i) is obvious since the axioms of $R$ are given by a simple recursive enumeration.

To prove (ii), first note that $\mathfrak{A} = \langle \omega, +, \cdot, s, 0 \rangle$ is a model of $R$. Now if $\operatorname{Fv}(\varphi) \subseteq \{v_0\}$ and $\varphi(\mathbf{x}) \in R$ for each $x \in \omega$, then $\mathfrak{A} \models \varphi[\mathbf{x}]$ for each $x \in \omega$ and hence $\mathfrak{A} \models \forall v_0 \varphi(v_0)$. Since $\mathfrak{A}$ is a model of $R$ it follows that $\exists v_0 \neg \varphi(v_0) \notin R$. Thus $R$ is $\omega$-consistent.
