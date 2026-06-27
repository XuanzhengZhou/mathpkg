---
role: proof
locale: en
of_concept: "let-and-be-measures-on-such-that-for"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.21"
---

If $f \in \mathfrak{L}_p(X, \mathcal{A}, \mu)$, then there is a sequence $(\sigma_n)_{n=1}^{\infty}$ of $\mathcal{A}$-measurable, nonnegative, simple functions increasing to $|f|^p$, and so

$$\lim_{n \to \infty} \int_X \sigma_n d\mu = \int_X |f|^p d\mu < \infty.$$

It is clear that $\int_X \sigma_n d\nu \le \int_X \sigma_n d\mu$, and it follows that

$$\int_X |f|^p d\nu = \lim_{n \to \infty} \int_X \sigma_n d\nu \le \int_X |f|^p d\mu.$$

The next lemma, which may at first glance appear rather strange, is actually the crucial step in

[Here $\|f\|_2$ denotes the norm in $\mathfrak{L}_2(X, \mathcal{A}, \mu + \nu)$.] Thus $L$ is a bounded linear functional on $\mathfrak{L}_2(X, \mathcal{A}, \mu + \nu)$, and so by (15.11), there is a function $h \in \mathfrak{L}_2(X, \mathcal{A}, \mu + \nu)$ such that

$$L(f) = \int_X f \bar{h} d(\mu + \nu).$$

(2)

Actually $h$ is real-valued and nonnegative $(\mu + \nu)$-a.e., as we now show. For any $f \in \mathfrak{L}_2(X, \mathcal{A}, \mu + \nu)$, we can write

$$L(f) = \int_X f \operatorname{Re} h d(\mu + \nu) - i \int_X f \operatorname{Im} h d(\mu + \nu).$$

Assume that $\operatorname{Im} h$ fails to vanish $(\mu + \nu)$-a.e.; say the set

$$A = \{x : \operatorname{Im} h(x) > 0\}$$

satisfies $(\mu + \nu)(A) > 0$. Then $L(\xi_A) = \int_A \operatorname{Re} h d(\mu + \nu) - i \int_A \operatorname{Im} h d(\mu + \nu)$ is not real. By (1), $L$ is obviously real-valued on real-valued functions. This is a contradiction. Similarly, if $h$ were negative on a set $B$ such that $(\mu + \nu)(B) > 0$, we would have $L(\xi_B) < 0$, which again contradicts the definition of $L$. Thus $h$ is real and nonnegative $(\mu + \nu)$-a.e.; and we may suppose it to be so everywhere. The definition (1) of $L$ and the representation (2) show that

$$\int_X f(1 - h) d\nu = \int_X f h d\mu$$

everywhere with respect to both $\mu$ and $v$. Thus (3) shows that

$$\int_X f(1-g) dv = \int_X fg d\mu$$

for every $f \in \mathfrak{L}_2(X, \mathcal{A}, \mu + v)$. $\square$
