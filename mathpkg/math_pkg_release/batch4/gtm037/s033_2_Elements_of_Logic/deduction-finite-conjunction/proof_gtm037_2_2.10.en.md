---
role: proof
locale: en
of_concept: deduction-finite-conjunction
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

This corollary follows from Theorem 10.87 (the Generalized Deduction Theorem) together with 10.33$(ii)$, which guarantees that only finitely many members of $\Delta$ are needed in any proof of $\varphi$ from $\Gamma \cup \Delta$. Specifically, if $\Gamma \cup \Delta \vdash \varphi$, then there exist $\psi_0, \dots, \psi_{m-1} \in \Delta$ such that $\Gamma \cup \{\psi_0, \dots, \psi_{m-1}\} \vdash \varphi$. Applying Theorem 10.87 yields $\Gamma \vdash \psi_0 \wedge \cdots \wedge \psi_{m-1} \rightarrow \varphi$. The converse direction is immediate. $\square$
