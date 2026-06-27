---
role: proof
locale: en
of_concept: compactness-theorem
source_book: gtm053
source_chapter: "2"
source_section: "2.1"
---

The first proof is an application of Godel's completeness theorem II.6.2 and uses the deduction system of II.2.2--II.2.5. By Lemma 2.2, the finitely satisfiable set $E$ is consistent. By Godel's completeness theorem, every consistent set of $L$-sentences is satisfiable; hence $E$ is satisfiable. Moreover, the model constructed in the completeness proof (or equivalently via the Lowenheim-Skolem theorem) has cardinality at most $|L| + \aleph_0$.

All three proofs of the compactness theorem use the axiom of choice; the construction of the model is in general ineffective.

The second proof (Henkin's method) proceeds via Lemma 2.6: one extends the language $L$ to $\tilde{L}$ with $|\tilde{L}| = |L| + \aleph_0$ and extends $E$ to a complete finitely satisfiable set $\tilde{\mathcal{E}}$ of $\tilde{L}$-sentences with witnesses. The term model built from $\tilde{\mathcal{E}}$ then satisfies $\tilde{\mathcal{E}}$, and its reduct to $L$ satisfies $E$, with cardinality bounded by $|\tilde{L}| = |L| + \aleph_0$.

The third proof uses ultraproducts (see Los's theorem, 2.10). For each finite subset $E_0 \subseteq E$, choose a model $\mathbf{A}_{E_0} \models E_0$. Let $I$ be the set of all finite subsets of $E$, and for each $i \in I$ define $J_i = \{j \in I : i \subseteq j\}$. The family $\{J_i : i \in I\}$ has the finite intersection property, so it extends to an ultrafilter $U$ on $I$. By Los's theorem, the ultraproduct $\prod_{i \in I} \mathbf{A}_i / U$ satisfies $E$. Its cardinality is bounded by $(\sup_i |A_i|)^{|I|} \leq \aleph_0^{|E|}$, and with a more careful choice of models one obtains cardinality $\leq |L| + \aleph_0$.
