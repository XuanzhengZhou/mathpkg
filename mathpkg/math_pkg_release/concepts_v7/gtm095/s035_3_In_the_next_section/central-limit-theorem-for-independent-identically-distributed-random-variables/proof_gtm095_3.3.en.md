---
role: proof
locale: en
of_concept: central-limit-theorem-for-independent-identically-distributed-random-variables
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§3. Khinchin LLN, CLT for i.i.d., Poisson theorem"
---

# Proof of Theorem 3 (Central Limit Theorem for i.i.d. Random Variables)

Let $\xi_1, \xi_2, \ldots$ be a sequence of independent identically distributed (nondegenerate) random variables with $\mathbb{E}\xi_1^2 < \infty$. Set $S_n = \xi_1 + \cdots + \xi_n$. We must show that as $n \to \infty$,

$$P\!\left\{ \frac{S_n - \mathbb{E}S_n}{\sqrt{\operatorname{Var} S_n}} \leq x \right\} \;\longrightarrow\; \Phi(x), \qquad x \in \mathbb{R},$$

where $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-u^2/2} \, du$ is the standard normal distribution function.

**Proof.** Let $m = \mathbb{E}\xi_1$ and $\sigma^2 = \operatorname{Var}\xi_1 > 0$ (nondegeneracy). Define the centered characteristic function

$$\varphi(t) = \mathbb{E} e^{i t (\xi_1 - m)}.$$

For the normalized sum, set

$$\varphi_n(t) = \mathbb{E} \exp\!\left\{ i t \, \frac{S_n - \mathbb{E}S_n}{\sqrt{\operatorname{Var} S_n}} \right\}.$$

Since $\mathbb{E}S_n = n m$ and $\operatorname{Var} S_n = n \sigma^2$, and the $\xi_k$ are i.i.d.,

$$\varphi_n(t) = \mathbb{E} \exp\!\left\{ i t \sum_{k=1}^{n} \frac{\xi_k - m}{\sigma \sqrt{n}} \right\} = \left[ \mathbb{E} \exp\!\left\{ i \frac{t}{\sigma \sqrt{n}} (\xi_1 - m) \right\} \right]^n = \left[ \varphi\!\left( \frac{t}{\sigma \sqrt{n}} \right) \right]^n.$$

Since $\mathbb{E}\xi_1^2 < \infty$, the characteristic function $\varphi$ is twice differentiable at $0$. Moreover, $\varphi(0) = 1$, $\varphi'(0) = i \mathbb{E}(\xi_1 - m) = 0$, and $\varphi''(0) = -\mathbb{E}(\xi_1 - m)^2 = -\sigma^2$. By the Taylor expansion (14) of Sect. 12, Chap. 2,

$$\varphi(s) = 1 + \varphi'(0) s + \frac{\varphi''(0)}{2} s^2 + o(s^2) = 1 - \frac{\sigma^2 s^2}{2} + o(s^2), \qquad s \to 0.$$

Substituting $s = t/(\sigma \sqrt{n})$ gives, for each fixed $t$,

$$\varphi\!\left( \frac{t}{\sigma \sqrt{n}} \right) = 1 - \frac{\sigma^2}{2} \cdot \frac{t^2}{\sigma^2 n} + o\!\left(\frac{1}{n}\right) = 1 - \frac{t^2}{2n} + o\!\left(\frac{1}{n}\right), \qquad n \to \infty.$$

Raising to the $n$-th power and using the well-known limit $(1 + a/n)^n \to e^a$,

$$\varphi_n(t) = \left[ 1 - \frac{t^2}{2n} + o\!\left(\frac{1}{n}\right) \right]^n \;\longrightarrow\; e^{-t^2/2}, \qquad n \to \infty.$$

The limiting function $e^{-t^2/2}$ is precisely the characteristic function of the standard normal distribution $\mathcal{N}(0,1)$. The characteristic function $e^{-t^2/2}$ is continuous at $0$. Hence, by Theorem 1 (the Continuity Theorem for characteristic functions),

$$\frac{S_n - \mathbb{E}S_n}{\sqrt{\operatorname{Var} S_n}} \;\xrightarrow{d}\; \mathcal{N}(0,1),$$

which is exactly the statement (5) of the Central Limit Theorem.
