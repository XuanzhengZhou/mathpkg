---
role: exercise
locale: en
chapter: "Chapter 13"
section: "13.4"
exercise_number: 4
---
# Exercise 13.4

For $q_n = n(n-1)/2$, show that

$$K_{MB} = (-1)^{q_n} K_{\tilde{w}},$$

where $K_{MB}$ is the Bochner-Martinelli kernel

$$K_{MB}(\zeta, z) = \sum_{j=1}^{n} \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^{2n}} \; d\bar{\zeta}_1 \wedge d\zeta_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_j} \wedge d\zeta_j \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_n,$$

and $K_{\tilde{w}}$ is the Cauchy-Fantappie form corresponding to the weight functions

$$\tilde{w}_j(\zeta, z) = \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^2},$$

namely

$$K_{\tilde{w}}(\zeta, z) = \frac{1}{|\zeta - z|^{2n}} \sum_{k=1}^{n} (-1)^{k-1} (\bar{\zeta}_k - \bar{z}_k) \; d\bar{\zeta}_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_k} \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_1 \wedge \cdots \wedge d\zeta_n.$$

*Hint:* Compare the ordering of the differentials $d\zeta_j$ and $d\bar{\zeta}_j$ in the two expressions. The sign $(-1)^{q_n}$ arises from reordering the $d\zeta_j$ terms past the $d\bar{\zeta}_j$ terms in the wedge product.
