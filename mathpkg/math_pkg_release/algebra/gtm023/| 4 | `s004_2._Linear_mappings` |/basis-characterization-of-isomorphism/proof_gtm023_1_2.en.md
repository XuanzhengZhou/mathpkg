---
role: proof
locale: en
of_concept: basis-characterization-of-isomorphism
source_book: gtm023
source_chapter: "1"
source_section: "2"
---

*First direction.* Assume $\varphi$ is a linear isomorphism. Since $\varphi$ is surjective and $(x_{\alpha})$ is a system of generators for $E$, the set $(\varphi x_{\alpha})$ is a system of generators for $F$. Since $\varphi$ is injective and $(x_{\alpha})$ is linearly independent, the set $(\varphi x_{\alpha})$ is linearly independent in $F$. Thus $(\varphi x_{\alpha})$ is a basis of $F$.

*Converse direction.* Assume that the vectors $y_{\alpha} = \varphi x_{\alpha}$ form a basis of $F$.

*Surjectivity.* For every $y \in F$, write $y = \sum_{\alpha} \eta^{\alpha} y_{\alpha} = \sum_{\alpha} \eta^{\alpha} \varphi x_{\alpha} = \varphi\left(\sum_{\alpha} \eta^{\alpha} x_{\alpha}\right)$. Hence $y$ is in the image of $\varphi$, so $\varphi$ is surjective.

*Injectivity.* Suppose $\varphi\left(\sum_{\alpha} \lambda^{\alpha} x_{\alpha}\right) = \varphi\left(\sum_{\alpha} \mu^{\alpha} x_{\alpha}\right)$. Then
$$
0 = \sum_{\alpha} \lambda^{\alpha} \varphi x_{\alpha} - \sum_{\alpha} \mu^{\alpha} \varphi x_{\alpha} = \sum_{\alpha} (\lambda^{\alpha} - \mu^{\alpha}) y_{\alpha}.
$$
Since the $y_{\alpha}$ are linearly independent, $\lambda^{\alpha} = \mu^{\alpha}$ for each $\alpha$. Thus $\sum_{\alpha} \lambda^{\alpha} x_{\alpha} = \sum_{\alpha} \mu^{\alpha} x_{\alpha}$, proving $\varphi$ is injective.

Therefore $\varphi$ is a linear isomorphism.
