---
role: proof
locale: en
of_concept: poissons-theorem
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§3. Khinchin LLN, CLT for i.i.d., Poisson theorem"
---

# Proof of Theorem 4 (Poisson's Theorem)

For each $n \geq 1$, let $\xi_{n1}, \ldots, \xi_{nn}$ be independent Bernoulli random variables with

$$P(\xi_{nk} = 1) = p_{nk}, \quad P(\xi_{nk} = 0) = q_{nk}, \quad p_{nk} + q_{nk} = 1.$$

Assume the asymptotic conditions

$$\max_{1 \leq k \leq n} p_{nk} \to 0, \qquad \sum_{k=1}^{n} p_{nk} \to \lambda > 0, \qquad n \to \infty.$$

We must show that for each $m = 0, 1, 2, \ldots$,

$$P(S_n = m) \to \frac{e^{-\lambda} \lambda^m}{m!}, \qquad n \to \infty,$$

where $S_n = \xi_{n1} + \cdots + \xi_{nn}$.

**Proof.** The characteristic function of each $\xi_{nk}$ is

$$\mathbb{E} e^{i t \xi_{nk}} = p_{nk} e^{i t} + q_{nk} = 1 + p_{nk} (e^{i t} - 1).$$

Since the $\xi_{n1}, \ldots, \xi_{nn}$ are independent within each row, the characteristic function of $S_n$ is

$$\varphi_{S_n}(t) = \mathbb{E} e^{i t S_n} = \prod_{k=1}^{n} \bigl( 1 + p_{nk}(e^{i t} - 1) \bigr).$$

Set $\lambda_n = \sum_{k=1}^{n} p_{nk}$; by hypothesis $\lambda_n \to \lambda$. Because $\max_k p_{nk} \to 0$, for sufficiently large $n$ we have $|p_{nk}(e^{it} - 1)| \leq 1/2$ for all $k$. Using the expansion $\log(1+z) = z + \theta |z|^2$ (valid for $|z| \leq 1/2$, with $|\theta| \leq 1$, taking the principal branch of the logarithm), we obtain

$$\log \varphi_{S_n}(t) = \sum_{k=1}^{n} \log\!\bigl(1 + p_{nk}(e^{i t} - 1)\bigr) = \sum_{k=1}^{n} \Bigl[ p_{nk}(e^{i t} - 1) + \theta_{nk} \, p_{nk}^2 |e^{i t} - 1|^2 \Bigr],$$

where $|\theta_{nk}| \leq 1$. The first sum equals $\lambda_n (e^{i t} - 1)$. For the remainder term,

$$\left| \sum_{k=1}^{n} \theta_{nk} \, p_{nk}^2 |e^{i t} - 1|^2 \right| \leq |e^{i t} - 1|^2 \sum_{k=1}^{n} p_{nk}^2 \leq |e^{i t} - 1|^2 \left( \max_{1 \leq k \leq n} p_{nk} \right) \sum_{k=1}^{n} p_{nk} \to 0$$

as $n \to \infty$, because $\max p_{nk} \to 0$ while $\sum p_{nk} \to \lambda < \infty$. Hence, for each fixed $t$,

$$\log \varphi_{S_n}(t) \;\longrightarrow\; \lambda (e^{i t} - 1), \qquad n \to \infty,$$

and consequently

$$\varphi_{S_n}(t) \;\longrightarrow\; \exp\!\bigl\{ \lambda (e^{i t} - 1) \bigr\}.$$

The right-hand side is precisely the characteristic function of the Poisson distribution with parameter $\lambda$. By the Continuity Theorem (Theorem 1), this implies $S_n \xrightarrow{d} \operatorname{Poisson}(\lambda)$, i.e.,

$$P(S_n = m) \;\longrightarrow\; \frac{e^{-\lambda} \lambda^m}{m!}, \qquad m = 0, 1, 2, \ldots,$$

which completes the proof of Poisson's Theorem.
