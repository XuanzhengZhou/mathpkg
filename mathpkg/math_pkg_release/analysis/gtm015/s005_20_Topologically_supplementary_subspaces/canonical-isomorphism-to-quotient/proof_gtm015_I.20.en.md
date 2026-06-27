---
role: proof
locale: en
of_concept: canonical-isomorphism-to-quotient
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Canonical Isomorphism of Supplement onto Quotient

Let $E$ be a vector space and let $M, N$ be supplementary linear subspaces of $E$, so that $E = M + N$ and $M \cap N = \{\theta\}$.

Let $\pi: E \to E/M$ be the canonical quotient mapping, and let $\pi_0 = \pi|_N$ be the restriction of $\pi$ to $N$. We claim that $\pi_0: N \to E/M$ is a vector space isomorphism.

**Surjectivity.** Given any coset $x + M \in E/M$, write $x = y + z$ with $y \in M$, $z \in N$ (possible since $E = M + N$). Then $x + M = (y + z) + M = z + M = \pi_0(z)$. Hence $\pi_0$ is surjective.

**Injectivity.** Suppose $\pi_0(z) = M$ (the zero coset) for some $z \in N$. Then $z \in M$, so $z \in M \cap N = \{\theta\}$, whence $z = \theta$. Thus $\pi_0$ is injective.

Therefore $\pi_0: N \to E/M$ is a vector space isomorphism.

If, in addition, $E$ is a TVS, then $\pi_0$ is continuous: $\pi$ is continuous by definition of the quotient topology, and the inclusion $N \hookrightarrow E$ is continuous for the relative topology on $N$; $\pi_0$ is the composition of these two continuous maps.

For $\pi_0$ to be a *bicontinuous* isomorphism (i.e., a TVS isomorphism between $N$ and $E/M$), it is necessary and sufficient that the direct sum $E = M \oplus N$ be topological; this is the content of Theorem (20.9). $\square$
