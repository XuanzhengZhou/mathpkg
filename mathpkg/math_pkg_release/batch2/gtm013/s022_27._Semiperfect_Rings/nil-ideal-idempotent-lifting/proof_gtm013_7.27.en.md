---
role: proof
locale: en
of_concept: nil-ideal-idempotent-lifting
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

Suppose that $I$ is a nil ideal in $R$ and $g \in R$ satisfies $g + I = g^2 + I$. Then letting $n$ be the nilpotency index of $g - g^2$, we can use the binomial formula as follows:

$$0 = (g - g^2)^n = \sum_{k=0}^{n} \binom{n}{k} g^{n-k} (-g^2)^k = \sum_{k=0}^{n} \binom{n}{k} (-1)^k g^{n+k}.$$

Rearranging, we obtain $g^n = g^{n+1} h(g)$ for some polynomial $h$ with integer coefficients. Setting $e = g^n h(g)^n$, one verifies that $e^2 = e$ and $e + I = g + I$, so $e$ lifts the given idempotent in $R/I$.
