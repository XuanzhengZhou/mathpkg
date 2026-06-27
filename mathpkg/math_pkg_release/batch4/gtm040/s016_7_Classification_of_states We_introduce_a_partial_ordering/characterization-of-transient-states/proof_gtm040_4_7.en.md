---
role: proof
locale: en
of_concept: characterization-of-transient-states
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** Write the expected number of visits as
$$N_{ii} = \sum_{k=1}^{\infty} k \Pr_i[n_i = k],$$
where $n_i$ is the total number of visits to state $i$. Rearranging terms,
$$N_{ii} = \sum_{k=1}^{\infty} \sum_{m=k}^{\infty} \Pr_i[n_i = m].$$

By complete additivity, this equals
$$N_{ii} = \sum_{k=1}^{\infty} \Pr_i[n_i \geq k].$$

By conclusion (1) of Lemma 4-19, $\Pr_i[n_i \geq k] = (\bar{H}_{ii})^{k-1}$. Therefore,
$$N_{ii} = \sum_{k=1}^{\infty} (\bar{H}_{ii})^{k-1}.$$

The right side is a geometric series, which is finite if and only if $\bar{H}_{ii} < 1$. In that case,
$$N_{ii} = \frac{1}{1 - \bar{H}_{ii}}.$$

Thus $i$ is transient ($\bar{H}_{ii} < 1$) if and only if $N_{ii} < +\infty$.
