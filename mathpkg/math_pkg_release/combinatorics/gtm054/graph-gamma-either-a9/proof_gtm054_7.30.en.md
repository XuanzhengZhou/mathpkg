---
role: proof
locale: en
of_concept: graph-gamma-either-a9
source_book: gtm054
source_chapter: "7"
source_section: "VIIA"
---

Let $\nu_0(\Gamma) = n$ and suppose $K_{n-1}$ is not a subgraph of $\Gamma$. There exists $\{x, y\} \in \mathcal{P}_2(V) + \mathcal{E}$. Let $U = V + \

PROOF. (a) For definiteness, suppose $h_0: V \rightarrow \{1, \ldots, m\}$ and that $h_0(x_0) = m$. If $x_0$ were incident with no vertex of color, say $j \in \{1, \ldots, m-1\}$, then one could define an $(m-1)$-coloring $h$ of $\Gamma$ by changing the color of $x_0$ from $m$ to $j$, contrary to assumption. Hence $\rho(x_0) \geq m-1$.

(b) If $\rho(x_0) = m-1$, then clearly $x_0$ is incident with exactly one vertex of each of the colors $1, \ldots, m-1$. Let $x_1$ be incident with $x_0$. For definiteness, suppose that $h_0(x_1) = 1$. If $x_1$ is incident with no vertex of some color $j \in \{2, \ldots, m-1\}$, then one could define a vertex $(m-1)$-coloring $h$ of $\Gamma$ by

$$h(x) = \begin{cases} h_0(x) & \text{if } x \in V + \{x_0, x_1\}; \\ 1 & \text{if } x = x_0; \\ j & \text{if } x = x_1, \end{cases}$$

contrary to assumption. Hence $\rho(x_1) \geq m-1$.

Let $y$ and $z$ be given as in the statement. Let $(W, \mathcal{F})$ be the component of $\Gamma_{h_0}^{-1}[h_0[(y,z)]]$ containing $y$, but suppose $z \notin W$. Define a vertex $(m-1)$-coloring $h$ of $\Gamma$ by

$$h(x) = \begin{cases} h_0(x) & \text{if } x \notin W + \{x_0\}; \\ h_0(z) & \text{if } x \in W \cap h_0^{-1}[h_0(y)]; \\ h_0(y) & \text{if } x \
