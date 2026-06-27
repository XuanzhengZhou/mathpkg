---
role: proof
locale: en
of_concept: proposition-1-62
source_book: gtm040
source_chapter: "1"
source_section: "62"
---

**Proof:** Since the

This equality for every such sequence $\{t_k\}$ implies that

$$\lim_{t \to 1} \sum c_n t^n = L.$$

d. Convergent subsequences of matrices. A bounded sequence of real numbers has a subsequence which converges to a finite limit. We shall obtain a generalization of this result to matrices.

Proposition 1-63: Let $\{A^{(n)}\}$ be a sequence of matrices with the property that for some pair of real numbers $c$ and $d$, $cE \leq A^{(n)} \leq dE$ for all $n$. Then there exists a subsequence of matrices $\{A^{(n_v)}\}$ which converges in every entry.

Proof: Since there are only denumerably many entries in each matrix, they can be numbered by a subset of the positive integers. Select a subsequence $\{A_1^{(n)}\}$ which converges in the first entry. Let $A_2^{(2)}, A_2^{(3)}, A_2^{(4)}, \ldots$ be a subsequence of $A_1^{(2)}, A_1^{(3)}, \ldots$ which converges in the second entry. In general, let $A_m^{(m)}, A_m^{(m+1)}, \ldots$ be a subsequence of $A_{m-1}^{(m)}, A_{m-1}^{(m+1)}, \ldots$ which converges in the $m$th entry. Finally set

$$A^{(n_v)} = A_v^{(v)}$$

Then $\{A^{(n_v)}\}$ converges in every entry.

Corollary 1-64: Let $\{A^{(n)}\}$ be a sequence of matrices with the property that $cE \leq A^{(n)} \leq dE$ for all $n$. Then $\lim_n A^{(n)} = A$ exists if and only if $\lim_v A^{(n_v)} = A$ for every convergent subsequence $\{A^{(n_v)}\}$.

Proof: The necessity of the condition is trivial. For the sufficiency suppose $\lim A_{ij}^{(n)}$ does not exist. Then $\lim \inf A_{ij}^{(n)} < \lim \

PROOF: Let $n_1 = k_1 d$ be an element of $T$. If $k_1 = 1$, $\{n_1\}$ is the required set. If not, choose $n_2$ such that $n_1 \nmid n_2$. Then $(n_1, n_2) = k_2 d$ with $k_2 < k_1$. If $k_2 = 1$, $\{n_1, n_2\}$ is the required set. Otherwise, find $n_3$ such that $k_2 d \nmid n_3$, and set $(n_1, n_2, n_3) = k_3 d$ with $k_3 < k_2$. Continuing in this way, we obtain a decreasing sequence of integers $k_1, k_2, \ldots$ bounded below by 1. It must terminate, and then we have constructed the finite set.

Lemma 1-66: Let $T$ be a non-empty set of positive integers which is closed under addition and which has the greatest common divisor $d$. Then all sufficiently large multiples of $d$ are in the set $T$.

PROOF: If $d \neq 1$, divide all the elements in $T$ by $d$ and reduce the problem to the case $d = 1$. By Lemma 1-65 there is a finite subset $\{n_1, \ldots, n_s\}$ of $T$ with greatest common divisor 1. Then there exist integers $c_1, \ldots, c_s$ with the property

$$c_1 n_1 + \cdots + c_s n_s = 1.$$

If we collect the positive terms and the negative terms and note that $T$ is closed under addition, we find that $T$ contains non-negative integers $m$ and $n$ with $m - n = 1$. Suppose $q \geq n(n - 1)$. Then $q = an + b$ with $a \geq n - 1$ and $0 \leq b \leq n - 1$. Thus

$$q = (a - b)n + bm$$

and $q$ is in $T

Theorem 1-68: Let $\{y_n\}$ be a sequence of identically distributed independent random variables with common mean $\mu$ and with common finite variance $\sigma^2 > 0$. Set $s_m = y_1 + \cdots + y_m$. Then for all real $\alpha$ and $\beta$ with $\alpha < \beta$,

$$\lim_{n \to \infty} \Pr\left[\alpha < \frac{s_m - m\mu}{\sigma\sqrt{m}} < \beta\right] = \Phi(\beta) - \Phi(\alpha),$$

where

$$\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-u^2/2} du.$$
