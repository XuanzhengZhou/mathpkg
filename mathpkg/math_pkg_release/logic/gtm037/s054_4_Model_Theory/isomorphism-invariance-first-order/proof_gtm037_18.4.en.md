---
role: proof
locale: en
of_concept: isomorphism-invariance-first-order
source_book: gtm037
source_chapter: "18"
source_section: "4"
---

The proof is by induction on the structure of terms and formulas.

**Terms.** For a variable $v_k$, we have $f(v_k^{\mathfrak{A}}[x]) = f(x_k) = (f \circ x)_k = v_k^{\mathfrak{B}}(f \circ x)$. For a constant symbol $c$, $f(c^{\mathfrak{A}}) = c^{\mathfrak{B}}$ because $f$ is an isomorphism, and $c^{\mathfrak{B}}(f \circ x) = c^{\mathfrak{B}}$ since constants do not depend on the assignment. For a compound term $\mathbf{O}(\sigma_0, \ldots, \sigma_{m-1})$, we use the induction hypothesis and the fact that $f$ commutes with operations:
$$f(\mathbf{O}^{\mathfrak{A}}(\sigma_0^{\mathfrak{A}}[x], \ldots)) = \mathbf{O}^{\mathfrak{B}}(f(\sigma_0^{\mathfrak{A}}[x]), \ldots) = \mathbf{O}^{\mathfrak{B}}(\sigma_0^{\mathfrak{B}}(f \circ x), \ldots).$$

**Formulas.** For an atomic formula $R(\sigma_0, \ldots, \sigma_{m-1})$, we apply the term case and the fact that $f$ preserves relations. For $\neg \psi$ and $\psi \to \chi$, the induction step is immediate from the definition of satisfaction. For $\forall v_k \psi$, we have $\mathfrak{A} \models \forall v_k \psi[x]$ iff for all $a \in A$, $\mathfrak{A} \models \psi[x(k|a)]$. By induction hypothesis, this holds iff for all $a \in A$, $\mathfrak{B} \models \psi[(f \circ x)(k|f(a))]$. Since $f$ is surjective, this is equivalent to for all $b \in B$, $\mathfrak{B} \models \psi[(f \circ x)(k|b)]$, i.e., $\mathfrak{B} \models \forall v_k \psi[f \circ x]$.

The sentence case follows immediately: $\mathfrak{A} \models \varphi$ iff $\mathfrak{A} \models \varphi[\emptyset]$ iff $\mathfrak{B} \models \varphi[f \circ \emptyset]$ iff $\mathfrak{B} \models \varphi[\emptyset]$ iff $\mathfrak{B} \models \varphi$.
