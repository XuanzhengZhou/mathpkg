---
role: proof
locale: en
of_concept: "let-be-a-sequence-of-complex-numbers-such"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.28"
---

Let $s_0 = 0$ and $s_n = \sum_{k=1}^{n} \frac{1}{k} \alpha_k$ for $n \geq 1$, and let $t_n = \alpha_1 + \alpha_2 + \cdots + \alpha_n (n \geq 1)$. With this notation we have

$$\alpha_k = k(s_k - s_{k-1})$$

and therefore

$$t_{n+1} = \sum_{k=1}^{n+1} k(s_k - s_{k-1}) = (n+1) s_{n+1} + \sum_{k=1}^{n} k s_k - \sum_{k=2}^{n+1} k s_{k-1}$$

$$= (n+1) s_{n+1} + \sum_{k=1}^{n} k s_k - \sum_{k=1}^{n} (k+1) s_k = (n+1) s_{n+1} - \sum_{k=1}^{n} s_k;$$

i.e.,

$$t_{n+1} = (n+1) s_{n+1} - \sum_{k=1}^{n} s_k$$

for $n = 1, 2, 3, \ldots$. Thus we have

$$\frac{1}{n+1} t_{n+1} = s_{n+1} - \left( \frac{n

Proof. We first prove that the series of functions $\sum_{k=1}^{\infty} \frac{f_k}{k}$ converges in the space $\mathfrak{L}_2(T, \mathcal{M}, \mu)$. If $m < n$, then we have

$$\left\| \sum_{k=1}^{n} \frac{f_k}{k} - \sum_{k=1}^{m} \frac{f_k}{k} \right\|_2^2 = \int_T \left| \sum_{k=m+1}^{n} \frac{f_k}{k} \right|^2 d\mu = \sum_{j,k=m+1}^{n} \frac{1}{jk} \int_T f_j \bar{f}_k d\mu$$

$$= \sum_{j \neq k} \frac{1}{jk} \int_T g_j d\mu_j \int_T \bar{g}_k d\mu_k + \sum_{k=m+1}^{n} \frac{1}{k^2} \int_T |g_k|^2 d\mu_k.$$

We have used (22.24.i) to write the last equality. The first term of the last expression above is zero by hypothesis, and the second term goes to zero as $m$ and $n$ go to $\infty$, by (i). Thus we have

$$\lim_{m,n \to \infty} \left\| \sum_{k=1}^{n} \frac{f_k}{k} - \sum_{k=1}^{m} \frac{f_k}{k} \right\|_2 = 0,$$

so that the partial sums of $\sum_{k=1}^{\infty} \frac{f_k}{k}$ form a Cauchy sequence in $\mathfrak{L}_2(T, \mathcal{M}, \mu)$.

Let $h$ be the $\mathfrak{L}_2$ limit of $\sum_{k=1}^{n} \frac{f_k}{k}$; then $h$ is also in $\mathfrak{L}_1$. Theorem (13.17) shows that $h$ is also the $\mathfrak{L}_1$ sum $\sum_{k=

independent of the first $n$ coordinates. [Note that $\sum_{k=n+1}^{\infty} \frac{1}{k} f_k$ converges in the $\mathfrak{L}_1$ metric to a function in $\mathfrak{L}_1$.] The integral

$$\int_{T_{\Omega_n}} \left( \sum_{k=n+1}^{\infty} \frac{1}{k} f_k \right) d\mu_{\Omega_n}$$

is plainly equal to the function $\sum_{k=n+1}^{\infty} \frac{1}{k} f_k$; thus (1) and (2) show that $\lim_{n \to \infty} \sum_{k=n+1}^{\infty} \frac{1}{k} f_k(t) = 0$ for almost all $t \in T$. That is, the series $\sum_{k=1}^{\infty} \frac{1}{k} f_k(t)$ converges a.e. in $T$. By (22.28), we have

$$\lim_{n \to \infty} \frac{1}{n} \left( f_1(t) + \cdots + f_n(t) \right) = 0$$

a.e. in $T$. □

(22.30) Example. Let $T_n$, $\mu_n$ and $f_n$ be just as in (22.9). We have $\|f_k\|_2^2 = \frac{1}{4}$, so that the hypotheses of (22.29) are satisfied. Hence we have

$$\lim_{n \to \infty} \frac{f_1 + \cdots + f_n}{n} = \lim_{n \to \infty} \frac{\left( t_1 - \frac{1}{2} \right) + \left( t_2 - \frac{1}{2} \right) + \cdots + \left( t_n - \frac{1}{2} \right)}{n} = 0$$

a.e.; i.e.,

$$\lim_{n \to \infty} \left( \frac{t_1 + t_2 + \cdots + t_n}{n} - \frac{1}{2} \right)

We will show first that for almost all $t \in T$, there is a positive integer $m_0$ [depending on $t$] such that

$$f_m(t) = f'_m(t) \quad \text{if} \quad m \geq m_0. \tag{1}$$

Under the hypothesis (i), it is trivial to show that the numbers $\mu_k(\{t_k \in T_k : |g_k(t_k)| > \alpha\})$ are independent of $k$ for every $\alpha \in R$. Using this fact, we have

$$\sum_{k=1}^{\infty} \mu(\{t \in T : |f_k(t)| + f'_k(t)\}) = \sum_{k=1}^{\infty} \mu(\{t \in T : |f_k(t)| > k\})$$

$$= \sum_{k=1}^{\infty} \mu_k(\{t_k \in T_k : |g_k(t_k)| > k\})$$

$$= \sum_{k=1}^{\infty} \left[ \sum_{n=k}^{\infty} \mu_1(\{t_1 \in T_1 : n < |g_1(t_1)| \leq n + 1\}) \right]$$

$$= \sum_{k=1}^{\infty} k \mu_1(\{t_1 \in T_1 : k < |g_1(t_1)| \leq k + 1\})$$

$$\leq \int_{T_1} |g_1| d\mu_1 < \infty. \tag{2}$$

Next write $E^{(k)} = \{t_k \in T_k : |g_k(t_k)| > k\}$ and $E_k = E^{(k)} \times T_{\{k\}}$. By (2), the series $\sum_{k=1}^{\infty} \mu_k(E^{(k)})$ converges, and so the BOREL-CANTELLI lemma (22.26) implies that $\mu \left( \bigcup_{n=1}^{\infty} \left( \bigcap_{k=n}^{\infty} E'_k \right) \right) = 1$. Thus almost all $t \in T$ have the property that

From (i), from the primeval definition (12.2) of the integral, and from (12.21), it is clear that

$$\sum_{k=1}^{\infty} k^{-2} \int_{T} f'_{k}^{2} d\mu = \int_{T_{1}} \left( \sum_{k=1}^{\infty} k^{-2} h_{k}^{2} \right) d\mu_{1}.$$ (6)

We will show that the function $w = \sum_{k=1}^{\infty} k^{-2} h_{k}^{2}$ is in $\mathfrak{L}_{1}(T_{1})$. Consider any point $t_{1} \in T_{1}$ such that $|g_{1}(t_{1})| > 0$. There is a [unique] positive integer $p$ such that $p - 1 < |g_{1}(t_{1})| \leq p$. We have $h_{1}(t_{1}) = h_{2}(t_{1}) = \cdots = h_{p-1}(t_{1}) = 0$ and $h_{p}(t_{1}) = h_{p+1}(t_{1}) = \cdots = g_{1}(t_{1})$, so that

$$\sum_{k=1}^{\infty} k^{-2} h_{k}^{2}(t_{1}) = \sum_{k=p}^{\infty} k^{-2} g_{1}^{2}(t_{1}) \leq |g_{1}(t_{1})| \sum_{k=p}^{\infty} k^{-2} p.$$ (7)

For every positive integer $p$, the relations

$$\sum_{k=p+1}^{\infty} k^{-2} < \int_{0}^{\infty} \frac{dx}{(x+p)^{2}} = \frac{1}{p}$$

are obvious, and so we have

$$\sum_{k=p}^{\infty} k^{-2} p < \frac{1}{p} + 1 \leq 2.$$ (8)

Combining (7) and (8), we see that

$$w \leq 2 |g_{1}|.$$

Since $g_{1} \in \mathfrak{L}_{1

(22.32) Exercise. (a) Prove the following analogue of (22.29). Notation is as in (22.29). Replace the hypothesis (22.29.i) by

(i) $\sum_{k=1}^{\infty} \alpha_k \|g_k\|_2^2 < \infty$,

where $\alpha_k > 0$ and $\sum_{k=1}^{\infty} \alpha_k < \infty$. Then the infinite series

(ii) $\sum_{k=1}^{\infty} \alpha_k f_k(t)$

converges for almost all $t \in T$.

(b) Prove the following analogue of (22.29), which is known as the weak law of large numbers. Again notation is as in (22.29). Replace (22.29.i) by the hypothesis

(iii) $\lim_{n \to \infty} \left[ \frac{1}{n^2} \sum_{k=1}^{n} \|f_k\|_2^2 \right] = 0$.

Then for every $\varepsilon > 0$, the equality

$$\lim_{n \to \infty} \mu \left( \left\{ t \in T : \left| \frac{1}{n} \sum_{k=1}^{n} f_k(t) \right| > \varepsilon \right\} \right) = 0$$

holds. That is, the sequence of functions $\left( \frac{1}{n} \sum_{k=1}^{n} f_k \right)_{n=1}^{\infty}$ converges to zero in measure.

(22.33) Exercise. Let $T_n = \{0, 1, 2, \ldots, r-1\}$ and let $\mu_n(A) = \frac{1}{r} \bar{A}$ ($n=1, 2, \ldots$). For a fixed $l \in \{0, 1, \ldots, r-1\}$, define

$$g_n(t) = \begin{cases} 1 \text{ if } t_n = l, \\ 0 \text{ if } t_n \neq l \end{cases}$$

for all

let $\Gamma = \{1, 2, 3, \ldots\}$, let $\Omega_n = \{1, 2, \ldots, n\}$, and let $\mathcal{M}^{(n)}$ be the $\sigma$-algebra of all sets $A_{\Omega_n} \times T_{\Omega_n}'$ for $A_{\Omega_n} \in \mathcal{M}_{\Omega_n}$. Now consider measures $\mu_n$ and $\eta_n$ on $(T_n, \mathcal{M}_n)$ such that $\mu_n(T_n) = \eta_n(T_n) = 1$, and let $\mu$ und $\eta$ be the product measures formed from the measures $\mu_n$ and $\eta_n$, respectively. Our first result deals with the case that $\eta_n \ll \mu_n$ for all $n$, and establishes a remarkable fact about $\eta$ and $\mu$.
