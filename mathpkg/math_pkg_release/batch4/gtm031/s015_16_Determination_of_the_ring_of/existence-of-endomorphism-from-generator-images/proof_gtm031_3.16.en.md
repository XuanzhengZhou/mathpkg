---
role: proof
locale: en
of_concept: existence-of-endomorphism-from-generator-images
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

Define $B: \sum \xi_i f_i \mapsto \sum \xi_i g_i$ for $\xi_i \in \mathfrak{o}$. To verify that $B$ is well-defined, suppose $\sum \xi_i f_i = \sum \xi_i' f_i$. Then $\sum (\xi_i - \xi_i') f_i = 0$, so $\xi_i - \xi_i' \in (\delta_i)$ for each $i$, i.e., $\delta_i \mid (\xi_i - \xi_i')$. Write $\xi_i - \xi_i' = \eta_i \delta_i$ for some $\eta_i \in \mathfrak{o}$. Then

$$\sum (\xi_i - \xi_i') g_i = \sum \eta_i \delta_i g_i = \sum \eta_i \cdot 0 = 0,$$

since $\delta_i g_i = 0$ by the condition $\epsilon_i \mid \delta_i$. Hence $\sum \xi_i g_i = \sum \xi_i' g_i$, so $B$ is well-defined.

The mapping $B$ is clearly $\mathfrak{o}$-linear: for any $\alpha \in \mathfrak{o}$,

$$(\alpha \sum \xi_i f_i) B = (\sum (\alpha \xi_i) f_i) B = \sum \alpha \xi_i g_i = \alpha \sum \xi_i g_i = \alpha ((\sum \xi_i f_i) B),$$

and additivity follows similarly from the definition. Therefore $B \in \mathfrak{B}$.
