---
role: proof
locale: en
of_concept: maximum-modulus-theorem-third-version
source_book: gtm011
source_chapter: "VI"
source_section: "1.4"
---

Suppose $|f(z)| \leq M$ does not hold for all $z \in G$. Then there exists $z_0 \in G$ with $|f(z_0)| > M$. Let $\varepsilon = |f(z_0)| - M > 0$. Define $h(z) = |f(z)|$; then $h$ is continuous on $G$. The set $K = \{z \in G : h(z) \geq M + \varepsilon/2\}$ is closed in $G$ and contains $z_0$. Since $G$ is a region, we may consider a component argument.

Alternatively, the result follows from the Second Version by a standard exhaustion argument: for each $n$, let $G_n = G \cap B(0; n)$. The limsup condition on $\partial_{\infty} G$ implies that for sufficiently large $n$, $|f(z)| \leq M + \varepsilon$ on $\partial G_n$. By the Second Version, $|f(z)| \leq M + \varepsilon$ on $G_n$ for all large $n$, hence on all of $G$. Since $\varepsilon > 0$ is arbitrary, $|f(z)| \leq M$ on $G$.

For the second part, if $|f(a)| = M$ for some $a \in G$, then $f$ attains its maximum modulus at an interior point, and by the First Version (1.1), $f$ is constant.
