---
role: proof
locale: en
of_concept: ccc-implies-omega-alpha-wdl
source_book: gtm008
source_chapter: "20"
source_section: "20. Weak Distributive Laws"
---

Let $\{b_{n\xi} \mid n < \omega \land \xi < \omega_{\alpha}\} \subseteq B$. By the c.c.c., for each $n \in \omega$ there exists a countable set $C_n \subseteq B$ such that
$$
\sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sup C_n.
$$

For each $c \in C_n$, since $c \leq \sum_{\xi < \omega_\alpha} b_{n\xi}$ and by the c.c.c. the antichain suppporting $c$ is countable, there exists a countable set of indices $I_{n,c} \subseteq \omega_\alpha$ such that $c \leq \sum_{\xi \in I_{n,c}} b_{n\xi}$. Define
$$
\eta_0 = \sup \bigcup \{I_{n,c} \mid n \in \omega, c \in C_n\}.
$$

Since each $C_n$ is countable and each $I_{n,c}$ is countable, $\bigcup_{n,c} I_{n,c}$ has cardinality at most $\omega \cdot \omega = \omega$. Because $\operatorname{cf}(\omega_\alpha) > \omega$, we have $\eta_0 < \omega_\alpha$.

Consequently, for every $n \in \omega$ and every $\xi < \omega_\alpha$,
$$
b_{n\xi} \leq \sum_{\xi \leq \eta_0} b_{n\xi} \quad \text{whenever } \xi > \eta_0,
$$
and in fact $\sum_{\xi < \omega_\alpha} b_{n\xi} = \sum_{\xi \leq \eta_0} b_{n\xi}$ for each $n$. Therefore,
$$
\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi}
= \prod_{n < \omega} \sum_{\xi \leq \eta_0} b_{n\xi}
\leq \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}.
$$

By the Remark after Definition 20.1, since $\operatorname{cf}(\omega_\alpha) > \omega$, the right-hand side equals
$$
\sum_{f \in \omega_{\alpha}^{\omega}} \prod_{n \in \omega} \sum_{\xi \leq f(n)} b_{n\xi},
$$
which establishes the $(\omega, \omega_\alpha)$-WDL.
