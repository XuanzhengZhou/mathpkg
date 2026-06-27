---
role: proof
locale: en
of_concept: simple-torus-modules
source_book: gtm020
source_chapter: "9"
source_section: "9. The Representation Ring of a Torus"
---

By Theorem 9.1, every simple $T^n$-module is one-dimensional and corresponds to a group homomorphism $T^n \rightarrow \mathbb{C}^\times$. Every such homomorphism factors through $S^1$, giving a character $\chi: T^n \rightarrow S^1$. The characters of $T^n$ are precisely the maps $(\theta_1, \ldots, \theta_n) \mapsto \exp(2\pi i \sum k_j \theta_j)$ for $(k_1, \ldots, k_n) \in \mathbb{Z}^n$. Hence each simple module is isomorphic to exactly one $M(k_1, \ldots, k_n)$.

For tensor products, $M(k_1, \ldots, k_n) \otimes M(l_1, \ldots, l_n) = M(k_1 + l_1, \ldots, k_n + l_n)$ follows from the relation $s(x \otimes y) = sx \otimes sy$ defining the action of $G$ on a tensor product. It follows that $R(T^n) \cong \mathbb{Z}[\mathbb{Z}^n] \cong \mathbb{Z}[\alpha_1, \ldots, \alpha_n, \alpha_1^{-1}, \ldots, \alpha_n^{-1}]$, where $\alpha_j$ corresponds to the generator with $k_j = 1$ and all other $k_i = 0$.

The involution $[M]^* = [\overline{M}]$ on $R(T^n)$ maps $\alpha_1^{k_1} \cdots \alpha_n^{k_n}$ to $\alpha_1^{-k_1} \cdots \alpha_n^{-k_n}$, where $\overline{M}$ is the conjugate module. The restriction-of-scalars map $\varepsilon_0: R(G) \rightarrow RO(G)$ satisfies $\varepsilon_0(\varepsilon_U(x)) = 2x$. Since $R(G)$ is a free abelian group by (7.5), $\varepsilon_U$ is a monomorphism.
