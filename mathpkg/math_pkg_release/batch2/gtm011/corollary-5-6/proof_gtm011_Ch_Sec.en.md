---
role: proof
locale: en
of_concept: corollary-5-6
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Since $\sum g_n(x)$ converges uniformly for $x$ in $X$ there is an integer $n_0$ such that $|g_n(x)| < \frac{1}{2}$ for all $x$ in $X$ and $n > n_0$. This implies that $\text{Re} [1 + g_n(x)] > 0$ and also, according to inequality (5.3), $|\log (1 + g_n(x))| \leq \frac{3}{2} |g_n(x)|$ for all $n > n_0$ and $x$ in $X$. Thus

$$h(x) = \sum_{n=n_0+1}^{\infty} \log (1 + g_n(x))$$

converges uniformly for $x$ in $X$. Since $h$ is continuous and $X$ is compact it follows that $h$ must be bounded; in particular, there is a constant $a$ such that $\text{Re} h(x) < a$ for all $x$ in $X$. Thus, Lemma 5.7 applies and gives that

$$\exp h(x) = \prod_{n=n_0+1}^{\infty} (1 + g_n(x))$$

converges uniformly for $x$ in $X$.

Finally,

$$f(x) = [1 + g_1(x)] \cdots [1 + g_{n_0}(x)] \exp h(x)$$

and $\exp h(x) \neq 0$ for any $x$ in $X$. So if $f(x) = 0$ it must be that $g_n(x) = -1$ for some $n$ with $1 \leq n \leq n_0$
