---
role: proof
locale: en
of_concept: lindeberg-condition
source_book: gtm095
source_chapter: "III"
source_section: "§2. Nonclassical CLT conditions"
---

# Proof: Lindeberg Condition Implies Condition $(\Lambda)$

## Statement (Theorem 2, Part 1)

Let $\xi_{n1}, \ldots, \xi_{nn}$ be a triangular array of independent random variables
with $\mathbb{E}\,\xi_{nk} = 0$, $\operatorname{Var} S_n = 1$ where $S_n = \xi_{n1} + \cdots + \xi_{nn}$.
If the Lindeberg condition

$$\sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr] \to 0, \qquad n \to \infty, \tag{L}$$

holds for every $\varepsilon > 0$, then condition $(\Lambda)$ is satisfied.

## Proof

From the Lindeberg condition we first deduce the asymptotic negligibility of the individual
terms. For any $\varepsilon > 0$,

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2}
= \max_{1 \leq k \leq n} \Bigl(
\mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| < \varepsilon)\bigr]
+ \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr]
\Bigr).$$

The first term is bounded by $\varepsilon^{2}$, since on $\{|\xi_{nk}| < \varepsilon\}$
we have $\xi_{nk}^{2} < \varepsilon^{2}$. The second term is controlled by the Lindeberg sum:

$$\mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr]
\leq \sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr].$$

Thus

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2}
\leq \varepsilon^{2} + \sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr].$$

Letting $n \to \infty$ and using condition (L), the sum on the right tends to $0$, yielding

$$\limsup_{n \to \infty} \max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \leq \varepsilon^{2}.$$

Since $\varepsilon > 0$ is arbitrary, we obtain

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0, \qquad n \to \infty. \tag{*}$$

Condition $(*)$ is precisely the condition of **asymptotic negligibility**, which is the
content of condition $(\Lambda)$ for the triangular array. In terms of probabilities,
for every $\varepsilon > 0$,

$$\max_{1 \leq k \leq n} \mathbb{P}\{|\xi_{nk}| \geq \varepsilon\}
\leq \frac{1}{\varepsilon^{2}} \max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0,
\qquad n \to \infty,$$

by Chebyshev's inequality. This establishes that the Lindeberg condition (L) implies
condition $(\Lambda)$. $\square$
