---
role: proof
locale: en
of_concept: kan-extension-full-embedding
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Kan Extension Along a Full Embedding is Trivial

**Proposition 5.2.** Let $J: \mathfrak{U} \rightarrow \mathfrak{B}$ be a full embedding. Then for any $T: \mathfrak{U} \rightarrow \mathfrak{A}$, the restriction of $\widetilde{J}T$ along $J$ is naturally isomorphic to $T$; i.e., $\widetilde{J}T \circ J \cong T$.

**Proof.** Let $U \in \mathfrak{U}$ and consider the category $\mathfrak{J}_{JU}$. There is a subcategory of $\mathfrak{J}_{JU}$ consisting of just the object $(U, 1_{JU})$ and its identity morphism. Now, given any object $(U_1, \psi_1)$ of $\mathfrak{J}_{JU}$, there is a unique morphism $\varphi: (U_1, \psi_1) \rightarrow (U, 1_{JU})$ with $J\varphi = \psi_1$, since $J$ is a full embedding. Indeed, fullness of $J$ provides a morphism $\varphi: U_1 \rightarrow U$ in $\mathfrak{U}$ such that $J\varphi = \psi_1$, and faithfulness guarantees uniqueness.

It is then obvious that $\varinjlim_{\mathfrak{J}_{JU}} T_{JU}$ is just $TU$, with

$$\varrho_{JU}(U_1, \psi_1) = T(\varphi).$$

Thus the colimit reduces to evaluation at the terminal object $(U, 1_{JU})$, and we obtain a natural isomorphism

$$\widetilde{J}T(JU) \cong T(U)$$

for all $U \in \mathfrak{U}$. This isomorphism is natural in $U$, so $\widetilde{J}T \circ J \cong T$ as functors. $\square$

**Remark.** We have, in this proof, a very special case of a *cofinal functor*, namely the embedding of the object $(U, 1_{JU})$ into $\mathfrak{J}_{JU}$; it is a general fact that colimits are invariant under cofinal functors in the sense that $\varinjlim T \cong \varinjlim TK$, where $K: \mathfrak{C} \rightarrow \mathfrak{D}$ is a cofinal functor of small categories and $T: \mathfrak{D} \rightarrow \mathfrak{A}$. For the definition of a cofinal functor, generalizing the notion of a cofinal subset of a directed set, see Exercise 5.4.
