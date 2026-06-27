---
role: proof
locale: en
of_concept: uan-condition-properties
source_book: gtm046
source_chapter: "IX-X"
source_section: "31-32"
---

Let $0 < \eta < \epsilon$. Since $$\int_{|x| < \epsilon} |x|^s dF'_{nk} \leq \eta^s + \epsilon^s P'[|X_{nk}| \geq \eta]$$ assertion (i) follows by taking $\max_k$ and letting $n \to \infty$ and then $\eta \to 0$. Assertion (ii) follows, on account of (i), from $$\int_{|x| < \epsilon} |x - \alpha'_{nk}(\epsilon)|^s dF'_{nk} \leq 2^{s-1} \int_{|x| < \epsilon} |x|^s dF'_{nk} + 2^{s-1} |\alpha'_{nk}(\epsilon)|^s$$ and $|\alpha'_{nk}(\epsilon)|^s \leq \epsilon^{s-1} |\alpha'_{nk}(\epsilon)|$. Finally, assertion (iii) follows, on account of (ii), from $$|\gamma'_{nk}(u)| \leq 2 \int_{|x| \geq \epsilon} dF'_{nk} + |u| \int_{|x| < \epsilon} |x - \alpha'_{nk}(\epsilon)| dF'_{nk}.$$
