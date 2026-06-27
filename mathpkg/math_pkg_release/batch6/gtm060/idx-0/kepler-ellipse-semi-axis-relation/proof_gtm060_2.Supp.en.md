---
role: proof
locale: en
of_concept: kepler-ellipse-semi-axis-relation
source_book: gtm060
source_chapter: "2"
source_section: "Supplement: Kepler Problem"
---

From the focal equation $r = p/(1 + e \cos \varphi)$, the pericenter distance ($\varphi = 0$) is $r_{\min} = p/(1 + e)$, and the apocenter distance ($\varphi = \pi$) is $r_{\max} = p/(1 - e)$. The major axis length is the sum:

$$2a = r_{\min} + r_{\max} = \frac{p}{1 + e} + \frac{p}{1 - e} = \frac{p(1 - e) + p(1 + e)}{(1 + e)(1 - e)} = \frac{2p}{1 - e^2}.$$

Thus $a = p/(1 - e^2)$. The focal distance is $c = a - r_{\min} = a - p/(1 + e)$. Substituting $a = p/(1 - e^2)$:

$$c = \frac{p}{1 - e^2} - \frac{p}{1 + e} = \frac{p - p(1 - e)}{1 - e^2} = \frac{pe}{1 - e^2} = ae.$$

Hence $e = c/a$. From the definition of an ellipse, $b^2 = a^2 - c^2 = a^2(1 - e^2)$, giving $e = \sqrt{a^2 - b^2}/a$.
