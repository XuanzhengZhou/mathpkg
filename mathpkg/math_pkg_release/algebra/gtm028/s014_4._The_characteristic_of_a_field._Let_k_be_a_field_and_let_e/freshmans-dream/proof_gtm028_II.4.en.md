---
role: proof
locale: en
of_concept: freshmans-dream
source_book: gtm028
source_chapter: "II"
source_section: "4. The characteristic of a field"
---

Let $k$ be a field of characteristic $p > 0$ with identity $e$.

**Proof of (5):** For any $a \in k$, we have
$$
pa = p(ea) = (pe)a = 0 \cdot a = 0,
$$
since $pe = 0$ by definition of the characteristic.

**Proof of (6):** By the binomial theorem,
$$
(b \pm c)^p = \sum_{i=0}^{p} \binom{p}{i} b^{p-i} (\pm c)^i = b^p + (\pm 1)^p c^p + \sum_{i=1}^{p-1} \binom{p}{i} b^{p-i} (\pm c)^i.
$$

For $1 \le i \le p-1$, the binomial coefficient $\binom{p}{i} = \frac{p!}{i!(p-i)!}$ is an integer divisible by $p$, since the numerator contains the prime factor $p$ while the denominator does not (as $i < p$ and $p-i < p$). Hence each term $\binom{p}{i} b^{p-i}(\pm c)^i$ is of the form $p \cdot (\text{element of }k)$, which vanishes by identity (5). Therefore only the first and last terms survive:
$$
(b \pm c)^p = b^p + (\pm 1)^p c^p.
$$

If $p \neq 2$, then $p$ is odd, so $(\pm 1)^p = \pm 1$, and we obtain $(b \pm c)^p = b^p \pm c^p$.

If $p = 2$, then $(b - c)^2 = b^2 + c^2$. This is consistent with the formula because $c^2 = -c^2$ in characteristic $2$ (since $2c^2 = 0$).
