---
role: proof
locale: en
of_concept: infinitely-many-prime-ideals-degree-1
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof of Theorem 126: Infinitely Many Prime Ideals of Degree 1

Let $\mathfrak{p}_f$ run through the distinct prime ideals of degree $f$ for $f = 1, 2, \ldots, n$. (Of course $\mathfrak{p}_f$ need not exist for each $f$.) Since at most $n$ distinct prime ideals of $k$ divide a given rational prime $p$, then, in any case, for $s > 1$,

$$\log \zeta_k(s) = \sum_{\mathfrak{p}} \left(-\log\left(1 - \frac{1}{N(\mathfrak{p})^s}\right)\right) = \sum_{f=1}^{n} \sum_{\mathfrak{p}_f} \left(-\log\left(1 - \frac{1}{N(\mathfrak{p}_f)^s}\right)\right),$$

where again $f(s)$ remains bounded. However, since $N(\mathfrak{p}_1) \geq 2$, we have for $s \geq 1$

$$-\log\left(1 - \frac{1}{N(\mathfrak{p}_1)^s}\right) = \frac{1}{N(\mathfrak{p}_1)^s} + \varphi(\mathfrak{p}_1, s),$$

$$0 \leq \varphi(\mathfrak{p}_1, s) = \frac{1}{2} \frac{1}{N(\mathfrak{p}_1)^{2s}} + \frac{1}{3} \frac{1}{N(\mathfrak{p}_1)^{3s}} + \cdots$$

$$< \frac{1}{N(\mathfrak{p}_1)^{2s}} \left(1 + \frac{1}{2^s} + \frac{1}{4^s} + \cdots\right) < \frac{2}{N(\mathfrak{p}_1)^{2s}},$$

and hence the sum over $\mathfrak{p}_1$ is

$$0 \leq \sum_{\mathfrak{p}_1} \varphi(\mathfrak{p}_1, s) \leq 2 \sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^{2s}} \leq 2n \sum_{p} \frac{1}{p^{2s}} \leq 2n \sum_{p} \frac{1}{p^2},$$

that is, bounded for $s \geq 1$. Hence, in combination with the result that for prime ideals of degree $f \geq 2$ the contributions to $\log \zeta_k(s)$ remain bounded, it follows that

$$\log \zeta_k(s) - \sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^s}$$

remains bounded as $s$ tends to $1$, and with this, by (96) [the relation $\log \zeta_k(s) = \log \frac{1}{s-1} + g(s)$ with $g(s)$ bounded], we have proved

$$\sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^s} = \log \frac{1}{s-1} + g_1(s),$$

where $g_1(s)$ remains bounded as $s$ tends to $1$. Hence if $s$ approaches $1$ the sum over $\mathfrak{p}_1$ becomes arbitrarily large and thus it must consist of infinitely many terms. Therefore, there are infinitely many prime ideals of degree one in $k$.
