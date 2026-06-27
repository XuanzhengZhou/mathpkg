---
role: proof
locale: en
of_concept: lemma-177-relation-symbols-of-lel
source_book: gtm037
source_chapter: "Part 3"
source_section: "Decidable and Undecidable Theories"
---

This is an immediate corollary of Lemma 17.6. By Definition 17.4(xv), the theory $\mathcal{P}$ contains the axiom:

$$\forall v_0 \cdots \forall v_{m-1}(R_{\mathbf{O}} v_0 \cdots v_{m-1} \leftrightarrow \mathbf{O} v_0 \cdots v_{m-1} = \Delta 1).$$

By Definition 17.4, the number-theoretic interpretation of $R_{\mathbf{O}}$ is:

$$\#R_{\mathbf{O}} = \{(x_0, \ldots, x_{m-1}): \#\mathbf{O} x_0 \cdots x_{m-1} = 1\}.$$

Now suppose $(x_0, \ldots, x_{m-1}) \in \#R_{\mathbf{O}}$. Then by definition, $\#\mathbf{O} x_0 \cdots x_{m-1} = 1$. By Lemma 17.6, $\mathcal{P} \models \mathbf{O}(\Delta x_0, \ldots, \Delta x_{m-1}) = \Delta 1$. Using the defining axiom (xv) for $R_{\mathbf{O}}$, we conclude $\mathcal{P} \models R_{\mathbf{O}}(\Delta x_0, \ldots, \Delta x_{m-1})$.

Conversely, if $(x_0, \ldots, x_{m-1}) \notin \#R_{\mathbf{O}}$, then $\#\mathbf{O} x_0 \cdots x_{m-1} \neq 1$. By Lemma 17.6 (the contrapositive of condition (ii) in Definition 17.1 applied through the representation), $\mathcal{P} \models \neg \mathbf{O}(\Delta x_0, \ldots, \Delta x_{m-1}) = \Delta 1$. Again using axiom (xv), we obtain $\mathcal{P} \models \neg R_{\mathbf{O}}(\Delta x_0, \ldots, \Delta x_{m-1})$.
