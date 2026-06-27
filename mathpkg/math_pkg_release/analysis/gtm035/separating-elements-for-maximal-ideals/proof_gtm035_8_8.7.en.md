---
role: proof
locale: en
of_concept: separating-elements-for-maximal-ideals
source_book: gtm035
source_chapter: "8"
source_section: "8.7"
---

# Proof of Existence of Elements Separating Pairs of Maximal Ideals

**Lemma 8.7.** Let $\mathfrak{A}$ be a commutative Banach algebra, $\mathcal{M}$ its maximal ideal space, and $\mathcal{M}_1, \mathcal{M}_2$ two disjoint closed subsets of $\mathcal{M}$. Then there exist finitely many elements $a_1, \ldots, a_N \in \mathfrak{A}$ such that the map

$$\hat{a} : \mathcal{M} \to \mathbb{C}^N, \quad M \mapsto (\hat{a}_1(M), \ldots, \hat{a}_N(M))$$

satisfies $\hat{a}(\mathcal{M}_1) \cap \hat{a}(\mathcal{M}_2) = \emptyset$.

**Proof.** (This proof follows the same pattern as that of Lemma 8.5.) Consider the compact product space $\mathcal{M}_1 \times \mathcal{M}_2$. For each point $x = (M, M') \in \mathcal{M}_1 \times \mathcal{M}_2$, we have $M \neq M'$ (since $\mathcal{M}_1 \cap \mathcal{M}_2 = \emptyset$). Because the Gelfand transform $\hat{\cdot} : \mathfrak{A} \to C(\mathcal{M})$ separates points of $\mathcal{M}$ (in the semisimple case; if $\mathfrak{A}$ has a nontrivial radical, the Gelfand transform still separates the maximal ideals: distinct maximal ideals correspond to distinct multiplicative linear functionals, so there exists $b_x \in \mathfrak{A}$ such that the evaluation of these functionals differs), there exists an element $b_x \in \mathfrak{A}$ with

$$\widehat{b_x}(M) \neq \widehat{b_x}(M').$$

Equivalently, $\widehat{b_x}(M) - \widehat{b_x}(M') \neq 0$.

By continuity of the function $(M, M') \mapsto \widehat{b_x}(M) - \widehat{b_x}(M')$ on $\mathcal{M} \times \mathcal{M}$, there exists a neighborhood $N_x$ of $(M, M')$ in $\mathcal{M}_1 \times \mathcal{M}_2$ such that

$$\widehat{b_x}(P) - \widehat{b_x}(P') \neq 0 \quad \text{for all } (P, P') \in N_x.$$

The family $\{N_x \mid x \in \mathcal{M}_1 \times \mathcal{M}_2\}$ is an open cover of the compact space $\mathcal{M}_1 \times \mathcal{M}_2$. By compactness, there exist finitely many points $x_1, \ldots, x_k \in \mathcal{M}_1 \times \mathcal{M}_2$ such that

$$\mathcal{M}_1 \times \mathcal{M}_2 \subset N_{x_1} \cup \cdots \cup N_{x_k}.$$

Set $a_j = b_{x_j}$ for $j = 1, \ldots, k$ and let $N = k$. We claim that the map

$$\hat{a} : \mathcal{M} \to \mathbb{C}^N, \quad M \mapsto (\hat{a}_1(M), \ldots, \hat{a}_N(M))$$

has the required property.

Suppose, for contradiction, that $\hat{a}(\mathcal{M}_1) \cap \hat{a}(\mathcal{M}_2) \neq \emptyset$. Then there exist $M \in \mathcal{M}_1$ and $M' \in \mathcal{M}_2$ such that $\hat{a}(M) = \hat{a}(M')$, i.e.,

$$\widehat{a_j}(M) = \widehat{a_j}(M') \quad \text{for all } j = 1, \ldots, N.$$

But $(M, M') \in \mathcal{M}_1 \times \mathcal{M}_2$, so $(M, M') \in N_{x_j}$ for some $j$. By definition of $N_{x_j}$, we would have $\widehat{a_j}(M) \neq \widehat{a_j}(M')$, a contradiction. Therefore $\hat{a}(\mathcal{M}_1) \cap \hat{a}(\mathcal{M}_2) = \emptyset$. $\square$

**Remark.** If $\mathfrak{A}$ is not semisimple, the same argument works because distinct maximal ideals (i.e., distinct points of $\mathcal{M}$) correspond to distinct multiplicative linear functionals $\varphi_M \neq \varphi_{M'}$, so there exists $a \in \mathfrak{A}$ with $\varphi_M(a) \neq \varphi_{M'}(a)$, which is precisely $\hat{a}(M) \neq \hat{a}(M')$. Semisimplicity is not required.
