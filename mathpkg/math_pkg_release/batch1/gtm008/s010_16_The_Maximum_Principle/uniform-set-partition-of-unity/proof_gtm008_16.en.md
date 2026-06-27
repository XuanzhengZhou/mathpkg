---
role: proof
locale: en
of_concept: uniform-set-partition-of-unity
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $y = \sum_{i \in I} b_i x_i$. Since $\mathcal{D}(u)$ is complete, $y$ exists and $y \in \mathcal{D}(u)$.

First direction: Since $\{x_i \mid i \in I\} \subseteq \mathcal{D}(u)$,

$$u(y) = \llbracket y \in u \rrbracket = \sum_{x \in \mathcal{D}(u)} u(x) \cdot \llbracket x = y \rrbracket \geq \sum_{i \in I} u(x_i) \cdot \llbracket x_i = y \rrbracket \geq \sum_{i \in I} u(x_i) \cdot b_i.$$

The last inequality holds because $\llbracket x_i = y \rrbracket \geq b_i$ (since $y$ is the Boolean sum of the $b_i x_i$).

Second direction: Since $\sum_{i \in I} b_i = 1$,

$$b_i \cdot u(y) = b_i \cdot \llbracket y \in u \rrbracket \leq \llbracket x_i = y \rrbracket \cdot \llbracket y \in u \rrbracket \leq \llbracket x_i \in u \rrbracket = u(x_i).$$

Thus $b_i \cdot u(y) \leq b_i \cdot u(x_i)$ for each $i$, and

$$u(y) = \left(\sum_{i \in I} b_i\right) \cdot u(y) \leq \sum_{i \in I} b_i \cdot u(x_i).$$

Combining both directions, $u(y) = \sum_{i \in I} b_i \cdot u(x_i)$.
