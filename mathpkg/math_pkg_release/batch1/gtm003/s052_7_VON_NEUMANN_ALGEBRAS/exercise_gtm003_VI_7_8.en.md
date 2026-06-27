---
role: exercise
locale: en
chapter: "VI"
section: "7"
exercise_number: 8
---

Let $H$ be an infinite-dimensional Hilbert space, and let $\hat{H} = H \oplus H^\perp$ where $H^\perp$ is a copy of $H$.

(a) For each $T \in \mathcal{L}(H)$, define $\hat{T} \in \mathcal{L}(\hat{H})$ by extending $T$ trivially on $H^\perp$. Prove that $T \mapsto \hat{T}$ is a $C^*$-isomorphism of $\mathcal{L}(H)$ into $\mathcal{L}(\hat{H})$.

(b) Let $P$ denote the orthogonal projection of $\hat{H}$ onto $H$, and let $Q = \mathrm{id}_{\hat{H}} - P$. Show that for each $T \in \mathcal{L}(H)$, $\hat{T}$ is reduced by the pair $(P, Q)$, i.e., $\hat{T} = P\hat{T}P + Q\hat{T}Q$.

(c) The mapping $\Phi: \mathcal{L}(H) \to \mathcal{L}(H^\perp)$ given by $\Phi(T) = Q\hat{T}Q$ is a $C^*$-homomorphism with kernel equal to $\mathcal{K}(H)$, the ideal of compact operators. Therefore, $\Phi$ defines a representation of the Calkin algebra $\mathcal{L}(H)/\mathcal{K}(H)$ in $\mathcal{L}(K)$ for $K = H^\perp$.

(d) Prove that if (and only if) $H$ is separable, then $\mathcal{K}(H)$ is the unique closed ideal of $\mathcal{L}(H)$ distinct from $\mathcal{L}(H)$ and $\{0\}$.
