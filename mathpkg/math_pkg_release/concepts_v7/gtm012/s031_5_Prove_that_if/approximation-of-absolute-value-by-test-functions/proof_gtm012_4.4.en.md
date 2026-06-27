---
role: proof
locale: en
of_concept: approximation-of-absolute-value-by-test-functions
source_book: gtm012
source_chapter: "4"
source_section: "§4. Characterization of distributions of type L'"
---

# Proof of Approximation of the absolute value function by test functions

**Lemma 4.2.** Let $h$ be defined by

$$h(t) = \begin{cases} |t|, & t \leq 0, \\ 0, & t > 0. \end{cases}$$

There is a sequence $(h_n)_{1}^{\infty} \subset \mathcal{L}$ such that

$$|h_n - h|_{0,a,M} \to 0 \quad \text{as } n \to \infty$$

for each $a \in \mathbb{R}, M \in \mathbb{R}$.

*Proof.* Choose a smooth function $\varphi: \mathbb{R} \to \mathbb{R}$ with the following properties:

1. $\varphi \geq 0$,
2. $\operatorname{supp}(\varphi) \subset [-1, 1]$,
3. $\int_{-\infty}^{\infty} \varphi(t) \, dt = 1$,
4. $\varphi \in C^{\infty}(\mathbb{R})$.

Such a function exists; for example, take the standard mollifier

$$\varphi(t) = \begin{cases} c \exp\left(-\frac{1}{1-t^2}\right), & |t| < 1, \\ 0, & |t| \geq 1, \end{cases}$$

with $c$ chosen to normalize the integral.

For each positive integer $n$, define $\varphi_n(t) = n \varphi(nt)$. Then $\operatorname{supp}(\varphi_n) \subset [-1/n, 1/n]$ and $\int \varphi_n = 1$.

Set $h_n = h * \varphi_n$, the convolution:

$$h_n(t) = \int_{-\infty}^{\infty} h(s) \varphi_n(t-s) \, ds = \int_{-\infty}^{0} |s| \varphi_n(t-s) \, ds.$$

Since $h$ is continuous on $\mathbb{R}$ (note that $\lim_{t \to 0-} h(t) = 0 = h(0)$ and $h(t) = 0$ for $t > 0$, so $h$ is continuous at $0$) and $\varphi_n$ is smooth with compact support, $h_n$ is smooth. Moreover, the support of $h_n$ is contained in $(-\infty, 1/n]$, because $\operatorname{supp}(h) = (-\infty, 0]$ and $\operatorname{supp}(\varphi_n) \subset [-1/n, 1/n]$. Thus $h_n \in \mathcal{L}$ for each $n$.

We now estimate the seminorm difference. Fix $a, M \in \mathbb{R}$. Recall

$$|u|_{0,a,M} = \sup_{t \geq M} e^{at} |u(t)|.$$

Consider three regimes for $t \geq M$:

**Case 1: $t > 1/n$.** Then $h(t) = 0$, and since $\operatorname{supp}(\varphi_n) \subset [-1/n, 1/n]$, the convolution satisfies

$$h_n(t) = \int_{t-1/n}^{t+1/n} h(s) \varphi_n(t-s) \, ds.$$

For $s$ in the integration range, $s \geq t-1/n > 0$, so $h(s) = 0$. Hence $h_n(t) = 0$. Thus $|h_n(t) - h(t)| = 0$ on $t > 1/n$, provided $M \leq 1/n$.

**Case 2: $t \leq -1/n$.** In this range, $t + 1/n \leq 0$, so for all $s$ with $|t-s| \leq 1/n$, we have $s \leq 0$ and $h(s) = |s| = -s$. Since the mollifier has unit mass and is symmetric,

$$h_n(t) = \int_{-\infty}^{\infty} (-s) \varphi_n(t-s) \, ds = \int_{-\infty}^{\infty} (-t + (t-s)) \varphi_n(t-s) \, ds = (-t)\int \varphi_n + \int (t-s)\varphi_n(t-s)\,ds = -t + 0 = |t|,$$

where the integral of $(t-s)\varphi_n(t-s)$ vanishes because $\varphi_n$ is even (after a possible reflection — more precisely, $\int u \varphi_n(u) du = 0$ by symmetry of $\varphi$). So $h_n(t) = h(t) = |t|$ for all $t \leq -1/n$. In particular, $|h_n(t) - h(t)| = 0$ on this region.

**Case 3: $-1/n \leq t \leq 1/n$.** On this compact interval, $|h(t)| \leq 1/n$. Moreover, for any $t$,

$$|h_n(t)| \leq \int_{-1/n}^{1/n} |h(t-u)| \varphi_n(u) \, du \leq \sup_{|u| \leq 1/n} |h(t-u)|.$$

For $t \in [-1/n, 1/n]$, the arguments $t-u$ range over $[-2/n, 2/n]$, where $|h| \leq 2/n$. Thus $|h_n(t)| \leq 2/n$, and $|h_n(t) - h(t)| \leq |h_n(t)| + |h(t)| \leq 3/n$.

**Assembling the estimate.** For any $t \geq M$:

- If $M \geq 1/n$, then either $t \leq -1/n$ (but this requires $t \leq -1/n$ and $t \geq M \geq 1/n$, impossible) or $t \geq M \geq 1/n / n$, in which case we are in Case 1 and the difference is $0$. Actually, for $M > 1/n$, we are in the range $t \geq M > 1/n$, so $h_n(t) = 0 = h(t)$. Hence $|h_n - h|_{0,a,M} = 0$.

- If $M \leq 1/n$, then for $t \in [M, 1/n]$, we have $e^{at} |h_n(t) - h(t)| \leq e^{|a|/n} \cdot 3/n$. For $t > 1/n$, the difference is $0$.

Therefore, in all cases,

$$|h_n - h|_{0,a,M} \leq \frac{3}{n} e^{|a|/n} \quad \text{for sufficiently large } n,$$

and the right-hand side tends to $0$ as $n \to \infty$. More precisely, for each fixed $a, M$, there exists $N$ such that for all $n \geq N$, we have $1/n < \max(|M|, 1)$ and the estimate above holds. Hence

$$\lim_{n \to \infty} |h_n - h|_{0,a,M} = 0$$

for every $a, M \in \mathbb{R}$. $\square$
