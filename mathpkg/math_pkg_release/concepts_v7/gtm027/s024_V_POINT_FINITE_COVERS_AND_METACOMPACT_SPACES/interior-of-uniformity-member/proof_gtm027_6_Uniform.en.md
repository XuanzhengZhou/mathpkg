---
role: proof
locale: en
of_concept: interior-of-uniformity-member
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof that the Interior of a Uniformity Member is in the Uniformity (Theorem 6.6)

**Theorem 6.6.** If $U$ is a member of the uniformity $\mathcal{U}$, then the interior of $U$ is also a member; consequently the family of all open symmetric members of $\mathcal{U}$ is a base for $\mathcal{U}$.

**Proof.** The interior of a subset $M$ of $X \times X$ (in the product topology induced by the uniform topology) is the set of all $(x,y)$ such that, for some $U$ and some $V$ in $\mathcal{U}$, $U[x] \times V[y] \subset M$. Since $U \cap V \in \mathcal{U}$, the interior of $M$ is

$$\text{int}(M) = \{(x,y) : V[x] \times V[y] \subset M \text{ for some } V \text{ in } \mathcal{U}\}.$$

If $U \in \mathcal{U}$, there is a symmetric member $V$ of $\mathcal{U}$ such that $V \circ V \circ V \subset U$. According to Lemma 6.1,

$$V \circ V \circ V = \bigcup \{V[x] \times V[y] : (x,y) \in V\}.$$

Hence every point $(x,y)$ of $V$ satisfies $V[x] \times V[y] \subset V \circ V \circ V \subset U$, so $(x,y)$ is an interior point of $U$. Since the interior of $U$ contains $V$, which is a member of $\mathcal{U}$, the interior of $U$ itself belongs to $\mathcal{U}$ (as it contains a member of $\mathcal{U}$).

Consequently, the family of all open symmetric members of $\mathcal{U}$ is a base: given any $U \in \mathcal{U}$, take $V \in \mathcal{U}$ symmetric with $V \circ V \subset U$, then the interior of $V$ is open, symmetric, and contained in $U$.
