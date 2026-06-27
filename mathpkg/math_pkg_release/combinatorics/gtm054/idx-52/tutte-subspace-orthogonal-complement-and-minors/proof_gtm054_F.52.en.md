---
role: proof
locale: en
of_concept: tutte-subspace-orthogonal-complement-and-minors
source_book: gtm054
source_chapter: "F"
source_section: "52"
---

(a) Let $\mathcal{T}$ be a Tutte subspace for $\Lambda$ and let $\mathcal{N}$ be the set of minimal nonempty supports of functions in $\mathcal{T}^\perp$. Following Example B18, $\Theta = (V, \mathcal{N})$ is a matroid. By definition of orthogonal complement,
$$\mathcal{T}^\perp = \{g \in \mathbb{F}^V : \sum_{x \in V} f(x)g(x) = 0 \text{ for all } f \in \mathcal{T}\}.$$
The minimal nonempty supports of functions in $\mathcal{T}^\perp$ correspond precisely to the cocycles of $\Lambda$, which are the cycles of $\Lambda^\perp$. Hence $\mathcal{T}^\perp$ is a Tutte subspace for $\Lambda^\perp$.

(b) Let $\Lambda'$ be a minor of $\Lambda$. A minor is obtained by a sequence of deletions and contractions. Since $\Lambda$ is representable over $\mathbb{F}$, there exists a Tutte subspace $\mathcal{T} \subseteq \mathbb{F}^V$ for $\Lambda$. For a deletion $\Lambda \setminus X$ (with $X \subseteq V$), the restriction $\mathcal{T}|_{V \setminus X} = \{h|_{V \setminus X} : h \in \mathcal{T}\}$ yields a Tutte subspace for the deletion. For a contraction $\Lambda / X$, one uses the dual construction via part (a) and the fact that contraction is deletion in the dual. By induction on the number of deletions and contractions, every minor preserves representability over $\mathbb{F}$.
