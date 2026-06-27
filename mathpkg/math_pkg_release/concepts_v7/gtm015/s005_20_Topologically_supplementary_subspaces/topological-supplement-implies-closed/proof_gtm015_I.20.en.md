---
role: proof
locale: en
of_concept: topological-supplement-implies-closed
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Topological Supplement Implies Closed

Let $E$ be a separated TVS and let $M$ be a linear subspace of $E$ that possesses a topological supplement $N$. Then $E$ is the topological direct sum of $M$ and $N$.

By Theorem (20.6), the projector $p: E \to E$ onto $M$ along $N$ is continuous. Moreover, $\operatorname{Im}(p) = M$ and $\operatorname{Ker}(p) = N$.

Consider the continuous mapping $\varphi: E \to E$ defined by $\varphi(x) = x - p(x)$. Since $\{\theta\}$ is closed in $E$ (because $E$ is separated, every singleton, in particular $\{\theta\}$, is closed), the inverse image

$$\varphi^{-1}(\{\theta\}) = \{x \in E : x - p(x) = \theta\} = \{x \in E : p(x) = x\} = \operatorname{Im}(p) = M$$

is closed in $E$. Thus $M$ is a closed subspace of $E$. $\square$

**Remark.** The contrapositive is also useful: if $M$ is a non-closed linear subspace of a separated TVS $E$, then $M$ cannot have a topological supplement in $E$. Note, however, that even in a Banach space, there may exist *closed* linear subspaces without topological supplements (see (20.10)).
