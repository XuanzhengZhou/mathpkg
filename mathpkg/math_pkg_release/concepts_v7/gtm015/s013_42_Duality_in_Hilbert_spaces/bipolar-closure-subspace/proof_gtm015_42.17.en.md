---
role: proof
locale: en
of_concept: bipolar-closure-subspace
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.17"
---

# Proof of Bipolar of a Subset is the Smallest Closed Linear Subspace

**Theorem (Exercise 42.17).** If $S$ is any subset of a Hilbert space $H$, then $S^{\perp\perp}$ is the smallest closed linear subspace of $H$ that contains $S$.

*Proof.* First, $S^{\perp\perp}$ is a closed linear subspace of $H$: for any subset $T$, $T^\perp$ is always a closed linear subspace (the intersection of the kernels of the continuous linear forms $x \mapsto (x|t)$ for $t \in T$). Thus $S^{\perp\perp} = (S^\perp)^\perp$ is a closed linear subspace.

Moreover, $S \subset S^{\perp\perp}$ (by (42.8)): for any $s \in S$ and any $z \in S^\perp$, we have $(s|z) = 0$ by definition of $S^\perp$, hence $s \in (S^\perp)^\perp = S^{\perp\perp}$.

Now let $M$ be any closed linear subspace of $H$ such that $S \subset M$. Taking orthogonal complements (which reverses inclusion),

$$M^\perp \subset S^\perp.$$

Taking orthogonal complements once more,

$$S^{\perp\perp} \subset M^{\perp\perp}.$$

Since $M$ is a closed linear subspace, Theorem (42.9) gives $M^{\perp\perp} = M$. Therefore $S^{\perp\perp} \subset M$.

Thus $S^{\perp\perp}$ is a closed linear subspace containing $S$, and it is contained in every closed linear subspace that contains $S$. Hence $S^{\perp\perp}$ is the smallest closed linear subspace of $H$ containing $S$. (In fact, $S^{\perp\perp}$ is the closure of the linear span of $S$.)
