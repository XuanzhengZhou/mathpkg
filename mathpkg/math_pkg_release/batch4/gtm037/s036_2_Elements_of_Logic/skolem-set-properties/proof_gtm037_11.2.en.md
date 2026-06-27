---
role: proof
locale: en
of_concept: skolem-set-properties
source_book: gtm037
source_chapter: "11"
source_section: "2"
---

Clearly $\varphi^S$ is universal and $\text{Fv}\,\varphi = \text{Fv}\,\varphi^S$.

\textbf{(i)} This is easily proved by induction on $\varphi$. The Skolem form $\varphi^S$ is constructed by successively replacing existential quantifiers with Skolem function symbols, and each replacement weakens the formula: $\exists v_i \psi$ is replaced by $\psi(v_i / S_{\exists v_i \psi} \alpha_0 \cdots \alpha_{m-1})$, where $\{\alpha_0, \ldots, \alpha_{m-1}\} = \text{Fv}\,\exists v_i \psi$. Since the Skolem term denotes some element, if the Skolem form holds then there exists a witness (the value of the Skolem term) for the existential quantifier, so the original formula holds.

\textbf{(ii)} Also proved by induction on $\varphi$. Assume $\mathfrak{A}$ is a model of the Skolem set of $L'$ over $\mathcal{L}$. The Skolem set contains axioms of the form

$$\forall \alpha_0 \cdots \forall \alpha_{m-1} [\exists v_i \psi \rightarrow \psi(v_i / S_{\exists v_i \psi} \alpha_0 \cdots \alpha_{m-1})],$$

which ensure that whenever the original formula holds, the Skolem form (with the Skolem term substituted for the existentially quantified variable) also holds.

\textbf{(iii)(a)} Assume the hypothesis and let $\varphi \in \Gamma$. Then $\mathfrak{A} \models \varphi$ by hypothesis, so by (ii), $\mathfrak{A}' \models \varphi^S$. Thus $\mathfrak{A}'$ is a model of $\Gamma'$, as desired.

\textbf{(iii)(b)} This follows from (i). If $\mathfrak{A}' \models \Gamma'$ and $\varphi \in \Gamma$, then $\mathfrak{A}' \models \varphi^S$, so by (i), $\mathfrak{A}' \models \varphi$. Since $\varphi$ is an $\mathcal{L}$-formula, $\mathfrak{A}' \upharpoonright \mathcal{L} \models \varphi$, hence $\mathfrak{A}' \upharpoonright \mathcal{L} \models \Gamma$.

\textbf{(iii)(c)} Assume first that $\Gamma \models \varphi$, where $\varphi$ is a sentence of $\mathcal{L}$. If $\mathfrak{A}'$ is any model of $\Gamma'$, then by (iii)(b), $\mathfrak{A}' \upharpoonright \mathcal{L}$ is a model of $\Gamma$ and so $\mathfrak{A}' \upharpoonright \mathcal{L} \models \varphi$. Thus $\mathfrak{A}' \models \varphi$, showing $\Gamma' \models \varphi$. Conversely, if $\Gamma' \models \varphi$ for an $\mathcal{L}$-sentence $\varphi$, and $\mathfrak{A} \models \Gamma$, expand $\mathfrak{A}$ to an $\mathcal{L}'$-structure $\mathfrak{A}'$ that is a model of the Skolem set (as constructed in the proof of the Skolem expansion theorem). Then by (iii)(a), $\mathfrak{A}' \models \Gamma'$, so $\mathfrak{A}' \models \varphi$, hence $\mathfrak{A} \models \varphi$.

\textbf{(iv)} If $\varphi$ has a model $\mathfrak{A}$, expand $\mathfrak{A}$ to a model $\mathfrak{A}'$ of the Skolem set; by (ii), $\mathfrak{A}' \models \varphi^S$, so $\varphi^S$ has a model. Conversely, if $\varphi^S$ has a model $\mathfrak{A}'$, then by (i), $\mathfrak{A}' \models \varphi$, so $\varphi$ has a model.
