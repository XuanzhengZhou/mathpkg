---
role: proof
locale: en
of_concept: de-moivre-laplace-integral-theorem
source_book: gtm095
source_chapter: "1"
source_section: "6. De Moivre–Laplace Limit Theorem"
---

# Proof of the De Moivre–Laplace Integral Theorem

**De Moivre–Laplace Integral Theorem.** Let $0 < p < 1$, $q = 1-p$, and

$$P_n(k) = C_n^k p^k q^{n-k}, \quad P_n(a, b] = \sum_{a < x \leq b} P_n(np + x\sqrt{npq}),$$

where the summation is over those $x$ for which $np + x\sqrt{npq}$ is an integer. Then

$$\sup_{-\infty \leq a < b \leq \infty} \left| P_n(a, b] - \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx \right| \to 0, \quad n \to \infty.$$

Equivalently, for $-\infty < a \leq b < \infty$,

$$P\left\{ a < \frac{S_n - np}{\sqrt{npq}} \leq b \right\} \to \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx, \quad n \to \infty.$$

**Proof.** The proof builds upon the Local Limit Theorem and proceeds through several steps.

### Step 1 (Local Limit Theorem)

Let $0 < p < 1$. Then uniformly for $k$ such that $|k - np| = o(npq)^{2/3}$,

$$P_n(k) \sim \frac{1}{\sqrt{2\pi npq}} e^{-(k-np)^2/(2npq)}.$$

The proof depends on Stirling's formula

$$n! = \sqrt{2\pi n}\, e^{-n} n^n (1 + R(n)),$$

where $R(n) \to 0$ as $n \to \infty$. Applying this to $P_n(k) = \frac{n!}{k!(n-k)!} p^k q^{n-k}$, one obtains after some algebra (involving the relative entropy $H(\hat{p}) = \hat{p}\log(\hat{p}/p) + (1-\hat{p})\log((1-\hat{p})/(1-p))$ with $\hat{p} = k/n$) the representation

$$P_n(k) = \frac{1}{\sqrt{2\pi npq}} e^{-(k-np)^2/(2npq)} (1 + \varepsilon'(n, k, n-k)),$$

where $\sup |\varepsilon'| \to 0$ as $n \to \infty$ over the range $|k-np| \leq \varphi(n)$ with $\varphi(n) = o(npq)^{2/3}$.

An equivalent formulation: for $x \in \mathbb{R}^1$ with $x = o(npq)^{1/6}$ and $np + x\sqrt{npq}$ an integer,

$$P_n(np + x\sqrt{npq}) \sim \frac{1}{\sqrt{2\pi npq}} e^{-x^2/2}.$$

### Step 2 (From local to integral, finite interval)

Set $t_k$ via $k = np + t_k\sqrt{npq}$, so that $\Delta t_k = t_{k+1} - t_k = 1/\sqrt{npq} \to 0$ as $n \to \infty$. From the local theorem, for all $t_k$ with $|t_k| \leq T < \infty$,

$$P_n(np + t_k\sqrt{npq}) = \frac{\Delta t_k}{\sqrt{2\pi}} e^{-t_k^2/2} [1 + \varepsilon(t_k, n)],$$

where $\sup_{|t_k| \leq T} |\varepsilon(t_k, n)| \to 0$ as $n \to \infty$.

For $-T \leq a \leq b \leq T$, the sum $P_n(a, b] = \sum_{a < t_k \leq b} P_n(np + t_k\sqrt{npq})$ splits as

$$P_n(a, b] = \frac{1}{\sqrt{2\pi}} \sum_{a < t_k \leq b} \Delta t_k \, e^{-t_k^2/2} + R_n^{(2)}(a, b),$$

where

$$R_n^{(2)}(a, b) = \sum_{a < t_k \leq b} \varepsilon(t_k, n) \frac{\Delta t_k}{\sqrt{2\pi}} e^{-t_k^2/2}.$$

The first term is a Riemann sum approximating the integral:

$$R_n^{(1)}(a, b) = \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx - \frac{1}{\sqrt{2\pi}} \sum_{a < t_k \leq b} \Delta t_k \, e^{-t_k^2/2} \to 0, \quad n \to \infty,$$

uniformly in $a, b \in [-T, T]$.

For the second remainder,

$$\sup_{-T \leq a \leq b \leq T} |R_n^{(2)}(a, b)| \leq \sup_{|t_k| \leq T} |\varepsilon(t_k, n)| \cdot \sum_{|t_k| \leq T} \frac{\Delta t_k}{\sqrt{2\pi}} e^{-t_k^2/2}.$$

Since the sum converges to $\frac{1}{\sqrt{2\pi}} \int_{-T}^T e^{-x^2/2} dx \leq 1$, we have $R_n^{(2)} \to 0$ uniformly on $[-T, T]$.

Therefore

$$\sup_{-T \leq a \leq b \leq T} \left| P_n(a, b] - (\Phi(b) - \Phi(a)) \right| \to 0, \quad n \to \infty,$$

where $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-t^2/2} dt$ is the standard normal distribution function.

### Step 3 (Extension to $T = \infty$)

By the convergence of the Gaussian integral, for any $\varepsilon > 0$ there exists a finite $T = T(\varepsilon)$ such that

$$\frac{1}{\sqrt{2\pi}} \int_{-T}^T e^{-x^2/2} dx > 1 - \frac{\varepsilon}{4}.$$

From Step 2, there exists $N$ such that for all $n > N$ and all $-T \leq a \leq b \leq T$,

$$\left| P_n(a, b] - \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx \right| \leq \frac{\varepsilon}{4}.$$

Now for arbitrary $-\infty \leq a < b \leq \infty$, consider the decomposition (assuming without loss of generality that $a \leq -T < T \leq b$):

$$
\begin{aligned}
\Bigg| P_n(a, b] - \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx \Bigg| 
&\leq \left| P_n(-T, T] - \frac{1}{\sqrt{2\pi}} \int_{-T}^T e^{-x^2/2} dx \right| \\
&\quad + \left| P_n(a, -T] - \frac{1}{\sqrt{2\pi}} \int_a^{-T} e^{-x^2/2} dx \right| \\
&\quad + \left| P_n(T, b] - \frac{1}{\sqrt{2\pi}} \int_T^b e^{-x^2/2} dx \right|.
\end{aligned}
$$

The first term is bounded by $\varepsilon/4$. For the tail terms, using the fact that both $P_n$ and the Gaussian integral are probability measures on $\mathbb{R}$,

$$P_n(-\infty, -T] + \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{-T} e^{-x^2/2} dx + P_n(T, \infty) + \frac{1}{\sqrt{2\pi}} \int_T^{\infty} e^{-x^2/2} dx \leq \frac{\varepsilon}{4} + \frac{\varepsilon}{2} + \frac{\varepsilon}{8} + \frac{\varepsilon}{8} = \varepsilon.$$

Thus the total error is bounded by $\varepsilon$ uniformly in $a, b$, which establishes

$$\sup_{-\infty \leq a < b \leq \infty} \left| P_n(a, b] - \frac{1}{\sqrt{2\pi}} \int_a^b e^{-x^2/2} dx \right| \to 0, \quad n \to \infty.$$

This completes the proof. $\square$
