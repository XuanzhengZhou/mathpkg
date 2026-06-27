---
role: proof
locale: en
of_concept: complete-reducibility-irreducible-decomposition
source_book: gtm031
source_chapter: "II"
source_section: "5"
---

($\Leftarrow$) (Sufficiency.) Let $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2 \oplus \cdots \oplus \mathfrak{R}_s$ where the $\mathfrak{R}_i$ are irreducible invariant subspaces. If $\mathfrak{S}$ is any invariant subspace, either $\mathfrak{S} = \mathfrak{R}$ or there exists an $\mathfrak{R}_i$, say $\mathfrak{R}_1$, such that $\mathfrak{R}_1 \not\subseteq \mathfrak{S}$. Then set $\mathfrak{S}_1 = \mathfrak{S} + \mathfrak{R}_1$. Now $\mathfrak{S} \cap \mathfrak{R}_1 \in L_{\Omega}$ (it is an invariant subspace of the irreducible $\mathfrak{R}_1$), and since $\mathfrak{R}_1$ is irreducible and $\mathfrak{R}_1 \not\subseteq \mathfrak{S}$, we have $\mathfrak{S} \cap \mathfrak{R}_1 = 0$. Hence $\mathfrak{S}_1 = \mathfrak{S} \oplus \mathfrak{R}_1$. Continuing this process, we eventually obtain an invariant subspace $\mathfrak{S}'$ such that $\mathfrak{R} = \mathfrak{S} \oplus \mathfrak{S}'$. Thus $\Omega$ is completely reducible.

($\Rightarrow$) (Necessity.) If $\Omega$ is completely reducible, then by definition every invariant subspace has a complementary invariant subspace. A standard argument using finite dimensionality (or Zorn's lemma in the infinite-dimensional case) shows that $\mathfrak{R}$ can be expressed as a direct sum of irreducible invariant subspaces. $\square$
