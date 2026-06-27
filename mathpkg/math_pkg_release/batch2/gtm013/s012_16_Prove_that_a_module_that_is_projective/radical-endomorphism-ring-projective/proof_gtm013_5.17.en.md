---
role: proof
locale: en
of_concept: radical-endomorphism-ring-projective
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** ($\Leftarrow$). Suppose $\\operatorname{Im} a \\ll_R P$. Then it suffices to show that $Sa \\ll_S S$. Suppose that $I \\leq_S S$ and $Sa + I = S$. Then $1_P = sa + b$ for some $s \\in S$ and $b \\in I$. Then $P = P1_P \\leq Psa + Pb \\leq \\operatorname{Im} a + Pb$, so $Pb = P$. But then $b$ is an epimorphism $b: P \\rightarrow P$. Since $P$ is projective, this epimorphism splits and there is $c \\in S$ with $1_P = cb \\in I$. Thus $I = S$ and $Sa \\ll_S S$.

($\Rightarrow$). Let $a \\in J(S)$ and suppose that $K \\leq P$ with $\\operatorname{Im} a + K = P$. Let $n_K: P \\rightarrow P/K$ be the natural epimorphism. Then $a n_K: P \\rightarrow P/K$ is epic. Choosing $s \\in S$ such that the diagram commutes, we have $(1 - sa)n_K = 0$. But since $a \\in J(S)$, $1 - sa$ is invertible and $n_K = 0$. Therefore $K = P$.
