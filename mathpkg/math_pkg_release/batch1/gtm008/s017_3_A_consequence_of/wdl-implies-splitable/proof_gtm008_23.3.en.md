---
role: proof
locale: en
of_concept: wdl-implies-splitable
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

Let $0 < r \leq b \land (\forall \xi < \omega_\alpha)[b = \sum_{\eta < \omega_\beta} b_{\xi \eta}].$ Then, by the $(\omega_\alpha, \omega_\beta)$-WDL,
$$b = \prod_{\xi < \omega_\alpha} \sum_{\eta < \omega_\beta} b_{\xi \eta} = \sum_{f \in \omega_\beta^{\omega_\alpha}} \prod_{\xi < \omega_\alpha} \sum_{\eta < f(\xi)} b_{\xi \eta}.$$
Therefore, for some $f \in \omega_\beta^{\omega_\alpha}$,
$$\bar{r} = r \cdot \prod_{\xi < \omega_\alpha} \sum_{\eta < f(\xi)} b_{\xi \eta} > 0.$$
Let $\Lambda = \{\sum_{\eta < f(\xi)} b_{\xi \eta} \mid \xi < \omega_\alpha\}$. Then $\bar{\Lambda} \leq \aleph_\alpha$. It remains to show that for $r' \in B$
$$0 < r' \leq \bar{r} \rightarrow (\forall \xi < \omega_\alpha)(\exists \eta < \omega_\beta)(\exists p \in \Lambda)[p \cdot r' > 0 \land p \cdot \bar{r} \leq \sum_{\eta' < \eta} b_{\xi \eta'}],$$
which follows from the definition of $\Lambda$ and $\bar{r}$.
