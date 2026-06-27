---
role: proof
locale: en
of_concept: topological-direct-sum-via-continuous-projector
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Topological Direct Sum via Continuous Projector

Let $E$ be a TVS and let $M, N$ be supplementary linear subspaces of $E$. Let $p: E \to E$ be the projector onto $M$ along $N$, defined by $p(y + z) = y$ for all $y \in M$, $z \in N$ (see Definition (20.4)). Then $p$ is linear, $p^2 = p$, $\operatorname{Im}(p) = M$, and $\operatorname{Ker}(p) = N$.

**Theorem.** $E$ is the topological direct sum of $M$ and $N$ if and only if the projector $p$ is continuous.

*Proof.* Recall that by definition, $E$ is the topological direct sum of $M$ and $N$ precisely when the natural continuous linear bijection $T: M \times N \to E$, $T(y, z) = y + z$, is a homeomorphism (i.e., $T^{-1}$ is continuous).

Now, for the projector $p$ defined above, we have $p(x) = y$ where $x = y + z$ is the unique decomposition of $x$ with $y \in M$, $z \in N$. But then $x - p(x) = z$ is the projection onto $N$ along $M$.

($\Rightarrow$) If $E$ is the topological direct sum of $M$ and $N$, then by Theorem (20.3), condition (b), the mapping $x \mapsto y = p(x)$ is continuous. So $p$ is continuous.

($\Leftarrow$) Conversely, if $p$ is continuous, then the mapping $x \mapsto p(x)$ is continuous, which is condition (b) of Theorem (20.3). By the equivalence established in (20.3), $E$ is the topological direct sum of $M$ and $N$. $\square$
