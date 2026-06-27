---
role: proof
locale: en
of_concept: chebyshev-inequality
source_book: gtm017
source_chapter: "II"
source_section: "e"
---
For $EX^2 = \sum_i a_i^2 p_i$, we have
$$EX^2 = \sum_{i=1}^{\infty} a_i^2 p_i \geq \sum_{|a_i| \geq \varepsilon} a_i^2 p_i \geq \varepsilon^2 \sum_{|a_i| \geq \varepsilon} p_i = \varepsilon^2 P(|X| \geq \varepsilon).$$
Dividing by $\varepsilon^2$ gives $P(|X| \geq \varepsilon) \leq EX^2 / \varepsilon^2$.
