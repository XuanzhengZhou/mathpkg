---
role: proof
locale: en
of_concept: l-one-primitive-character-formula
source_book: gtm059
source_chapter: "3"
source_section: "3. Complex Analytic Class Number Formulas"
---

For $\Re(s) > 1$, the $L$-series converges absolutely:

$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}.$$

Using Abel summation (summation by parts), one shows that the series converges for $\Re(s) > 0$ (the Abel-Dirichlet lemma applies since the partial sums $\sum_{n \leq x} \chi(n)$ are bounded for a non-principal character, and $n^{-s}$ decreases). Hence $L(1, \chi)$ is defined by continuity.

Write the $L$-series as a sum over residue classes modulo $m$:

$$L(s, \chi) = \sum_{a=1}^{m} \chi(a) \sum_{k=0}^{\infty} \frac{1}{(a + km)^s}.$$

Now use the integral representation for the Hurwitz-type sum, or equivalently expand using the geometric series for $\log(1 - z)$:

$$-\log(1 - z) = \sum_{n=1}^{\infty} \frac{z^n}{n}, \qquad |z| < 1.$$

For a primitive $m$-th root of unity $\zeta$, we have for each $a$ with $(a, m) = 1$:

$$\sum_{k=0}^{\infty} \frac{1}{a + km} = \lim_{x \to 1^-} \sum_{k=0}^{\infty} \frac{x^{a+km}}{a+km} = \lim_{x \to 1^-} \frac{1}{m} \sum_{t=1}^{m} \zeta^{-at} \sum_{n=1}^{\infty} \frac{(\zeta^t x)^n}{n} = -\frac{1}{m} \sum_{t=1}^{m} \zeta^{-at} \log(1 - \zeta^t).$$

Multiplying by $\chi(a)$ and summing over $a$:

$$L(1, \chi) = -\frac{1}{m} \sum_{t=1}^{m} \left( \sum_{a=1}^{m} \chi(a) \zeta^{-at} \right) \log(1 - \zeta^t).$$

The inner sum is the Gauss sum: $\sum_{a=1}^{m} \chi(a) \zeta^{-at} = \overline{\chi}(t) \tau(\chi)$. Since $\chi$ is primitive, $\tau(\chi) \neq 0$, and this relation holds for all $t$. Substituting:

$$L(1, \chi) = -\frac{\tau(\chi)}{m} \sum_{t=1}^{m} \overline{\chi}(t) \log(1 - \zeta^t).$$

Re-indexing $t \mapsto a$ and noting that $\log(1 - \zeta^a)$ is defined with the principal branch where $-\pi < \Im(\log(1 - \zeta^a)) < \pi$, we obtain the stated formula.
