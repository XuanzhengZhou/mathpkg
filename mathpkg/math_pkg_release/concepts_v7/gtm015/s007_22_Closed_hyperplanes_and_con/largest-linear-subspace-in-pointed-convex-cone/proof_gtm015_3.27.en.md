---
role: proof
locale: en
of_concept: largest-linear-subspace-in-pointed-convex-cone
source_book: gtm015
source_chapter: "3"
source_section: "27"
---

# Proof of Largest linear subspace contained in a pointed convex cone

If $A$ is a pointed convex cone in $E$, then $A \cap (-A)$ is a linear subspace of $E$; it is the largest linear subspace contained in $A$.

Let $N = A \cap (-A)$. Since $A$ is pointed, $\theta \in N$. Obviously $-N = N$, i.e., $N$ contains negatives. If $\alpha > 0$ then $\alpha N \subset A \cap (-A) = N$ (since $A$ and $-A$ are both cones). For $\alpha < 0$, $\alpha N = (-\alpha)(-N) \subset N$. Thus $\lambda N \subset N$ for all scalars $\lambda$. Finally, $N + N \subset A + A \subset A$ (since $A$ is a convex cone) and $N + N \subset (-A) + (-A) \subset -A$, so $N + N \subset A \cap (-A) = N$. Thus $N$ is a linear subspace.

If $M$ is any linear subspace contained in $A$, then $M = -M \subset -A$, so $M \subset A \cap (-A) = N$. Thus $N$ is the largest linear subspace in $A$.
