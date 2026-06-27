---
role: proof
locale: en
of_concept: banach-bidual-w-star-structure
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

Let $\pi: A \to \mathcal{L}(H)$ denote the universal representation of $A$, where $H = \bigoplus_{\varphi \in \mathcal{S}(A)} H_\varphi$ and $\pi = \bigoplus \{\pi_\varphi : \varphi \in \mathcal{S}(A)\}$. Unless $A = \{0\}$, the construction ensures that $\pi(A)$ is non-degenerate.

For each fixed $\varphi \in \mathcal{S}(A)$, let $\xi = (\xi_\psi) \in H$ be defined by $\xi_\psi = 0$ for $\psi \neq \varphi$, with $\xi_\varphi$ being the cyclic vector of $\pi_\varphi$. Consider the duality $\langle L^1(H), \mathcal{L}(H) \rangle$ and let $\pi_*$ denote the adjoint of $\pi$ restricted to $L^1(H) \subset \mathcal{L}(H)'$.

Since $\pi_*(\xi \otimes \xi) = \varphi$ and $\varphi \in \mathcal{S}(A)$ was arbitrary, the mapping $\pi_*$ is surjective onto the state space. This implies that the second adjoint $\pi_{**}: A'' \to \mathcal{L}(H)$ maps $A''$ isometrically onto the strong closure $\overline{\pi(A)}$ in $\mathcal{L}(H)$. By Corollary 1, $\overline{\pi(A)} = \pi(A)^{cc}$ is a von Neumann algebra. Transporting the $W^*$-structure back to $A''$ via $\pi_{**}$ yields the desired $W^*$-structure on $A''$ under which $A$ is a $C^*$-subalgebra.
