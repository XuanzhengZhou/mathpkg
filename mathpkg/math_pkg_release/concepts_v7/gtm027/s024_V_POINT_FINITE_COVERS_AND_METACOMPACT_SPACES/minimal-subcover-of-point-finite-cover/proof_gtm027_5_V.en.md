---
role: proof
locale: en
of_concept: minimal-subcover-of-point-finite-cover
source_book: gtm027
source_chapter: "5"
source_section: "V. Point Finite Covers and Metacompact Spaces"
---

# Proof of Minimal Subcover of a Point Finite Cover

Let $\mathcal{U}$ be a point finite cover of a set $X$. We prove that $\mathcal{U}$ has a minimal subcover, that is, a subcover no proper subfamily of which is a cover.

Consider the family $\mathcal{S}$ of all subfamilies of $\mathcal{U}$ that cover $X$. This family is non-empty since $\mathcal{U} \in \mathcal{S}$. Partially order $\mathcal{S}$ by reverse inclusion: $\mathcal{V}_1 \leq \mathcal{V}_2$ if $\mathcal{V}_2 \subseteq \mathcal{V}_1$. To apply Zorn's Lemma, let $\mathcal{C}$ be a chain in $\mathcal{S}$.

Let $\mathcal{V}^* = \bigcap \mathcal{C}$. We claim $\mathcal{V}^*$ covers $X$. Suppose $x \in X$. Since $\mathcal{U}$ is point finite, $x$ belongs to only finitely many members of $\mathcal{U}$, say $U_1, \ldots, U_n$. Since each $\mathcal{V} \in \mathcal{C}$ covers $X$, for each $\mathcal{V}$ there is some $i$ such that $U_i \in \mathcal{V}$. By the finite intersection property of the chain (the sets of indices being finite), there exists some $i_0$ such that $U_{i_0} \in \mathcal{V}$ for cofinally many (hence all) $\mathcal{V} \in \mathcal{C}$. Therefore $U_{i_0} \in \mathcal{V}^*$, so $\mathcal{V}^*$ covers $X$.

Thus $\mathcal{V}^* \in \mathcal{S}$ and $\mathcal{V}^* \leq \mathcal{V}$ for all $\mathcal{V} \in \mathcal{C}$, so every chain has a lower bound. By Zorn's Lemma, $\mathcal{S}$ contains a minimal element, which is precisely a minimal subcover of $\mathcal{U}$.
