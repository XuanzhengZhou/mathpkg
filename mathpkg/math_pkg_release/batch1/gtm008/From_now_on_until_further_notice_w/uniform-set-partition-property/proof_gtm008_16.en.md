---
role: proof
locale: en
of_concept: uniform-set-partition-property
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $y = \sum_{i \in I} b_i x_i$. Since $\mathcal{D}(u)$ is complete, $y$ exists and $y \in \mathcal{D}(u)$. Since $\{x_i\} \subseteq \mathcal{D}(u)$,

\begin{align*}
u(y) = \llbracket y \in u \rrbracket &= \sum_{x \in \mathcal{D}(u)} u(x) \cdot \llbracket x = y \rrbracket \\
&\geq \sum_{i \in I} u(x_i) \cdot \llbracket x_i = y \rrbracket \\
&\geq \sum_{i \in I} u(x_i) \cdot b_i.
\end{align*}

(Note that since $x_i \in \mathcal{D}(u)$, $\llbracket x_i = y \rrbracket \geq b_i$.)

On the other hand, since $\sum b_i = 1$ and the $b_i$ are disjoint,
$$b_i \cdot u(y) \leq \llbracket x_i = y \rrbracket \cdot \llbracket y \in u \rrbracket \leq \llbracket x_i \in u \rrbracket = u(x_i).$$

Thus $b_i \cdot u(y) \leq b_i \cdot u(x_i)$, and summing over $i$:
$$u(y) = \sum_i b_i \cdot u(y) \leq \sum_i b_i \cdot u(x_i).$$

Combining both inequalities yields $u(y) = \sum_i b_i \cdot u(x_i)$.
