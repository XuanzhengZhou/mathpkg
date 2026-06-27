---
role: proof
locale: en
of_concept: if-vdash-varphi-leftrightarrow-forall-xpsix-and-vdash-varphi-leftrightarrow-exis
source_book: gtm001
source_chapter: "11"
source_section: ""
---

** If all of the free variables of $\varphi, (\forall x)\psi(x)$, and $(\exists x)\eta(x)$ are among $a_1, \ldots, a_n$ then by Theorem 12.6

$$a_1, \ldots, a_n \in A \rightarrow [\varphi^A \leftrightarrow (\forall x \in A)\psi^A(x)].$$

$$a_1, \ldots, a_n \in A \rightarrow [\varphi^A \leftrightarrow (\exists x \in A)\eta^A(x)].$$

Also since $\psi(x)$ and $\eta(x)$ are absolute

$$a_1, \ldots, a_n \in A \wedge x \in A \rightarrow [\psi(x) \leftrightarrow \psi^A(x)],$$

$$

Remark. Satisfaction and absoluteness have been defined for wffs. Most of our theorems in ZF are however wffs in the wider sense (Definition 4.1). It is therefore convenient to extend our definitions to wffs in the wider sense.
