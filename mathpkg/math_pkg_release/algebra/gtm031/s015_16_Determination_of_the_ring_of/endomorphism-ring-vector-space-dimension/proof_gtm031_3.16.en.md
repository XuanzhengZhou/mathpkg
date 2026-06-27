---
role: proof
locale: en
of_concept: endomorphism-ring-vector-space-dimension
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

First, $\mathfrak{B} \supseteq \mathfrak{A} = \Phi[A] \supseteq \Phi$, so scalar multiplication by elements of $\Phi$ acts on $\mathfrak{B}$, making it a vector space over $\Phi$.

The normalized matrix corresponding to scalar multiplication $\alpha 1$ is the scalar matrix $\operatorname{diag}(\alpha, \ldots, \alpha)$, since $f_i (\alpha 1) = \alpha f_i$. The set $\mathfrak{U}$ of normalized matrices is closed under addition and under multiplication by scalar matrices; thus $\mathfrak{U}$ is a vector space over $\Phi$ where $\alpha(\beta)$ is defined as the matrix product $\alpha 1 \cdot (\beta)$.

Since the correspondence $\mathfrak{U} \to \mathfrak{B}$ is a bijection and respects the vector space operations ($B_1 + B_2 \leftrightarrow (\beta_1) + (\beta_2)$ and $\alpha B \leftrightarrow \alpha(\beta)$), $\mathfrak{B}$ and $\mathfrak{U}$ are isomorphic as vector spaces over $\Phi$.

To compute $\dim \mathfrak{U}$, count the degrees of freedom in each matrix entry:
- For $i \geq j$: $\beta_{ij}$ is arbitrary in $\mathfrak{o}$, but $\mathfrak{o} = \Phi[\lambda]$ and we work modulo $(\delta_j)$, giving $n_j = \deg \delta_j$ free parameters per entry.
- For $i < j \leq u$: $\beta_{ij}$ satisfies $\beta_{ij} \equiv 0 \pmod{\eta_{ij}}$, where $\eta_{ij} = \delta_i^{-1} \delta_j$ has degree $n_j - n_i$. Thus $\beta_{ij}$ is a multiple of $\eta_{ij}$, so there are $n_i$ free parameters.
- For $i \leq u < j$: $\beta_{ij} = 0$, no free parameters.
- For $i, j > u$: $\beta_{ij}$ is arbitrary over $\Phi$, giving $1$ dimension each (infinitely many over $\mathfrak{o}$, but over $\Phi$ each degree represents an independent parameter).

Carrying out the count yields $N = \sum_{j=1}^{t} (2t - 2j + 1) n_j$. When $t > 1$, comparing with $n = \sum_{j=1}^{t} n_j$ gives $N > n$. Since $\dim \mathfrak{A} = n_t$ (the degree of the minimal polynomial), it follows that $\mathfrak{B} \supsetneq \mathfrak{A}$.
