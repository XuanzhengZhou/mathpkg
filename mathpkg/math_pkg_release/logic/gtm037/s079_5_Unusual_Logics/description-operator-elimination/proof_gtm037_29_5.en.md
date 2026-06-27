---
role: proof
locale: en
of_concept: description-operator-elimination
source_book: gtm037
source_chapter: "29"
source_section: "Unusual Logics"
---

We proceed by simultaneous induction on $\sigma$ and $\varphi$. If $\sigma$ is $v_i$, then for $\psi$ in (i) we may take the formula $v_i = v_k$. If $\sigma$ is $\mathbf{O} \rho_0 \cdots \rho_{m-1}$ and $v_k$ does not occur in $\sigma$, first choose distinct new variables $v_{l0}, \ldots, v_{l(m-1)}$ not occurring in $\sigma$ and different from $v_k$. By the induction assumption there are formulas $\psi_i$ for $i < m$ not involving $\tau$ such that $\Gamma \models \rho_i = v_{li} \leftrightarrow \psi_i$. The required formula $\psi$ is then obtained by combining these equivalences with the equation $\sigma = v_k$.

For formulas, the induction proceeds through the connectives, quantifiers, and atomic formulas. The only nontrivial case is an atomic formula containing a $\tau$-term, which reduces to case (i).
