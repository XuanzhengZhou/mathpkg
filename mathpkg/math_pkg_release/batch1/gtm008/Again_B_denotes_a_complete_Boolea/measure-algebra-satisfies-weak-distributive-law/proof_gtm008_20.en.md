---
role: proof
locale: en
of_concept: measure-algebra-satisfies-weak-distributive-law
source_book: gtm008
source_chapter: "20"
source_section: "20"
---

Let $m$ be a strictly positive $\sigma$-measure on the measure algebra $B$, and let $\{b_{nk} \mid n, k < \omega\} \subseteq B$ be given. For each $n < \omega$, define

$$s_n = \sum_{k < \omega} b_{nk}.$$

We must show

$$\prod_{n < \omega} s_n = \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{k \leq f(n)} b_{nk}.$$

The reverse inequality (RHS $\leq$ LHS) holds in any Boolean algebra, since $\sum_{k \leq f(n)} b_{nk} \leq s_n$ for each $n$ and $f$. It remains to prove LHS $\leq$ RHS.

Let $b = \prod_{n < \omega} s_n$. For each $n < \omega$, the sequence of partial sums

$$S_n^{\ell} = \sum_{k \leq \ell} b_{nk}$$

converges to $s_n$ in the order topology of $B$, and by $\sigma$-additivity of $m$,

$$\lim_{\ell \to \infty} m(s_n - S_n^{\ell}) = 0.$$

Fix $n < \omega$. For any $\varepsilon > 0$, choose $\ell_n \in \omega$ such that $m(s_n - S_n^{\ell_n}) < \varepsilon$. More precisely, for each $n$ choose $\ell_n$ so that

$$m\!\left(s_n - \sum_{k \leq \ell_n} b_{nk}\right) < \frac{1}{2^{n+1}}.$$

Define $f \in \omega^{\omega}$ by $f(n) = \ell_n$. Consider the element

$$c = \prod_{n < \omega} \sum_{k \leq f(n)} b_{nk}.$$

We claim that $b - c = 0$ (i.e., $b \leq c$). Indeed,

$$b - c = b \cdot (-c) = \left(\prod_{n < \omega} s_n\right) - \prod_{n < \omega} S_n^{f(n)}.$$

Since $b - c \leq \sum_{n < \omega} (s_n - S_n^{f(n)})$ (as one can check by Boolean algebra identities), and

$$m\!\left(\sum_{n < \omega} (s_n - S_n^{f(n)})\right) \leq \sum_{n < \omega} m(s_n - S_n^{f(n)}) < \sum_{n < \omega} \frac{1}{2^{n+1}} = 1,$$

we must have $b - c = 0$; otherwise, if $b - c \neq 0$, then by strict positivity $m(b - c) > 0$, but then $b - c \leq \sum_n (s_n - S_n^{f(n)})$ would imply $m(b-c) < 1$, which does not yield a contradiction by itself.

To be more precise: since $m$ is strictly positive, it suffices to show $m(b - c) = 0$. Because $b - c \leq \sum_n (s_n - S_n^{f(n)})$ and the measure of the right-hand side can be made arbitrarily small (by choosing $\ell_n$ with $m(s_n - S_n^{\ell_n}) < \varepsilon/2^{n+1}$), we get $m(b-c) < \varepsilon$ for every $\varepsilon > 0$. Hence $m(b-c) = 0$, so $b - c = 0$ by strict positivity. Therefore $b \leq c$, which means

$$b \leq \prod_{n < \omega} \sum_{k \leq f(n)} b_{nk} \leq \sum_{g \in \omega^{\omega}} \prod_{n < \omega} \sum_{k \leq g(n)} b_{nk}.$$

Since $b = \prod_n s_n$, this establishes the $(\omega, \omega)$-WDL.
