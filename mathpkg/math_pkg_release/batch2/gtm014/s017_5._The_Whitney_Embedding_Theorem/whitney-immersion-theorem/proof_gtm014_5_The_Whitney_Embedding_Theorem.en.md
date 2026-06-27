---
role: proof
locale: en
of_concept: whitney-immersion-theorem
source_book: gtm014
source_chapter: "5"
source_section: "The Whitney Embedding Theorem"
---

**Openness:** Already established in Lemma 5.5.

**Density:** Let $n = \dim X$, $m = \dim Y$, and $q = \min(m, n) = n$ (since $m \geq 2n$). For $r \geq 1$, Theorem 5.4 gives

$$\operatorname{codim} S_r = (n - q + r)(m - q + r) = r(m - n + r).$$

Since $m \geq 2n$, we have $m - n \geq n$, so

$$\operatorname{codim} S_r = r(m - n + r) \geq r(n + r) \geq n + 1$$

for all $r \geq 1$.

By the Thom Transversality Theorem (or its parametric refinement Lemma 4.15), the set of smooth maps $f: X \to Y$ whose 1-jet $j^1 f$ is transverse to each $S_r$ is dense in $C^\infty(X, Y)$. When $\dim X < \operatorname{codim} S_r$, transversality to $S_r$ is equivalent to $j^1 f(X) \cap S_r = \varnothing$. Since $\dim X = n$ and $\operatorname{codim} S_r \geq n + 1$, this dimension condition holds for all $r \geq 1$. Hence for a dense set of maps, $j^1 f(X) \cap S_r = \varnothing$ for all $r \neq 0$, which by Lemma 5.1 means $f$ is an immersion. Therefore $\operatorname{Im}(X, Y)$ is dense in $C^\infty(X, Y)$.

Together with openness from Lemma 5.5, $\operatorname{Im}(X, Y)$ is open and dense.
