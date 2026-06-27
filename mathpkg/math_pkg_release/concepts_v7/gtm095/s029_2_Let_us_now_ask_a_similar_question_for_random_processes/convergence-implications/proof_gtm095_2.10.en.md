---
role: proof
locale: en
of_concept: convergence-implications
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Implications Between Modes of Convergence

**Theorem 2.** We have the following implications:

$$\xi_n \xrightarrow{\text{a.s.}} \xi \;\Rightarrow\; \xi_n \xrightarrow{P} \xi,$$

$$\xi_n \xrightarrow{L^p} \xi \;\Rightarrow\; \xi_n \xrightarrow{P} \xi, \quad p > 0,$$

$$\xi_n \xrightarrow{P} \xi \;\Rightarrow\; \xi_n \xrightarrow{d} \xi.$$

*Proof.* (11) follows from comparing the definition of convergence in probability with condition (5) in Theorem 1. If $\xi_n \xrightarrow{\text{a.s.}} \xi$, then for every $\varepsilon > 0$,

$$P\{|\xi_n - \xi| \geq \varepsilon\} \leq P\left\{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\right\} \to 0, \quad n \to \infty.$$

(12) follows from Chebyshev's (Markov's) inequality:

$$P\{|\xi_n - \xi| \geq \varepsilon\} \leq \frac{E|\xi_n - \xi|^p}{\varepsilon^p} \to 0.$$

To prove (13), let $f(x)$ be a continuous function, let $|f(x)| \leq c$, let $\varepsilon > 0$, and let $N$ be such that $P(|\xi| > N) \leq \varepsilon/(4c)$. Take $\delta$ so that $|f(x) - f(y)| \leq \varepsilon/2$ for $|x| \leq N$ and $|x - y| \leq \delta$. Then (cf. the "probabilistic" proof of Weierstrass's theorem in Subsection 5, Sect. 5, Chap. 1)

$$E|f(\xi_n) - f(\xi)| = E\left(|f(\xi_n) - f(\xi)|; |\xi_n - \xi| \leq \delta, |\xi| \leq N\right)$$

$$+ E\left(|f(\xi_n) - f(\xi)|; |\xi_n - \xi| \leq \delta, |\xi| > N\right)$$

$$+ E\left(|f(\xi_n) - f(\xi)|; |\xi_n - \xi| > \delta\right)$$

$$\leq \varepsilon/2 + \varepsilon/2 + 2c\, P\{|\xi_n - \xi| > \delta\}$$

$$= \varepsilon + 2c\, P\{|\xi_n - \xi| > \delta\}.$$

But $P\{|\xi_n - \xi| > \delta\} \to 0$, and hence $E|f(\xi_n) - f(\xi)| \leq 2\varepsilon$ for sufficiently large $n$. Since $\varepsilon > 0$ is arbitrary, $E f(\xi_n) \to E f(\xi)$, i.e., $\xi_n \xrightarrow{d} \xi$. $\square$
