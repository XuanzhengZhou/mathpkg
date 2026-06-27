---
role: proof
locale: en
of_concept: relative-coordinate-dependence
source_book: gtm060
source_chapter: "1"
source_section: "2"
---
Let $\mathbf{x}_i = \varphi_i(t)$ be a solution. Under spatial translation by $\mathbf{r} \in \mathbb{R}^3$, the transformed solution is $\tilde{\varphi}_i(t) = \varphi_i(t) + \mathbf{r}$. The accelerations are unchanged: $\ddot{\tilde{\varphi}}_i = \ddot{\varphi}_i$. If the force law is $\mathbf{F}_i(\{\mathbf{x}_j\}, \{\dot{\mathbf{x}}_j\})$, invariance requires:

$$\mathbf{F}_i(\{\varphi_j + \mathbf{r}\}, \{\dot{\varphi}_j\}) = \mathbf{F}_i(\{\varphi_j\}, \{\dot{\varphi}_j\})$$

for all $\mathbf{r}$. This means $\mathbf{F}_i$ is invariant under simultaneous translation of all position arguments, which is equivalent to depending only on differences $\mathbf{x}_j - \mathbf{x}_k$.
