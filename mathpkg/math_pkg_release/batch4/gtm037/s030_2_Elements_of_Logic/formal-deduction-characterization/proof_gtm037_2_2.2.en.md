---
role: proof
locale: en
of_concept: formal-deduction-characterization
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

The equivalence follows directly from the inductive definition of $\Gamma \vdash \varphi$ as the closure of $\Gamma \cup \operatorname{Axm}$ under modus ponens and generalization. 

For the forward direction ($\Rightarrow$), one proves by induction on the closure definition that any formula in the deductive closure has a finite sequence witnessing the derivation. If $\varphi$ is in $\Gamma$ or $\operatorname{Axm}$, take a sequence of length $1$. If $\varphi$ is obtained by modus ponens from $\psi$ and $\psi \to \varphi$, concatenate the witnessing sequences for $\psi$ and $\psi \to \varphi$ and append $\varphi$. If $\varphi = \forall v_k \psi$ is obtained by generalization, take the witnessing sequence for $\psi$ and append $\forall v_k \psi$.

For the converse ($\Leftarrow$), one shows by induction on the length $m$ of the sequence that every formula appearing in a sequence satisfying (i)-(iv) belongs to the deductive closure. The base cases (i) and (ii) are immediate. For modus ponens (iii), if $\psi_j$ and $\psi_k = (\psi_j \to \psi_i)$ are in the deductive closure by induction hypothesis, then $\psi_i$ is also in the closure by the modus ponens closure condition. For generalization (iv), the same reasoning applies.
