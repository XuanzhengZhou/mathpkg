---
role: proof
locale: en
of_concept: interpretation-model-theoretic-relationship
source_book: gtm037
source_chapter: ""
source_section: ""
---
The proof proceeds by induction on the structure of the formula $\varphi$.

For atomic formulas $\varphi \equiv R\mathbf{t}_0 \cdots \mathbf{t}_{n-1}$, the equivalence follows directly from the definition of the translation $\varphi^{\mathfrak{A}}$ in terms of the relation map $R$ and the term translations $\mathbf{t}_i^{\mathfrak{A}}$, together with the definition of $\mathfrak{B}^{\Gamma'\mathfrak{A}}$ as the model whose domain is $\{a \in B : \mathfrak{B} \models \chi[a]\}$ and whose relations and operations are interpreted via the translations under $\mathfrak{A}$.

For propositional connectives (e.g., $\neg \varphi$, $\varphi \land \psi$), the induction hypothesis applied to the subformulas immediately yields the equivalence, since $\models$ respects the standard truth-functional semantics of the connectives and the translation $(\cdot)^{\mathfrak{A}}$ commutes with propositional connectives by definition.

For the quantifier step, consider $\varphi \equiv \exists v_i \psi$. By definition, $\mathfrak{B}^{\Gamma'\mathfrak{A}} \models \exists v_i \psi[x]$ iff there exists $a \in B^{\Gamma'\mathfrak{A}}$ such that $\mathfrak{B}^{\Gamma'\mathfrak{A}} \models \psi[x(i|a)]$. By the induction hypothesis, this holds iff there exists $a \in B^{\Gamma'\mathfrak{A}}$ such that $\mathfrak{B} \models \psi^{\mathfrak{A}}[x(i|a)]$. The condition $a \in B^{\Gamma'\mathfrak{A}}$ means $\mathfrak{B} \models \chi[a]$, which is built into the translation $(\exists v_i \psi)^{\mathfrak{A}}$ via the formula $\chi$. Thus the condition is equivalent to $\mathfrak{B} \models (\exists v_i \psi)^{\mathfrak{A}}[x]$.

The case of the universal quantifier is handled similarly, or follows by duality with negation and the existential quantifier.
