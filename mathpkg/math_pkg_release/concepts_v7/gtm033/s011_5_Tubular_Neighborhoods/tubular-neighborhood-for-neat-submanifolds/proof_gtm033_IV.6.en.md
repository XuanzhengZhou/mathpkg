---
role: proof
locale: en
of_concept: tubular-neighborhood-for-neat-submanifolds
source_book: gtm033
source_chapter: "IV"
source_section: "6"
---

# Proof of Tubular Neighborhood for Neat Submanifolds (Theorem 6.3)

**Theorem (6.3).** Let $M \subset V$ be a neat submanifold. Then $M$ has a tubular neighborhood in $V$.

*Proof.* By Theorem 6.2 there is a neighborhood $N \subset V$ of $\partial V$ and a diffeomorphism

$$\varphi: (N, \partial V \cap N) \to (\partial V \times [0, \infty), \partial V \times \{0\})$$

which restricts to a collar on $\partial M$ in $M$. This means that near $\partial V$, the pair $(V, M)$ looks like $(\partial V \times [0, \infty), \partial M \times [0, \infty))$.

Now embed $N$ as a neat submanifold of the upper half-space $\mathbb{R}_+^q$, with $\partial V$ mapping into $\mathbb{R}^{q-1} \times \{0\}$ and meeting it orthogonally. We can extend this embedding of $N$ to an embedding of all of $V$ in $\mathbb{R}_+^q$. Thus $V$ is now a neat submanifold of $\mathbb{R}_+^q$, and both $V$ and $M$ meet $\mathbb{R}^{q-1} \times \{0\}$ orthogonally along $\partial V$ and $\partial M$ (Figure 4-2).

We can now find a normal tubular neighborhood of $V$ in $\mathbb{R}_+^q$ (Figure 4-3). Since $M$ is a neat submanifold of $V$, restricting this normal tubular neighborhood to $M$ and composing with a smooth retraction $V \to V$ (adapted to the boundary, as in the proof of Theorem 5.2) yields a tubular neighborhood of $M$ in $V$. The rest of the proof proceeds exactly as in the proof of Theorem 5.2. ∎
