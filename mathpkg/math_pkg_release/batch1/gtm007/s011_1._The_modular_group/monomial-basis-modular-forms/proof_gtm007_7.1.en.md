---
role: proof
locale: en
of_concept: monomial-basis-modular-forms
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

**Generation.** We prove the monomials $G_2^\alpha G_3^\beta$ with $2\alpha + 3\beta = k$ generate $M_k$. This is clear for $k \leq 3$ by Theorem 4 parts (i) and (ii). For $k \geq 4$, argue by induction on $k$. Choose integers $\gamma, \delta \geq 0$ such that $2\gamma + 3\delta = k$ (possible for all $k \geq 2$). The modular form $g = G_2^\gamma G_3^\delta$ is not zero at infinity (since $G_2(\infty) \neq 0$ and $G_3(\infty) \neq 0$). For any $f \in M_k$, there exists $\lambda \in \mathbf{C}$ such that $f - \lambda g$ vanishes at infinity, hence is a cusp form. By Theorem 4(iii), $f - \lambda g = \Delta h$ with $h \in M_{k-6}$. Applying the inductive hypothesis to $h$ expresses it as a linear combination of monomials, and multiplication by $\Delta = G_2^3 - 27 G_3^2$ (which itself is a polynomial in $G_2, G_3$) preserves the polynomial form.

**Linear independence.** If the monomials were linearly dependent, there would be a nontrivial polynomial relation $P(G_2, G_3) = 0$. Then the ratio $G_2^3 / G_3^2$ would satisfy a nontrivial algebraic equation over $\mathbf{C}$, hence would be constant. But $G_2(\rho) = 0$ while $G_3(\rho) \neq 0$, a contradiction. Thus the monomials are linearly independent and form a basis.
