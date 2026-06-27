---
role: proof
locale: en
of_concept: density-topology
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

To prove that $\mathcal{T}$ is a topology, we must show it is closed under arbitrary unions. Let $\{A_{\alpha} - N_{\alpha} : \alpha \in \Gamma\}$ be any subfamily of $\mathcal{T}$, where each $A_{\alpha} \in S$ and $N_{\alpha} \in \mathcal{N}$. Let $b$ denote the least upper bound of the measures of finite unions of members of $\{A_{\alpha}\}$, and choose a sequence $\{\alpha_n\}$ such that $\mu\left(\bigcup_{n=1}^{\infty} A_{\alpha_n}\right) = b$. Put $A = \bigcup_{n=1}^{\infty} A_{\alpha_n}$. Then $A \in S$, and the definition of $b$ implies that $A_{\alpha} - A \in \mathcal{N}$ for every $\alpha \in \Gamma$.

Since

$$A_{\alpha} - (A_{\alpha} - A) \subset A,$$

it follows from properties (2) and (5) of the lower density that

$$\phi(A_{\alpha}) \subset \phi(A) \quad \text{for every } \alpha.$$

Putting

$$N_0 = \bigcup_{n=1}^{\infty} \left[ N_{\alpha_n} \cup \left(A_{\alpha_n} - \phi(A_{\alpha_n})\right) \right],$$

we have $N_0 \in \mathcal{N}$ and

$$A - N_0 \subset \bigcup_{n=1}^{\infty} \left[ \phi(A_{\alpha_n}) - N_{\alpha_n} \right] \subset \bigcup_{\alpha \in \Gamma} \left[ \phi(A_{\alpha}) - N_{\alpha} \right] \subset \phi(A).$$

The extremes differ by a nullset, and therefore

$$\bigcup_{\alpha \in \Gamma} \left[ \phi(A_{\alpha}) - N_{\alpha} \right] = \phi(A) - N$$

for some $N \in \mathcal{N}$, by the completeness of $\mu$. This shows that arbitrary unions of members of $\mathcal{T}$ belong to $\mathcal{T}$. The verification that finite intersections belong to $\mathcal{T}$ follows from property (4) of the lower density.
