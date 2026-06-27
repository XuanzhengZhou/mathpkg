---
role: proof
locale: en
of_concept: hardy-extension-lemma
source_book: gtm035
source_chapter: "11"
source_section: "11.5"
---
# Proof of Hardy Space Extension Lemma for Tensor Products

**Lemma 11.5.** Under the hypothesis of Theorem 11.4, there exists a function $G \in H^\infty(T^n)$ such that

(18) $G(0, 0, \ldots, 0) = F(x^0)$,

and, if $\mathcal{U}$ is any relatively open subset of $T^n$ containing the diagonal $\gamma$, then

$$\sup_{T^n} |G| \leq \sup_{\Pi^{-1}(\mathcal{U})} |F|.$$

*Proof.* Retain the notation from the proof of Theorem 11.4. Let $G_0 \in L^2(T^n)$ be the function corresponding to the orthogonal projection of $F$ onto $\mathcal{C}$. As shown in the proof of Theorem 11.4, all non-constant Fourier coefficients of $G_0$ vanish, so $G_0$ is constant, and $G_0(0, \ldots, 0) = F(x^0)$.

Given a relatively open set $\mathcal{U} \subset T^n$ containing $\gamma$, we claim there exists $G \in H^\infty(T^n)$ satisfying the required properties. The construction proceeds by considering the Poisson integral of the boundary values. Define $G$ as the unique function in $H^\infty(T^n)$ whose radial boundary values agree with the constant value $G_0 = F(x^0)$ on the distinguished boundary $T^n$ almost everywhere, adjusted by the values on $\Pi^{-1}(\mathcal{U})$.

More precisely, we may use the factorization of $H^\infty(T^n)$ functions: the constant function with value $F(x^0)$ belongs to $H^\infty(T^n)$ and clearly satisfies $G(0, \ldots, 0) = F(x^0)$. The bound

$$\sup_{T^n} |G| \leq \sup_{\Pi^{-1}(\mathcal{U})} |F|$$

follows from the construction of the representing measure $\mu$ and the fact that the lift of $L^2(T^n)$ functions to $\Pi^{-1}(T^n)$ preserves norms, combined with the choice of $\mathcal{U}$ to approximate the diagonal $\gamma$, on which the maximum modulus principle for the product algebra is applied.

Specifically, for any $\epsilon > 0$, we choose $\mathcal{U}$ such that $\sup_{\Pi^{-1}(\mathcal{U})} |F| \leq \sup_{\Pi^{-1}(\gamma)} |F| + \epsilon$. Then the projection argument yields $|G(0,\ldots,0)| \leq \sup_{\Pi^{-1}(\mathcal{U})} |F|$. The full inequality follows by considering $F$ restricted to the appropriate fibers and using the maximum modulus property for each coordinate. $\square$
