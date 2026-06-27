---
role: proof
locale: en
of_concept: minimal-cogenerator-noetherian-test
source_book: gtm013
source_chapter: "7"
source_section: "25. Injective Modules and Noetherian Rings—The Faith–Walker Theorems"
---

(a) $\Rightarrow$ (c). If $R$ is left noetherian, then by (18.13) every direct sum of injective left $R$-modules is injective. Since the minimal cogenerator $C_0$ is injective, it follows that $C_0^{(A)}$ is injective for every set $A$.

(c) $\Rightarrow$ (b). This implication is immediate, as $\mathbb{N}$ is a particular set.

(b) $\Rightarrow$ (a). Assume that $C_0^{(\mathbb{N})}$ is injective. Recall from (18.16) that $C_0 = \bigoplus_{T \in \mathcal{S}} E(T)$ where $\mathcal{S}$ is an irredundant set of representatives of the simple left $R$-modules. If $I$ is any left ideal of $R$, then by Lemma 25.2, $I$ is a $C_0$-annihilator left ideal (since $C_0$ cogenerates every left $R$-module). Thus every left ideal of $R$ belongs to $\mathcal{L}_R(C_0)$. Now apply Theorem 25.1 with $E = C_0$: the hypothesis that $C_0^{(\mathbb{N})}$ is injective (condition (c) of 25.1) implies that the $C_0$-annihilator left ideals satisfy the ascending chain condition (condition (b) of 25.1). Since every left ideal is a $C_0$-annihilator left ideal, $R$ satisfies the ascending chain condition on left ideals; i.e., $R$ is left noetherian.
