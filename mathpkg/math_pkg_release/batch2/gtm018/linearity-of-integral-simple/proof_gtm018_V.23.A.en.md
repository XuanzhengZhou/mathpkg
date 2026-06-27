---
role: proof
locale: en
of_concept: linearity-of-integral-simple
source_book: gtm018
source_chapter: "V"
source_section: "23"
---

The result is an immediate consequence of the definition of the integral for simple functions. If $f = \sum_{i=1}^{n} \alpha_i \chi_{E_i}$ and $g = \sum_{j=1}^{m} \beta_j \chi_{F_j}$ are representations as linear combinations of characteristic functions of measurable sets of finite measure, then $\alpha f + \beta g = \sum_{i=1}^{n} \alpha \alpha_i \chi_{E_i} + \sum_{j=1}^{m} \beta \beta_j \chi_{F_j}$ is a representation of the linear combination as a simple function. The integral, being defined as the corresponding linear combination of the measures of the constituent sets, is then computed as

$$\int (\alpha f + \beta g) d\mu = \sum_{i=1}^{n} \alpha \alpha_i \mu(E_i) + \sum_{j=1}^{m} \beta \beta_j \mu(F_j) = \alpha \int f d\mu + \beta \int g d\mu.$$

The independence of the integral from the particular representation of a simple function (already verified) ensures that this computation is valid for any representation.
