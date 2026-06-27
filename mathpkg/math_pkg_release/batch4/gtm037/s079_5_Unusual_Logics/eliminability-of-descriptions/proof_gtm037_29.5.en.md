---
role: proof
locale: en
of_concept: eliminability-of-descriptions
source_book: gtm037
source_chapter: "29"
source_section: "5. Unusual Logics"
---

We proceed by simultaneous induction on $\sigma$ and $\varphi$.

If $\sigma$ is $v_i$, then for $\psi$ in (i) we may obviously take the formula $v_i = v_k$.

If $\sigma$ is $\mathbf{O} \rho_0 \cdots \rho_{m-1}$ and $v_k$ does not occur in $\sigma$, first choose distinct new variables $v_{l_0}, \ldots, v_{l_{m-1}}$ not occurring in $\sigma$ and different from $v_k$. By the induction assumption there are formulas $\psi_i$ for $i < m$ not involving $\tau$ such that

$$\Gamma \models \rho_i = v_{l_i} \leftrightarrow \psi_i$$

for each $i < m$. Then we may take $\psi$ to be

$$\exists v_{l_0} \cdots \exists v_{l_{m-1}} \left( \bigwedge_{i<m} \psi_i \land \mathbf{O} v_{l_0} \cdots v_{l_{m-1}} = v_k \right).$$

If $\sigma$ is $\tau v_i \varphi$ and $v_k$ does not occur in $\sigma$, we use the induction hypothesis on $\varphi$ to obtain $\varphi^*$. The construction ensures that the $\tau$-free formula $\psi$ satisfies the required equivalence.

For formulas, the induction proceeds similarly through the logical connectives and quantifiers, replacing each occurrence of $\tau$ using part (i) to eliminate $\tau$-terms. This completes the simultaneous induction and establishes both (i) and (ii).
