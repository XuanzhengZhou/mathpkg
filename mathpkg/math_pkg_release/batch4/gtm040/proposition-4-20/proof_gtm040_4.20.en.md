---
role: proof
locale: en
of_concept: proposition-4-20
source_book: gtm040
source_chapter: "4"
source_section: "20"
---

**Proof:**

$$N_{ii} = \sum_{k=1}^{\infty} k \Pr_i[n_i = k],$$

which upon rearrangement of terms becomes

$$= \sum_{k=1}^{\infty} \sum_{m=k}^{\infty} \Pr_i[n_i = m],$$

which by complete additivity is

$$= \sum_{k=1}^{\infty} \Pr_i[n_i \geq k]$$

$$= \sum_{k=1}^{\infty} (\bar{H}_{ii})^{k-1} \text{ by conclusion (1) of Lemma 4-19.}$$

The right side is finite if and only if $\bar{H}_{ii} < 1$.
