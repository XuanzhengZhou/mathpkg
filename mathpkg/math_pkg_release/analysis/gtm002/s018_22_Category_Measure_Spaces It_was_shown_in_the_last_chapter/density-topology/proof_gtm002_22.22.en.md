---
role: proof
locale: en
of_concept: density-topology
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

We need to verify that $\mathcal{T}$ is a topology, i.e., closed under finite intersections and arbitrary unions.

**Finite intersections.** Let $\phi(A_1) - N_1$ and $\phi(A_2) - N_2$ be basic open sets. Using property (4) of the lower density,
$$(\phi(A_1) - N_1) \cap (\phi(A_2) - N_2) = \phi(A_1) \cap \phi(A_2) - (N_1 \cup N_2) = \phi(A_1 \cap A_2) - (N_1 \cup N_2),$$
which is again a basic open set since $A_1 \cap A_2 \in S$ and $N_1 \cup N_2 \in \mathcal{N}$.

**Arbitrary unions.** Let $\{\phi(A_\alpha) - N_\alpha : \alpha \in \Gamma\}$ be any family of basic open sets. Let $b$ be the least upper bound of the measures of finite unions of the sets $A_\alpha$, and choose a sequence $\{\alpha_n\}$ such that
$$\mu\left(\bigcup_{n=1}^{\infty} A_{\alpha_n}\right) = b.$$
Put $A = \bigcup_{n=1}^{\infty} A_{\alpha_n}$. Then $A \in S$, and the definition of $b$ implies that $A_\alpha - A \in \mathcal{N}$ for every $\alpha \in \Gamma$. Since
$$A_\alpha - (A_\alpha - A) \subset A,$$
it follows from properties (2) and (5) that
$$\phi(A_\alpha) \subset \phi(A) \quad \text{for every } \alpha.$$
Putting
$$N_0 = \bigcup_{n=1}^{\infty} \left[ N_{\alpha_n} \cup \left(A_{\alpha_n} - \phi(A_{\alpha_n})\right) \right],$$
we have $N_0 \in \mathcal{N}$ and
$$A - N_0 \subset \bigcup_{n=1}^{\infty} \left[ \phi(A_{\alpha_n}) - N_{\alpha_n} \right] \subset \bigcup_{\alpha \in \Gamma} \left[ \phi(A_\alpha) - N_\alpha \right] \subset \phi(A).$$
The extremes differ by a nullset, and therefore
$$\bigcup_{\alpha \in \Gamma} \left[ \phi(A_\alpha) - N_\alpha \right] = \phi(A) - N$$
for some $N \in \mathcal{N}$, by the completeness of $\mu$. Thus arbitrary unions of basic open sets are open, and $\mathcal{T}$ is indeed a topology.

That $\mu$ is a category measure relative to $\mathcal{T}$ follows from Theorems 22.6-22.8 below.
