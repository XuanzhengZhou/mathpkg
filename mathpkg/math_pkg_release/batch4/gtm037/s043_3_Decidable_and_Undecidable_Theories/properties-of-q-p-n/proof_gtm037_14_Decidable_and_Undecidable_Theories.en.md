---
role: proof
locale: en
of_concept: properties-of-q-p-n
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

(i) $Q$ is finitely axiomatizable by definition, since it is axiomatized by the seven sentences (a)-(g).

(ii) $P$ is recursively axiomatizable because the set of its axioms consists of the finite set (a), (b), (d)-(g) together with the recursive set of induction axioms, one for each formula $\psi$.

(iii) For $Q$, $P$, and $N$, the $\omega$-consistency follows from the fact that each has the standard model $\mathfrak{A} = (\omega, +, \cdot, \mathbf{s}, \mathbf{0})$. If $\operatorname{Fv}(\varphi) \subseteq \{v_0\}$ and $\varphi(\mathbf{x}) \in \Gamma$ for each $x \in \omega$, then $\mathfrak{A} \models \varphi[\mathbf{x}]$ for each $x$, hence $\mathfrak{A} \models \forall v_0 \varphi(v_0)$. Since $\mathfrak{A}$ is a model of each theory, $\exists v_0 \neg \varphi(v_0)$ cannot be in the theory. (The proof is analogous to that of 14.10.)
