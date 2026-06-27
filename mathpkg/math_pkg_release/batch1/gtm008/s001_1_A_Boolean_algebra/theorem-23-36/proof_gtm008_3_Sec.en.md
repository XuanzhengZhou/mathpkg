---
role: proof
locale: en
of_concept: theorem-23-36
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
Let $0 < r \leq b \land (\forall \xi < \omega_\alpha)[b = \sum_{\eta < \omega_\beta} b_{\xi n}].$ Then, by the $(\omega_\alpha, \omega_\beta)$-WDL,
$$b = \prod_{\xi < \omega_\alpha} \sum_{\eta < \omega_\beta} b_{\xi n} = \sum_{f \in \omega_\beta \omega_\alpha} \prod_{\xi < \omega_\alpha} \sum_{\eta < f(\xi)} b_{\xi n}.$$
Therefore, for some $f \in \omega_\beta \omega_\alpha$,
$$\bar{r} = r \cdot \prod_{\xi < \omega_\alpha} \sum_{\eta < f(\xi)} b_{\xi n} > 0.$$
Let $\Lambda = \{\sum_{\eta < f(\xi)} b_{\xi n} \mid \xi < \omega_\alpha\}$. Then $\bar{\Lambda} \leq \aleph_\alpha$. Thus it remains to show that for $r' \in B$
$$0 < r' \leq \bar{r} \rightarrow (\forall \xi < \omega_\alpha)(\exists \eta < \omega_\beta)(\exists p \in \

For any $p \in P$, define

$$CA(p) = \{q \mid q \text{ is coatomic } \land q \geq p\}.$$

$P$ is said to be coatomic if

$(\forall p, q \in P)[CA(q) \subseteq CA(p) \leftrightarrow p \leq q].$

A coatomic partial order structure $P$ is said to be strongly coatomic if

$(\forall p \in P)(\forall S \subseteq CA(p))(\exists q \in P)[S = CA(q)].$

Remark. If $P$ is coatomic, then

$(\forall p \in P)[p \neq 1 \rightarrow CA(p) \neq 0]$

and

$(\forall p, q \in P)[p = q \leftrightarrow CA(p) = CA(q)].$
