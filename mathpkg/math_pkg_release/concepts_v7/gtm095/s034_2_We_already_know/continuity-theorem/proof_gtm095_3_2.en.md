---
role: proof
locale: en
of_concept: continuity-theorem
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of the Continuity Theorem for Characteristic Functions

Let $\{F_n\}$ be a sequence of distribution functions with corresponding characteristic functions

$$\varphi_n(t) = \int_{-\infty}^{\infty} e^{itx} \, dF_n(x), \quad t \in \mathbb{R}.$$

---

## Proof of Conclusion (1)

Suppose $F_n \xrightarrow{w} F$, where $F = F(x)$ is a distribution function with characteristic function $\varphi(t) = \int_{-\infty}^{\infty} e^{itx} \, dF(x)$.

For each fixed $t \in \mathbb{R}$, the functions

$$f_t(x) = \operatorname{Re} e^{itx} = \cos tx, \qquad g_t(x) = \operatorname{Im} e^{itx} = \sin tx$$

are bounded and continuous on $\mathbb{R}$. By the definition of weak convergence,

$$
\begin{aligned}
\lim_{n \to \infty} \operatorname{Re} \varphi_n(t) &= \lim_{n \to \infty} \int_{-\infty}^{\infty} \cos tx \, dF_n(x) = \int_{-\infty}^{\infty} \cos tx \, dF(x) = \operatorname{Re} \varphi(t), \\[4pt]
\lim_{n \to \infty} \operatorname{Im} \varphi_n(t) &= \lim_{n \to \infty} \int_{-\infty}^{\infty} \sin tx \, dF_n(x) = \int_{-\infty}^{\infty} \sin tx \, dF(x) = \operatorname{Im} \varphi(t).
\end{aligned}
$$

Hence $\varphi_n(t) \to \varphi(t)$ for all $t \in \mathbb{R}$. $\square$

---

## Proof of Conclusion (2)

Suppose $\lim_n \varphi_n(t)$ exists for each $t \in \mathbb{R}$ and the limit function

$$\varphi(t) = \lim_{n \to \infty} \varphi_n(t)$$

is continuous at $t = 0$.

### Step 1: Tightness

Let $P_n$ be the probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ corresponding to $F_n$, i.e., $P_n((-\infty, x]) = F_n(x)$. We first show that $\{P_n\}$ is tight.

By Lemma 3 (Tail Estimate), for any $a > 0$,

$$P_n\!\left( \mathbb{R} \setminus \left(-\frac{1}{a}, \frac{1}{a}\right) \right) = \int_{|x| \geq 1/a} dF_n(x) \leq \frac{K}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi_n(t) \bigr] \, dt,$$

with $K = 7$.

Since $\varphi_n(t) \to \varphi(t)$ pointwise, we have $\operatorname{Re} \varphi_n(t) \to \operatorname{Re} \varphi(t)$. By the dominated convergence theorem (the integrand is bounded by $2$ on $[0, a]$),

$$\lim_{n \to \infty} \frac{1}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi_n(t) \bigr] \, dt = \frac{1}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi(t) \bigr] \, dt.$$

Because $\varphi$ is continuous at $0$ and $\varphi(0) = \lim_n \varphi_n(0) = \lim_n 1 = 1$, we have $\operatorname{Re} \varphi(t) \to 1$ as $t \to 0$. Hence for any $\varepsilon > 0$ we can choose $a > 0$ sufficiently small so that

$$\frac{K}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi(t) \bigr] \, dt < \varepsilon.$$

For this $a$, the inequality above yields

$$\limsup_{n \to \infty} P_n\!\left( \mathbb{R} \setminus \left(-\frac{1}{a}, \frac{1}{a}\right) \right) \leq \varepsilon.$$

This means that for sufficiently large $n$, the mass of $P_n$ outside $[-1/a, 1/a]$ is arbitrarily small, which is precisely the tightness condition. Therefore $\{P_n\}$ is a tight family.

### Step 2: Weak convergence via Lemma 2

Since $\{P_n\}$ is tight and $\lim_n \varphi_n(t) = \varphi(t)$ exists for all $t \in \mathbb{R}$, Lemma 2 implies that $\{P_n\}$ converges weakly to some probability measure $P$. Let $F$ be the distribution function of $P$. By the definition of weak convergence,

$$F_n \xrightarrow{w} F.$$

### Step 3: Identification of the limit characteristic function

By conclusion (1) of the theorem, weak convergence $F_n \xrightarrow{w} F$ implies that the characteristic functions converge pointwise:

$$\lim_{n \to \infty} \varphi_n(t) = \int_{-\infty}^{\infty} e^{itx} \, dF(x).$$

But we already know that $\lim_n \varphi_n(t) = \varphi(t)$. Hence

$$\varphi(t) = \int_{-\infty}^{\infty} e^{itx} \, dF(x) \quad \text{for all } t \in \mathbb{R},$$

so $\varphi$ is indeed the characteristic function of the probability distribution $F$. $\square$

---

The theorem is thus established: weak convergence of distribution functions is equivalent to pointwise convergence of the corresponding characteristic functions to a function continuous at the origin.
