---
role: proof
locale: en
of_concept: density-topology-construction
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

Let $(X, S, \mu)$ be a complete finite measure space and $\phi$ a lower density on $X$. Let $\mathcal{N} = \{N \in S : \mu(N) = 0\}$. For each $A \in S$ and $N_A \in \mathcal{N}$, define the basic open set $\phi(A) \setminus N_A$. We must verify that these sets form a base for a topology.

First, note that $X = \phi(X) \setminus \emptyset$ belongs to the family. If $\phi(A_1) \setminus N_1$ and $\phi(A_2) \setminus N_2$ are two basic sets, then using properties (4) and (5) of the lower density,
$$(\phi(A_1) \setminus N_1) \cap (\phi(A_2) \setminus N_2) = \phi(A_1 \cap A_2) \setminus (N_1 \cup N_2),$$
which is again a basic set. Thus the family is closed under finite intersections and forms a base for a topology $\mathcal{T}$.

The key technical step is to show that the union of any family of basic open sets is measurable and can be expressed appropriately. Let $\{\phi(A_\alpha) \setminus N_\alpha\}_{\alpha \in \Gamma}$ be any subfamily of $\mathcal{T}$. Let $b$ be the least upper bound of the measures of finite unions of the $A_\alpha$, and choose a sequence $\{\alpha_n\}$ such that
$$\mu\left(\bigcup_{n=1}^{\infty} A_{\alpha_n}\right) = b.$$
Put $A = \bigcup_{n=1}^{\infty} A_{\alpha_n}$. Then $A \in S$, and the definition of $b$ implies that $A_\alpha \setminus A \in \mathcal{N}$ for every $\alpha \in \Gamma$.

Since $A_\alpha \setminus (A_\alpha \setminus A) \subset A$, it follows from properties (2) and (5) of the lower density that
$$\phi(A_\alpha) \subset \phi(A) \quad \text{for every } \alpha \in \Gamma.$$

Now define
$$N_0 = \bigcup_{n=1}^{\infty} \left[ N_{\alpha_n} \cup (A_{\alpha_n} \setminus \phi(A_{\alpha_n})) \right].$$
Since each $A_{\alpha_n} \triangle \phi(A_{\alpha_n})$ is a nullset (by property (1)), $N_0 \in \mathcal{N}$. Then
$$A \setminus N_0 \subset \bigcup_{n=1}^{\infty} \left[ \phi(A_{\alpha_n}) \setminus N_{\alpha_n} \right] \subset \bigcup_{\alpha \in \Gamma} \left[ \phi(A_\alpha) \setminus N_\alpha \right] \subset \phi(A).$$

The extremes differ by a nullset, and therefore by the completeness of $\mu$,
$$\bigcup_{\alpha \in \Gamma} \left[ \phi(A_\alpha) \setminus N_\alpha \right] = \phi(A) \setminus N$$
for some $N \in \mathcal{N}$. This shows that the union of any family of basic open sets is again an element of the base (up to a nullset adjustment), establishing that we have indeed defined a topology.

With this topology, Theorems 22.6, 22.7, and 22.8 below characterize the nowhere dense sets, Baire-property sets, and regular open sets, confirming that $\mu$ is a category measure in $(X, \mathcal{T})$.
