---
role: proof
locale: en
of_concept: lemma-7-16
source_book: gtm011
source_chapter: "Entire Functions"
source_section: ""
---

Proof. To prove (a) note that if $0 < t \leq 1$ and $z$ is in $S$ then $(\text{Re } z-1) \log t \leq (a-1) \log t$; since $e^{-t} \leq 1$,

$$|e^{-t} t^{z-1}| \leq t^{\text{Re } z-1} \leq t^{a-1}.$$

So if $0 < \alpha < \beta < 1$ then

$$\left| \int_{\alpha}^{\beta} e^{-t} t^{z-1} dt \right| \leq \int_{\alpha}^{\beta} t^{a-1} dt$$

$$= \frac{1}{a} (\beta^a - \alpha^a)$$

for all $z$ in $S$. If $\epsilon > 0$ then we can choose $\delta, 0 < \delta < 1$, such that $a^{-1}(\beta^a - \alpha^a) < \epsilon$ for $|\alpha - \beta| < \delta$. This proves part (a).

To prove part (b) note that for $z$ in $S$ and $t \geq 1$, $|t^{z-1}| \leq t^{a-1}$. Since $t^{a-1} \exp(-\frac{1}{2}t)$ is continuous on $[1,
