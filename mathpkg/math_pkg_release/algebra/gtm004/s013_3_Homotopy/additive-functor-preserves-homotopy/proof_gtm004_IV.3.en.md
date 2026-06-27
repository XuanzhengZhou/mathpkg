---
role: proof
locale: en
of_concept: additive-functor-preserves-homotopy
source_book: gtm004
source_chapter: "IV"
source_section: "3. Homotopy"
---

# Proof of Additive Functors Preserve Homotopy

**Lemma 3.4.** Let $F : \mathcal{A} \rightarrow \mathcal{B}$ be an additive functor between abelian categories. If $\varphi \simeq \psi : C \rightarrow D$ in $\mathbf{Ch}(\mathcal{A})$, then

$$F(\varphi) \simeq F(\psi) : F(C) \rightarrow F(D) \quad \text{in } \mathbf{Ch}(\mathcal{B}).$$

Consequently, $F$ induces a functor between the homotopy categories.

*Proof.* Let $\Sigma : \varphi \simeq \psi$ be a homotopy, so that

$$\psi - \varphi = \partial_D \Sigma + \Sigma \partial_C.$$

Applying the additive functor $F$ to this equation yields

$$F(\psi) - F(\varphi) = F(\psi - \varphi) = F(\partial_D \Sigma + \Sigma \partial_C).$$

Since $F$ is additive, it preserves sums, and since $F$ applied to a chain complex $C$ yields the complex $F(C)$ with differential $F(\partial_C)$, we have

$$F(\partial_D \Sigma + \Sigma \partial_C) = F(\partial_D) F(\Sigma) + F(\Sigma) F(\partial_C) = \partial_{F(D)} F(\Sigma) + F(\Sigma) \partial_{F(C)}.$$

Thus $F(\Sigma) : F(C) \rightarrow F(D)$ is a homotopy from $F(\varphi)$ to $F(\psi)$, i.e., $F(\varphi) \simeq F(\psi)$. $\square$
