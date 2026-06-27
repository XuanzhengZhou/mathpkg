---
role: proof
locale: en
of_concept: khinchins-law-of-large-numbers
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§3. Khinchin LLN, CLT for i.i.d., Poisson theorem"
---

# Proof of Theorem 2 (Khinchin's Law of Large Numbers)

Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with $\mathbb{E}|\xi_1| < \infty$. Set $S_n = \xi_1 + \cdots + \xi_n$ and $m = \mathbb{E}\xi_1$. We must show that

$$\frac{S_n}{n} \xrightarrow{P} m, \qquad n \to \infty.$$

**Proof.** Let $\varphi(t) = \mathbb{E} e^{it\xi_1}$ be the characteristic function of $\xi_1$. Since the $\xi_i$ are independent and identically distributed, the characteristic function of the normalized sum $S_n/n$ is

$$\varphi_{S_n/n}(t) = \mathbb{E} e^{it S_n/n} = \mathbb{E} e^{i (t/n)(\xi_1 + \cdots + \xi_n)} = \bigl[ \mathbb{E} e^{i (t/n) \xi_1} \bigr]^n = \bigl[ \varphi(t/n) \bigr]^n.$$

Because $\mathbb{E}|\xi_1| < \infty$, the characteristic function $\varphi$ is differentiable at $0$ with derivative

$$\varphi'(0) = i \mathbb{E}\xi_1 = i m.$$

Using the first-order Taylor expansion of $\varphi$ around $0$:

$$\varphi(s) = \varphi(0) + \varphi'(0) s + o(s) = 1 + i m s + o(s), \qquad s \to 0.$$

Substituting $s = t/n$ yields, for each fixed $t$,

$$\varphi\!\left(\frac{t}{n}\right) = 1 + i m \frac{t}{n} + o\!\left(\frac{1}{n}\right), \qquad n \to \infty.$$

Therefore

$$\varphi_{S_n/n}(t) = \left[ 1 + \frac{i m t}{n} + o\!\left(\frac{1}{n}\right) \right]^n \;\longrightarrow\; e^{i m t}, \qquad n \to \infty.$$

The limiting function $e^{i m t}$ is the characteristic function of the degenerate random variable that equals $m$ with probability $1$. By Theorem 1 (the Continuity Theorem for characteristic functions), the convergence of characteristic functions implies convergence in distribution:

$$\frac{S_n}{n} \xrightarrow{d} m.$$

Convergence in distribution to a constant is equivalent to convergence in probability (see Problem 7 in Sect. 10, Chap. 2). Hence

$$\frac{S_n}{n} \xrightarrow{P} m,$$

which completes the proof of Khinchin's Law of Large Numbers.
