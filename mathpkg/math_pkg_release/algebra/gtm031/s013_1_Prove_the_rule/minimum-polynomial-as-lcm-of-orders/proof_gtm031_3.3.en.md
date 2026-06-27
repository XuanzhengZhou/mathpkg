---
role: proof
locale: en
of_concept: minimum-polynomial-as-lcm-of-orders
source_book: gtm031
source_chapter: "The Theory of a Single Linear Transformation"
source_section: "3"
---

*Proof.* Let $(e_1, e_2, \dots, e_r)$ be a set of generators for $\Re$ relative to $A$, meaning every $x \in \Re$ can be written as $x = \sum_{i=1}^r e_i \phi_i(A)$ for suitable $\phi_i(\lambda) \in \Phi[\lambda]$. (Such a set exists; for example, any ordinary basis has this property.) Let $\bar{\mu}(\lambda) = [\mu_{e_1}(\lambda), \mu_{e_2}(\lambda), \dots, \mu_{e_r}(\lambda)]$ be the least common multiple of the orders of the generators.

Since each $\mu_{e_i}(\lambda)$ divides the minimum polynomial $\mu(\lambda)$ of $A$ (as $e_i \mu(A) = 0$ and $\mu_{e_i}(\lambda)$ is the polynomial of least degree annihilating $e_i$), it follows that $\bar{\mu}(\lambda) \mid \mu(\lambda)$.

Conversely, for any $x = \sum e_i \phi_i(A)$, we have

$$x\bar{\mu}(A) = \sum_{i=1}^r e_i \phi_i(A)\bar{\mu}(A) = \sum_{i=1}^r e_i \bar{\mu}(A)\phi_i(A) = 0,$$

because $\bar{\mu}(\lambda)$ is a multiple of each $\mu_{e_i}(\lambda)$, hence $e_i \bar{\mu}(A) = 0$ for all $i$. Since this holds for every $x \in \Re$, we have $\bar{\mu}(A) = 0$. The minimum polynomial $\mu(\lambda)$ divides any polynomial that annihilates $A$, so $\mu(\lambda) \mid \bar{\mu}(\lambda)$. Therefore $\mu(\lambda) = \bar{\mu}(\lambda)$. $\square$
