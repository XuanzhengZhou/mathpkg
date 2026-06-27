---
role: proof
locale: en
of_concept: differentiation-of-translation
source_book: gtm012
source_chapter: "3"
source_section: "3. Translation, convolution, and approximation"
---

# Proof of Lemma 3.2: Uniform Convergence of Difference Quotient to Derivative

Recall that for $u \in \mathcal{P}$ (smooth periodic functions), $D u$ denotes the derivative. Note that

$$t^{-1}[u(x + t) - u(x)] = t^{-1}[T_{-t} u - u](x).$$

**Lemma 3.2.** If $u \in \mathcal{P}$, then

$$|t^{-1}(T_{-t} u - u) - D u| \to 0 \quad \text{as} \quad t \to 0.$$

**Proof.** By the Mean Value Theorem, for each $x$ and $t \neq 0$ there exists $y = y(t, x)$ lying between $x$ and $x + t$ such that

$$t^{-1}[T_{-t} u - u](x) = \frac{u(x + t) - u(x)}{t} = D u(y).$$

Therefore,

$$t^{-1}[T_{-t} u - u](x) - D u(x) = D u(y) - D u(x),$$

where $y = y(t, x)$ lies between $x$ and $x + t$. In particular, $|y - x| \leq |t|$.

Since $u \in \mathcal{P}$, the derivative $D u$ is uniformly continuous on the compact circle $[0, 2\pi]$ (with periodic identification). Given $\varepsilon > 0$, there exists $\delta > 0$ such that whenever $|y - x| < \delta$, we have $|D u(y) - D u(x)| < \varepsilon$.

Choose $|t| < \delta$. Then for every $x$, the point $y(t, x)$ satisfies $|y - x| \leq |t| < \delta$, and thus

$$|t^{-1}[T_{-t} u - u](x) - D u(x)| = |D u(y) - D u(x)| < \varepsilon.$$

Since $\varepsilon > 0$ was arbitrary and the bound is independent of $x$, this proves

$$|t^{-1}(T_{-t} u - u) - D u| \to 0 \quad \text{as} \quad t \to 0,$$

i.e., the difference quotient converges uniformly to the derivative. $\square$
