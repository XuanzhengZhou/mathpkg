---
role: proof
locale: en
of_concept: T-stable-subgroup-of-U-is-direct-product
source_book: gtm021
source_chapter: "28"
source_section: "28.1"
---
Let $\Psi = \Phi(H, T)$, so $\mathfrak{h} = \bigsqcup_{\alpha \in \Psi} \mathfrak{g}_\alpha$. Order $\Psi$ in any way as $(\alpha_1, \ldots, \alpha_n)$, and let $\pi: U_{\alpha_1} \times \cdots \times U_{\alpha_n} \rightarrow H$ be the product morphism. This makes sense, because for $\alpha \in \Psi$, $U_\alpha = C_U(T_\alpha)$ does lie in $H$ (apply Proposition 18.4A to the action of $T_\alpha$ on $H$). We show $\pi$ is bijective (which implies that $H$ is connected) by induction on $\dim H$.

First treat the case where $H$ is connected. If $H$ is commutative, then $\pi$ is actually a homomorphism, with $\operatorname{Ker} \pi$ finite and $T$-stable. The connected group $T$ must permute the finite set $\operatorname{Ker} \pi$ trivially (Proposition 8.2(d)), forcing $\operatorname{Ker} \pi \subset$ fixed point set of $T$ on $H = e$.
