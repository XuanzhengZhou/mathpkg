---
role: proof
locale: en
of_concept: regular-open-via-density
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

If $A \in S$, then $\phi(A)$ is open in $\mathcal{T}$, and the closure of $\phi(A)$ is of the form $\phi(A) \cup N$ for some $N \in \mathcal{N}$, by Theorem 22.6. Let $\phi(A_1) - N_1$ be any open subset of $\phi(A) \cup N$. Then

$$\phi(A_1) - N_1 \subset \phi(A_1) = \phi(\phi(A_1) - N_1) \subset \phi(\phi(A) \cup N) = \phi(A).$$

Thus $\phi(A)$ is the largest open subset of $\phi(A) \cup N = \overline{\phi(A)}$. This shows that $\phi(A)$ is equal to the interior of its closure, that is, $\phi(A)$ is regular open.

Conversely, suppose $G$ is regular open. By definition of the topology, $G = \phi(A) - N$ for some $A \in S$ and $N \in \mathcal{N}$. Since $\phi(A) \triangle [\phi(A) - N]$ is contained in $N$, we have $\phi(A) \sim \phi(A) - N = G$. But $G$ and $\phi(A)$ both differ from each other by a nowhere dense set, and both are regular open. For regular open sets, $G \sim \phi(A)$ and both being regular open forces $G = \phi(A)$, since two distinct regular open sets cannot differ by only a nowhere dense set. Therefore $G = \phi(A)$ for some $A \in S$.
