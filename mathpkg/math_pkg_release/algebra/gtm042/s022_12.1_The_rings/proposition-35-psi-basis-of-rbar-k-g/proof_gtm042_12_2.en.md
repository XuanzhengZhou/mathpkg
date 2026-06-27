---
role: proof
locale: en
of_concept: proposition-35-psi-basis-of-rbar-k-g
source_book: gtm042
source_chapter: "12"
source_section: "12.2"
---

The algebra $K[G]$ is a product of simple algebras $A_i$, corresponding to the distinct irreducible representations $V_i$ of $G$ over $K$. If $D_i = \operatorname{Hom}^G(V_i, V_i)$ is the commuting algebra of $G$ in $\operatorname{End}(V_i)$, then $D_i$ is a division algebra (noncommutative, in general), and $A_i \cong M_{n_i}(D_i^{\mathrm{op}})$. Let $K_i$ be the center of $D_i$.

Now let $\Sigma_i$ be the set of $K$-homomorphisms of the field $K_i$ into the algebraically closed field $\mathbb{C}$. If $\sigma \in \Sigma_i$, scalar extension from $K$ to $\mathbb{C}$ by means of $\sigma$ makes $D_i$ into a matrix algebra $M_{m_i}(\mathbb{C})$, and $A_i$ becomes $M_{n_i m_i}(\mathbb{C})$. Composing $G \to A_i \to M_{n_i m_i}(\mathbb{C})$, we obtain an irreducible representation of $G$ over $\mathbb{C}$, of degree $n_i m_i$, and with character $\psi_{i,\sigma} = \sigma(\psi_i)$ where $\psi_i$ is the character of the representation over the center $K_i$.

For fixed $i$, the characters $\psi_{i,\sigma}$ are conjugate: the Galois group of $\mathbb{C}$ over $K$ permutes them transitively. Moreover, each irreducible character of $G$ over $\mathbb{C}$ is equal to one of the $\psi_{i,\sigma}$. We have

$$\chi_i = \operatorname{Tr}_{K_i/K}(\varphi_i) = \sum_{\sigma \in \Sigma_i} \sigma(\varphi_i) = m_i \sum_{\sigma \in \Sigma_i} \psi_{i,\sigma},$$

which gives the decomposition of $\chi_i$ as a sum of irreducible characters over $\mathbb{C}$.

Now let $\chi = \sum_{i,\sigma} d_{i,\sigma} \psi_{i,\sigma}$ be an element of $R(G)$, where the $d_{i,\sigma}$ are integers. In order that $\chi$ have values in $K$, it is necessary and sufficient that it be invariant under the Galois group of $\mathbb{C}$ over $K$, i.e., that the $d_{i,\sigma}$ depend only on $i$. If this is indeed the case, and we let $d_i$ denote their common value, we have

$$\chi = \sum_i d_i \sum_{\sigma \in \Sigma_i} \psi_{i,\sigma} = \sum_i d_i \frac{\chi_i}{m_i}.$$

Hence the characters $\psi_i = \chi_i/m_i$ form a basis of $\overline{R}_K(G)$.
