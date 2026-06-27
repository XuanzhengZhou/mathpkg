---
role: proof
locale: en
of_concept: quantifier-elimination-rich-sets
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

The proof proceeds by induction on the structure of the sentence $\varphi$.

**Base case.** If $\varphi$ is atomic (an equality $\sigma = \tau$ or a relation application $\mathbf{R}\sigma_0\cdots\sigma_{m-1}$), then $\varphi$ itself is quantifier-free, and we may take $\psi = \varphi$.

**Induction steps for Boolean connectives.** If $\varphi = \neg\varphi_1$, by the induction hypothesis there is a quantifier-free $\psi_1$ with $\Gamma \vdash \varphi_1 \leftrightarrow \psi_1$, and we take $\psi = \neg\psi_1$. Similarly, if $\varphi = \varphi_1 \lor \varphi_2$ (or $\varphi_1 \land \varphi_2$), by induction we obtain quantifier-free $\psi_1, \psi_2$ and take $\psi = \psi_1 \lor \psi_2$ (or $\psi_1 \land \psi_2$).

**Induction step for the universal quantifier.** If $\varphi = \forall v_i \varphi_1$, note that $\forall v_i \varphi_1$ is equivalent to $\neg\exists v_i \neg\varphi_1$. By the induction hypothesis, there is a quantifier-free $\psi_1$ with $\Gamma \vdash \neg\varphi_1 \leftrightarrow \psi_1$. Since $\Gamma$ is rich, there exists a constant $c$ such that $\Gamma \vdash \exists v_i \psi_1 \rightarrow \operatorname{Subf}_c^{v_i}\psi_1$. But $\operatorname{Subf}_c^{v_i}\psi_1$ is quantifier-free (no variables occur in a sentence). Then $\neg\operatorname{Subf}_c^{v_i}\psi_1$ is quantifier-free and provably equivalent to $\varphi$ modulo $\Gamma$. By induction on formula complexity, the result follows for all sentences.
