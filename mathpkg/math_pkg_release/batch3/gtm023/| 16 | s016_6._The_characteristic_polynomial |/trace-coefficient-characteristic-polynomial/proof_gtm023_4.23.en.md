---
role: proof
locale: en
of_concept: trace-coefficient-characteristic-polynomial
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§7. The trace"
---

From formula (4.48) for $p = 1$,
$$\sum_{\sigma} \varepsilon_{\sigma} \Delta(\varphi x_{\sigma(1)}, x_{\sigma(2)}, \ldots, x_{\sigma(n)}) = (-1)^{n-1} \alpha_1 \Delta(x_1, \ldots, x_n),$$
where the sum is over all permutations $\sigma$ with $\sigma(2) < \cdots < \sigma(n)$.

This sum can be reorganized as
$$\sum_{i=1}^{n} (-1)^{i-1} \Delta(\varphi x_i, x_1, \ldots, \hat{x}_i, \ldots, x_n) = \sum_{i=1}^{n} \Delta(x_1, \ldots, x_{i-1}, \varphi x_i, x_{i+1}, \ldots, x_n).$$

By the definition of the trace,
$$\sum_{i} \Delta(x_1, \ldots, \varphi x_i, \ldots, x_n) = \operatorname{tr} \varphi \cdot \Delta(x_1, \ldots, x_n).$$

Comparing with the expression above yields $(-1)^{n-1} \alpha_1 = \operatorname{tr} \varphi$, i.e., $\alpha_1 = (-1)^{n-1} \operatorname{tr} \varphi$.
