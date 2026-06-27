---
role: proof
locale: en
of_concept: equivalence-relation-partition-b7-b7
source_book: gtm054
source_chapter: "5"
source_section: "IVB"
---

As above, represent $D$ by the list: $x_0, e_1, x_1, e_2, \ldots, e_m, x_m = x_0$ and let $\{I, J\}$ be a 2-partition of $\{1, \ldots, m\}$ where

$$I = \{i: e_i = (x_{i-1}, x_i)\} \quad \text{and} \quad J = \{i: e_i = (x_i, x_{i-1})\}.$$

By definition, $h_D = \sum_{i \in I} c_{e_i} - \sum_{i \in J} c_{e_i}$. Hence,

$$\partial(h_D) = \sum_{i \in I} \partial(c_{e_i}) - \sum_{i \in J} \partial(c_{e_i})$$

$$= \sum_{i \in I} (c_{x_i} - c_{x_{i-1}}) - \sum_{i \in J} (c_{x_{i-1

flow. In order to show that $h_D$ is an elementary flow, it suffices to prove that $h_D$ is a minimal flow, since by definition, $h_D[W] \subseteq \{0, 1, -1\}$. We select a minimal flow $h$ such that $\sigma(h) \subseteq \sigma(h_D)$. By the first part of this same proof, there exists an elementary circuit $D''$ such that $\sigma(h_D'') \subseteq \sigma(h)$, and so $\sigma(h_D'') \subseteq \sigma(h_D)$. By IIIA9, both $\sigma(h_D'')$ and $\sigma(h_D)$ are elementary cycles of $\Gamma$. Hence

$$\sigma(h_D) = \sigma(h) = \sigma(h_D'') \in \mathcal{M}(F).$$

As an immediate consequence of this proposition and IIIA9 we have
