---
role: proof
locale: en
of_concept: regular-open-sets-in-density-topology
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

**($\Rightarrow$)** If $A \in S$, then $\phi(A)$ is a basic open set, hence open in $\mathcal{T}$. By Theorem 22.6, the closure of $\phi(A)$ is of the form $\phi(A) \cup N$ for some $N \in \mathcal{N}$. We claim that $\phi(A)$ is the largest open subset of its closure, i.e., $\phi(A)$ equals the interior of its closure (which is the definition of a regular open set).

Let $\phi(A_1) - N_1$ be any open subset of $\phi(A) \cup N$. Then
$$\phi(A_1) - N_1 \subset \phi(A_1) = \phi(\phi(A_1) - N_1) \subset \phi(\phi(A) \cup N) = \phi(A).$$
The last equality uses the properties of the lower density: since $\phi(A) \cup N \sim \phi(A)$ (they differ by a nullset $N$), we have $\phi(\phi(A) \cup N) = \phi(\phi(A)) = \phi(A)$ by property (2) and the fact that $\phi$ is idempotent on its image. Thus $\phi(A)$ contains every open subset of $\phi(A) \cup N$, so $\phi(A)$ is exactly the interior of its closure. Hence $\phi(A)$ is regular open.

**($\Leftarrow$)** Conversely, if $G$ is regular open, then $G$ is open in $\mathcal{T}$, so $G = \phi(B) - N$ for some $B \in S$ and $N \in \mathcal{N}$. Since $\phi(B) \triangle (\phi(B) - N) \subset N$, we have $\phi(B) \sim \phi(B) - N = G$. By Theorem 22.6, $G$ and $\phi(B)$ differ by a nowhere dense set (a nullset), and both are regular open sets. Two regular open sets that differ by a nowhere dense set must be equal. Therefore $G = \phi(B)$ for $B \in S$.
