---
role: proof
locale: en
of_concept: l-one-even-character-formula
source_book: gtm059
source_chapter: "3"
source_section: "3. Complex Analytic Class Number Formulas"
---

Start from the general formula for a primitive character $\chi$ modulo $m$:

$$L(1, \chi) = \frac{\tau(\chi)}{m} \sum_{a=1}^{m} \overline{\chi}(a) \log(1 - \zeta^a).$$

Pair the terms for $a$ and $m - a$. Since $\chi$ is even, $\overline{\chi}(m-a) = \overline{\chi}(-a) = \overline{\chi}(-1) \overline{\chi}(a) = \overline{\chi}(a)$ (because $\chi(-1) = 1$ implies $\overline{\chi}(-1) = 1$). Also $\zeta^{m-a} = \zeta^{-a}$.

Now

$$\log(1 - \zeta^a) + \log(1 - \zeta^{-a}) = \log((1 - \zeta^a)(1 - \zeta^{-a})) = \log|1 - \zeta^a|^2 = 2 \log|1 - \zeta^a|.$$

The imaginary parts cancel because $(1 - \zeta^a)(1 - \zeta^{-a}) = 2 - (\zeta^a + \zeta^{-a}) = 2 - 2\cos(2\pi a/m) = 4\sin^2(\pi a/m) \geq 0$, so the logarithm is real.

Summing over all $a = 1, \dots, m-1$ and pairing terms $a$ with $m-a$, each unordered pair contributes $2 \log|1 - \zeta^a|$. Since the pairs are counted twice in the original sum, we obtain:

$$L(1, \chi) = \frac{\tau(\chi)}{m} \sum_{a=1}^{m-1} \overline{\chi}(a) \log|1 - \zeta^a|.$$

(The term $a = m$ is $\overline{\chi}(m) \log(1 - 1) = 0$ and can be omitted.)
