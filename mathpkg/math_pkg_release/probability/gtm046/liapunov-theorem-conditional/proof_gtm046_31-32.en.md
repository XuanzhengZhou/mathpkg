---
role: proof
locale: en
of_concept: liapunov-theorem-conditional
source_book: gtm046
source_chapter: "IX-X"
source_section: "31-32"
---

Take the $Y_{nk}$ to be conditionally normal $\mathcal{N}(0, \sigma'^2_{nk})$, so that the law of $Y_{nk}$ is the weighted symmetric normal $\mathcal{N}(0, \sigma'^2_{nk})$, and apply the comparison theorem with $S = R, l = 0, m = 2$, and $\delta \leq 1$. The comparison conditions for $j = 1, 2$ are fulfilled, since the corresponding sums vanish—the first because of the centering and the second because of $E'Y_{nk}^2 = E'X_{nk}^2$. The condition with $m + \delta$ is fulfilled, since $$E |Y_{nk}|^{2+\delta} = EE' |Y_{nk}|^{2+\delta} = cE\sigma'^{2+\delta}_{nk} \leq cEE' |X_{nk}|^{2+\delta} = cE |X_{nk}|^{2+\delta}$$ and hence $$\sum_k E \int |x|^{2+\delta} |dF'_{nk} - dG'_{nk}| \leq (1 + c) \sum_k E |X_{nk}|^{2+\delta} \to 0.$$
