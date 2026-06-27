---
role: proof
locale: en
of_concept: bilinear-form-to-linear-map-dual
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

**Proof.** Let $\sigma \in \mathcal{B}(V)$. Since $\sigma$ is linear in the second variable, the mapping

$$b \mapsto \sigma(a, b)$$

is a linear form on $V$. Denote this form by $a\varrho_\sigma$. Then, since $\sigma$ is linear in the first variable, $\varrho_\sigma$ is a linear mapping of $V$ into the dual space $V^*$, i.e.,

$$(xa + yb)\varrho_\sigma = x(a\varrho_\sigma) + y(b\varrho_\sigma).$$

Conversely, let $f \in \mathcal{L}(V, V^*)$ and define $\sigma_f$ by

$$\sigma_f(a, b) = (af)(b)$$

for all $a, b \in V$. Then $\sigma_f$ is bilinear because $f$ is linear and each $af$ is a linear form on $V$. The mapping $f \mapsto \sigma_f$ is the inverse of $\sigma \mapsto \varrho_\sigma$, so $\sigma \mapsto \varrho_\sigma$ is bijective. Linearity follows directly from the definitions of addition and scalar multiplication on $\mathcal{B}(V)$:

$$(\sigma + \tau)(a, b) = \sigma(a, b) + \tau(a, b), \quad (x\sigma)(a, b) = x\sigma(a, b).$$

If $(a_1, \ldots, a_n)$ is an ordered basis of $V$ and $s_{ij} = \sigma(a_i, a_j)$, then

$$a_i\varrho_\sigma(a_j) = s_{ij}$$

and so $a_i\varrho_\sigma = \sum_j s_{ij} a^j$. Thus the matrix $(\varrho_\sigma; (a_i), (a^j))$ is simply $(s_{ij})$. Similarly, $(\tilde{\sigma}; (a_i), (a^j)) = (s_{ij})^t$. Since row rank equals column rank, the ranks of $\varrho_\sigma$ and $\tilde{\sigma}$ both equal the rank of $\sigma$.
