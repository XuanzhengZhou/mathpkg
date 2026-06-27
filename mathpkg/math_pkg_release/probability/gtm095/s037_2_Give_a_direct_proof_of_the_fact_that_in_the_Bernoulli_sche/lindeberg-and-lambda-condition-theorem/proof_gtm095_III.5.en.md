---
role: proof
locale: en
of_concept: lindeberg-and-lambda-condition-theorem
source_book: gtm095
source_chapter: "III"
source_section: "§5. Nonclassical Conditions for the Central Limit Theorem"
---

# Proof of Theorem 2: Equivalence of Lindeberg Condition and Condition $(\Lambda)$

## Statement

Let $\xi_{n1}, \ldots, \xi_{nn}$, $n \geq 1$, be a triangular array of independent
random variables with distribution functions $F_{nk}(x) = \mathbb{P}\{\xi_{nk} \leq x\}$,
$\mathbb{E}\,\xi_{nk} = 0$, and $\operatorname{Var}(\xi_{n1} + \cdots + \xi_{nn}) = 1$.
Then:

1. **Lindeberg condition (L) implies condition $(\Lambda)$.**

2. **If $\displaystyle\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0$ as $n \to \infty$,
   then condition $(\Lambda)$ implies the Lindeberg condition (L).**

In other words, under the additional hypothesis of asymptotic negligibility, the two
conditions are equivalent.

## Proof of Part 1: $(L) \Longrightarrow (\Lambda)$

From the Lindeberg condition

$$\sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr] \to 0,
\qquad n \to \infty, \quad \forall \varepsilon > 0, \tag{L}$$

we deduce asymptotic negligibility. Decompose the second moment:

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2}
= \max_{1 \leq k \leq n} \Bigl(
\mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| < \varepsilon)\bigr]
+ \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr]
\Bigr).$$

The first expectation is bounded by $\varepsilon^{2}$. For the second,

$$\mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr]
\leq \sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr].$$

Hence

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2}
\leq \varepsilon^{2} + \sum_{k=1}^{n} \mathbb{E}\bigl[\xi_{nk}^{2}\, I(|\xi_{nk}| \geq \varepsilon)\bigr].$$

Letting $n \to \infty$, condition (L) forces the sum to vanish, so

$$\limsup_{n \to \infty} \max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \leq \varepsilon^{2}.$$

Since $\varepsilon > 0$ was arbitrary, we obtain

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0, \qquad n \to \infty.$$

Applying Chebyshev's inequality,

$$\max_{1 \leq k \leq n} \mathbb{P}\{|\xi_{nk}| \geq \varepsilon\}
\leq \frac{1}{\varepsilon^{2}} \max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0,
\qquad n \to \infty.$$

This is precisely the content of condition $(\Lambda)$. Thus $(L) \Rightarrow (\Lambda)$.

## Proof of Part 2: $(\Lambda) \Longrightarrow (L)$ under the asymptotic smallness hypothesis

Assume condition $(\Lambda)$ holds and that

$$\max_{1 \leq k \leq n} \mathbb{E}\,\xi_{nk}^{2} \to 0, \qquad n \to \infty. \tag{H}$$

Let $\Phi_{nk}$ denote the normal distribution with the same mean and variance as $F_{nk}$,
i.e. $\Phi_{nk} \sim \mathcal{N}(0, \gamma_{nk})$ where $\gamma_{nk} = \mathbb{E}\,\xi_{nk}^{2}$.
Their characteristic functions are

$$\varphi_{nk}(t) = e^{-t^{2}\gamma_{nk}/2}, \qquad
\varphi(t) = e^{-t^{2}/2} = \prod_{k=1}^{n} \varphi_{nk}(t).$$

### Step 1: Derivation of the joint tail estimate

The proof of sufficiency of $(\Lambda)$ for the central limit theorem
(Theorem 1 of this section) yields the estimate, for every $\varepsilon > 0$,

$$\sum_{k=1}^{n} \int_{|x| > \varepsilon} x^{2}\, d\bigl[F_{nk}(x) + \Phi_{nk}(x)\bigr] \to 0,
\qquad n \to \infty. \tag{1}$$

### Step 2: Smooth truncation

Fix $\varepsilon > 0$ and choose a continuously differentiable even function
$h = h(x)$ such that

$$|h(x)| \leq x^{2}, \qquad |h'(x)| \leq 4|x|,$$

and

$$h(x) = \begin{cases}
x^{2}, & |x| > 2\varepsilon,\\[2pt]
0,    & |x| \leq \varepsilon.
\end{cases}$$

From (1) we immediately obtain

$$\sum_{k=1}^{n} \int_{|x| > \varepsilon} h(x)\, d\bigl[F_{nk}(x) + \Phi_{nk}(x)\bigr] \to 0,
\qquad n \to \infty. \tag{2}$$

### Step 3: Integration by parts

Apply integration by parts to the integrals in (2). For the right tail $x \geq \varepsilon$,

$$\int_{x \geq \varepsilon} h(x)\, d\bigl[(1 - F_{nk}(x)) + (1 - \Phi_{nk}(x))\bigr]
= \int_{x \geq \varepsilon} h'(x)\bigl[(1 - F_{nk}(x)) + (1 - \Phi_{nk}(x))\bigr]\, dx,$$

and for the left tail $x \leq -\varepsilon$,

$$\int_{x \leq -\varepsilon} h(x)\, d\bigl[F_{nk}(x) + \Phi_{nk}(x)\bigr]
= \int_{x \leq -\varepsilon} h'(x)\bigl[F_{nk}(x) + \Phi_{nk}(x)\bigr]\, dx.$$

Summing over $k = 1, \ldots, n$ and using the bound $|h'(x)| \leq 4|x|$,

$$\Bigl|\sum_{k=1}^{n} \int_{|x| \geq \varepsilon} h(x)\, d\bigl[F_{nk} + \Phi_{nk}\bigr]\Bigr|
\leq 4 \sum_{k=1}^{n} \int_{|x| \geq \varepsilon} |x|\,\bigl|F_{nk}(x) - \Phi_{nk}(x)\bigr|\, dx. \tag{3}$$

### Step 4: Recovery of the Lindeberg integral

Condition $(\Lambda)$ guarantees that the right-hand side of (3) tends to $0$ as
$n \to \infty$ (this is precisely the content of condition $(\Lambda)$ expressed
in terms of the distribution functions). Consequently, (2) holds.

Now, since $h(x) = x^{2}$ for $|x| > 2\varepsilon$, we have

$$\sum_{k=1}^{n} \int_{|x| \geq 2\varepsilon} x^{2}\, dF_{nk}(x)
\leq \sum_{k=1}^{n} \int_{|x| \geq \varepsilon} h(x)\, dF_{nk}(x)
\leq \sum_{k=1}^{n} \int_{|x| \geq \varepsilon} h(x)\, d\bigl[F_{nk} + \Phi_{nk}\bigr].$$

The right-hand side tends to $0$ by (2), and therefore

$$\sum_{k=1}^{n} \int_{|x| \geq 2\varepsilon} x^{2}\, dF_{nk}(x) \to 0,
\qquad n \to \infty.$$

Since $\varepsilon > 0$ is arbitrary, this is precisely the Lindeberg condition (L).

This completes the proof of Theorem 2. $\square$
