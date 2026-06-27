---
role: proof
locale: en
of_concept: hahn-banach-seminorm-extension
source_book: gtm015
source_chapter: "3"
source_section: "28"
---

# Proof of Hahn-Banach-Bohnenblust-Sobczyk theorem

Let $E$ be a vector space over $\mathbb{K}$, let $p$ be a seminorm on $E$, and let $M$ be a linear subspace of $E$. If $g$ is a linear form on $M$ such that $|g(y)| \le p(y)$ for all $y \in M$, then $g$ may be extended to a linear form $f$ on $E$ such that $|f(x)| \le p(x)$ for all $x \in E$.

Suppose first that $\mathbb{K} = \mathbb{R}$. By the Hahn-Banach theorem (28.6), $g$ may be extended to a linear form $f$ on $E$ such that $f(x) \le p(x)$ for all $x \in E$. Then also $-f(x) = f(-x) \le p(-x) = p(x)$, hence $|f(x)| \le p(x)$ for all $x$.

Now suppose $\mathbb{K} = \mathbb{C}$. Let $g_0(x) = \operatorname{Re} g(x)$; this is an $\mathbb{R}$-linear form on $M$ with $|g_0(y)| \le |g(y)| \le p(y)$. Viewing $E$ as a real vector space, extend $g_0$ to an $\mathbb{R}$-linear form $f_0$ on $E$ with $|f_0(x)| \le p(x)$ by the real case. Define $f: E \rightarrow \mathbb{C}$ by
$$f(x) = f_0(x) - i f_0(ix).$$
Then $f$ is $\mathbb{C}$-linear, extends $g$, and for any $x$, write $f(x) = |f(x)| e^{i\theta}$. Then
$$|f(x)| = e^{-i\theta} f(x) = f(e^{-i\theta} x) = f_0(e^{-i\theta} x) \le p(e^{-i\theta} x) = |e^{-i\theta}| p(x) = p(x).$$
