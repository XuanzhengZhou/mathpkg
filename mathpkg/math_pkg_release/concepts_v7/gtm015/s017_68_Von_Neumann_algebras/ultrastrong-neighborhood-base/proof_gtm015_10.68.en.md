---
role: proof
locale: en
of_concept: ultrastrong-neighborhood-base
source_book: gtm015
source_chapter: "10"
source_section: "68"
---

# Proof of Basic neighborhood of zero for the ultrastrong topology

Proof. With notation as in (68.11), a basic $\tau_{us}$-neighborhood $\mathcal{V}$ of $0 \in \mathcal{L}(H)$ is defined by fixing $y_1 = (y_{1i}), \ldots, y_n = (y_{ni}) \in K$ and setting

$$\mathcal{V} = \{T \in \mathcal{L}(H): p_{y_k}(\tilde{T}) \leq 1 \text{ for } k = 1, \ldots, n\};$$

since $p_{y_k}(\tilde{T}) \leq 1$ iff $p_{y_k}(\tilde{T})^2 \leq 1$, this may be written

$$\mathcal{V} = \left\{T \in \mathcal{L}(H): \sum_{i=1}^{\infty} \sum_{k=1}^{n} \|T y_{ki}\|^2 \leq 1\right\}.$$

Set $x_i$ to be the sequence obtained by concatenating the $y_{k i}$ for $k = 1, \ldots, n$ (with zeros for large indices). Then $\sum_i \|x_i\|^2 = \sum_k \sum_i \|y_{ki}\|^2 < \infty$, and the condition $\sum_{k=1}^{n} \sum_{i=1}^{\infty} \|T y_{ki}\|^2 \leq 1$ is equivalent to $\sum_{i=1}^{\infty} \|T x_i\|^2 \leq 1$. Thus the basic neighborhoods can be described by a single sequence $(x_i)$ in $K$.
