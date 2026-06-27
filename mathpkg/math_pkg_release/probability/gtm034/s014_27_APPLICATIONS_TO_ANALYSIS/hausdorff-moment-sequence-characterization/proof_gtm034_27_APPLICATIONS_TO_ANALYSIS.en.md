---
role: proof
locale: en
of_concept: hausdorff-moment-sequence-characterization
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

Given a sequence $c(n)$, define $f$ on $R^+ = \{(m,n) : m \geq 0, n \geq 0\}$ by
$$f(m,0) = 2^m c(m), \quad f(m,n) = 2^{m+n} \Delta^n c(m).$$
For the simple unsymmetric 2D random walk with $P(0,x) = 1/2$ if $x = (0,1)$ or $x = (1,0)$, one verifies that $f$ satisfies $\sum_{y} P(x,y)f(y) = f(x)$ on $R^+$. This uses $\Delta^n c(m+1) + \Delta^{n+1} c(m) = \Delta^n c(m)$.

If $c(n) = \int_0^1 t^n d\mu(t)$, then $\Delta c(n) = \int_0^1 t^n(1-t)d\mu(t) \geq 0$, and by induction $\Delta^k c(n) \geq 0$. Conversely, if $\Delta^k c(n) \geq 0$ for all $k,n$, then $f \geq 0$ is a non-negative $P$-regular function on $R^+$.

The general theory (via the Martin boundary method developed in P3) shows that every non-negative regular function on $R^+$ admits the integral representation
$$f(m,n) = 2^{m+n} \int_0^1 t^m (1-t)^n d\mu(t).$$
Setting $n = 0$ gives $c(m) = \int_0^1 t^m d\mu(t)$, proving $c(n)$ is a moment sequence. The necessity of $\Delta^k c(n) \geq 0$ follows from the integral representation.
