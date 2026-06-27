---
role: proof
locale: en
of_concept: scott-isomorphism-theorem
source_book: gtm037
source_chapter: "31"
source_section: "Unusual Logics"
---

For each finite sequence $a$ of length $n$ of elements of $A$ and each $\beta < \omega_1$, define formulas $\varphi_a^\beta \in \text{Fmla}_L^n$ by transfinite recursion: $\varphi_a^0$ is the conjunction of all atomic and negated atomic formulas true of $a$; for limit $\lambda$, $\varphi_a^\lambda = \bigwedge_{\alpha < \lambda} \varphi_a^\alpha$; and $\varphi_a^{\alpha+1} = \varphi_a^\alpha \wedge \bigwedge_{b \in A} \exists v_n \varphi_{a\langle b\rangle}^\alpha \wedge \forall v_n \bigvee_{b \in A} \varphi_{a\langle b\rangle}^\alpha$.

Since $A$ is countable, the descending chain of subsets defined by $\varphi_a^\alpha$ must stabilize at some countable ordinal. The stabilized formulas characterize the isomorphism type: if $\mathfrak{B} \models \varphi_\emptyset^\alpha$ for sufficiently large $\alpha$, then a back-and-forth argument shows $\mathfrak{B} \cong \mathfrak{A}$.
