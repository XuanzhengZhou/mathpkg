---
role: proof
locale: en
of_concept: local-ring-inclusion-implies-equality
source_book: gtm052
source_chapter: "I"
source_section: "6"
---

**Proof.** Embed $Y$ in $\mathbf{P}^n$ for some $n$. Replacing $Y$ by its closure, we may assume $Y$ is projective. After a suitable linear change of coordinates in $\mathbf{P}^n$, we may assume that neither $P$ nor $Q$ is in the hyperplane $H_0$ defined by $x_0 = 0$. Thus $P, Q \in Y \cap (\mathbf{P}^n - H_0)$ which is affine, so we may assume that $Y$ is an affine variety.

Let $A$ be the affine coordinate ring of $Y$. Then there are maximal ideals $\mathfrak{m}, \mathfrak{n} \subseteq A$ such that $\mathcal{O}_P = A_{\mathfrak{m}}$ and $\mathcal{O}_Q = A_{\mathfrak{n}}$. If $\mathcal{O}_Q \subseteq \mathcal{O}_P$, we must have $\mathfrak{m} \subseteq \mathfrak{n}$. But $\mathfrak{m}$ is a maximal ideal, so $\mathfrak{m} = \mathfrak{n}$, and hence $P = Q$.
