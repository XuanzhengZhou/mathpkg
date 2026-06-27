---
role: proof
locale: en
of_concept: nowhere-dense-sets-in-density-topology
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

**($\Leftarrow$)** If $N \in \mathcal{N}$, then $N$ is a nullset. Consider any nonempty basic open set $\phi(A) - N_1$ (where $A \in S$, $N_1 \in \mathcal{N}$). We show $N$ is not dense in $\phi(A) - N_1$. Note that $X - N = \phi(X) - N$ is a basic open set. If $\phi(A) - N_1 \neq \emptyset$, then $\mu(\phi(A) - N_1) > 0$. But $\mu(N) = 0$, so $N$ cannot be dense in $\phi(A) - N_1$. Hence $N$ is nowhere dense. Moreover, the complement $X - N = \phi(X) - N$ is open, so $N$ is closed.

**($\Rightarrow$)** Conversely, suppose $N$ is nowhere dense in $\mathcal{T}$. Then $\bar{N}$ (the closure of $N$ in $\mathcal{T}$) has empty interior. Since $N$ is nowhere dense, it is of first category in the topological sense. But we also know $\bar{N}$ is closed and nowhere dense, so by Theorem 22.2 (applied to the density topology which is a Baire space), $\bar{N}$ is a nullset. Therefore $N \subset \bar{N}$ is also a nullset, i.e., $N \in \mathcal{N}$.

Thus the nowhere dense sets are exactly the nullsets $\mathcal{N}$, and each such set is closed (since $X - N \in \mathcal{T}$ for $N \in \mathcal{N}$).
