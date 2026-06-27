---
role: proof
locale: en
of_concept: nowhere-dense-iff-nullset
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

($\Leftarrow$) Suppose $N \in \mathcal{N}$, i.e., $\mu(N) = 0$. By property (3) of the lower density, $\phi(X) = X$. Then
$$X \setminus N = \phi(X) \setminus N$$
is a basic open set in the topology $\mathcal{T}$, which means $N$ is closed. Moreover, $N$ contains no nonempty $\mathcal{T}$-open set, because any basic open set $\phi(A) \setminus N_A$ that is non-null would have positive measure (otherwise $\mu(\phi(A) \setminus N_A) = 0$ would imply $\phi(A) \setminus N_A \subset M$ for some $M \in \mathcal{N}$, making the basic open set empty in the relevant sense). Thus $\operatorname{int}_{\mathcal{T}}(N) = \emptyset$, so $N$ is nowhere dense and closed.

($\Rightarrow$) Conversely, suppose $N \subset X$ is nowhere dense relative to $\mathcal{T}$. Then $\operatorname{int}_{\mathcal{T}}(\overline{N}^{\mathcal{T}}) = \emptyset$. Every nonempty $\mathcal{T}$-open set has the form $\phi(A) \setminus N_A$ with $\mu(A) > 0$ (otherwise $\phi(A)$ would be a nullset, implying $A$ is a nullset). If $\mu(N) > 0$, then by property (1) of $\phi$, $\mu(\phi(N)) = \mu(N) > 0$, so $\phi(N) \setminus \emptyset$ is a nonempty $\mathcal{T}$-open set. But $\phi(N) \setminus \emptyset$ is contained in the closure of $N$ (up to a nullset), which would give $N$ nonempty interior, a contradiction. Hence $\mu(N) = 0$, i.e., $N \in \mathcal{N}$.
