---
role: proof
locale: en
of_concept: dimension-of-factor-space
source_book: gtm023
source_chapter: "1"
source_section: "1.21"
---

If $E_1 = \{0\}$ or $E_1 = E$ the formula is trivial. Assume $0 < \dim E_1 < \dim E$. Let $x_1, \ldots, x_r$ be a basis of $E_1$ and extend it to a basis $x_1, \ldots, x_r, \ldots, x_n$ of $E$. By the theorem on basis of a factor space (sec. 1.18), the vectors $\bar{x}_{r+1}, \ldots, \bar{x}_n$ (the images under the canonical projection) form a basis of $E/E_1$. Hence $\dim E/E_1 = n - r = \dim E - \dim E_1$, giving $\dim E = \dim E_1 + \dim E/E_1$.

The inequality $\dim E_1 \leq \dim E$ is immediate. If equality holds, then $\dim E/E_1 = 0$, so $E/E_1 = \{\bar{0}\}$ and $E_1 = E$.
