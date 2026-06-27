---
role: proof
locale: en
of_concept: double-orthogonal-complement
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.9"
---

# Proof of Double Orthogonal Complement of a Closed Subspace

**Theorem.** If $N$ is a closed linear subspace of a Hilbert space $H$, then $N^{\perp\perp} = N$.

*Proof.* First, the inclusion $N \subset N^{\perp\perp}$ holds for any subset $N$ (42.8): if $y \in N$, then for every $z \in N^\perp$ we have $(y|z) = 0$, which means $y \in (N^\perp)^\perp = N^{\perp\perp}$.

For the reverse inclusion, let $x \in N^{\perp\perp}$. By the orthogonal decomposition theorem (42.7), write $x = y + z$ with $y \in N$ and $z \in N^\perp$. Since $y \in N \subset N^{\perp\perp}$ (by the first paragraph) and $x \in N^{\perp\perp}$, we have

$$z = x - y \in N^{\perp\perp}$$

because $N^{\perp\perp}$ is a linear subspace. But $z \in N^\perp$ by construction. Thus $z \in N^\perp \cap N^{\perp\perp}$, which means $z$ is orthogonal to every vector in $N^\perp$ and in particular $z$ is orthogonal to itself: $(z|z) = 0$. Hence $z = \theta$ and $x = y \in N$.

Therefore $N^{\perp\perp} = N$.
