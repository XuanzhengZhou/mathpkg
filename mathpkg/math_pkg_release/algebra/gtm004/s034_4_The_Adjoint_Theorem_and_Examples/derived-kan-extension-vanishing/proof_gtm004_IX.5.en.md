---
role: proof
locale: en
of_concept: derived-kan-extension-vanishing
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Vanishing of Derived Kan Extension on Projective Functors

**Proposition 5.8.** Let $\mathfrak{A}$ have enough projectives and exact coproducts. If $R \in [\mathfrak{U}, \mathfrak{A}]$ is an $\mathcal{E}_0$-projective functor, then $(L_n^{\mathcal{E}_1} \widetilde{J})R = 0$ for $n \geq 1$.

**Proof.** Clearly every functor $\mathfrak{U}_d \rightarrow \mathfrak{A}$ is $\mathcal{E}_0$-projective (since $\mathcal{E}_0$ is the class of split epimorphisms in $[\mathfrak{U}_d, \mathfrak{A}]$, every object is projective). Thus, since $(L_n^{\mathcal{E}_1} \widetilde{J})$ is additive and $\mathfrak{A}$ has exact coproducts, it is enough, by Theorem 4.1 and Corollary 5.4, to prove the assertion for

$$R = \widetilde{K}_U A: \mathfrak{U} \rightarrow \mathfrak{A},$$

where $A = A_U$ is an arbitrary object of $\mathfrak{A}$ and $\widetilde{K}_U$ is the Kan extension along $K_U: 1 \rightarrow \mathfrak{U}$.

Now choose a projective resolution of $A$ in $\mathfrak{A}$:

$$P: \cdots \rightarrow P_n \rightarrow P_{n-1} \rightarrow \cdots \rightarrow P_0 \twoheadrightarrow A.$$

Since coproducts are exact in $\mathfrak{A}$, applying the functor $\widetilde{K}_U$ preserves exactness, and we obtain a resolution

$$\widetilde{K}_U P: \cdots \rightarrow \widetilde{K}_U P_n \rightarrow \widetilde{K}_U P_{n-1} \rightarrow \cdots \rightarrow \widetilde{K}_U P_0 \twoheadrightarrow \widetilde{K}_U A.$$

Each $\widetilde{K}_U P_n$ is $\mathcal{E}_1$-projective (by Corollary 5.4, it is a coproduct of projectives), so this is an $\mathcal{E}_1$-projective resolution of $R = \widetilde{K}_U A$.

Now apply $\widetilde{J}$ to this resolution. By Proposition 5.2 (or more precisely, the explicit formula (5.14) in the text),

$$\widetilde{J}(\widetilde{K}_U P_n) = \widetilde{K}_{JU} P_n,$$

which has trivial derived functors: $(L_m^{\mathcal{E}_1} \widetilde{J})(\widetilde{K}_U P_n) = 0$ for all $m \geq 1$ (each is projective, hence acyclic). Thus the complex $\widetilde{J}(\widetilde{K}_U P)$ is an $\mathcal{E}_1$-acyclic resolution of $\widetilde{J}(\widetilde{K}_U A)$. Consequently,

$$(L_n^{\mathcal{E}_1} \widetilde{J})(\widetilde{K}_U A) = H_n\bigl(\widetilde{J}(\widetilde{K}_U P)\bigr) = 0, \quad n \geq 1.$$

By additivity and the reduction step, the same vanishing holds for any $\mathcal{E}_0$-projective $R$. $\square$
