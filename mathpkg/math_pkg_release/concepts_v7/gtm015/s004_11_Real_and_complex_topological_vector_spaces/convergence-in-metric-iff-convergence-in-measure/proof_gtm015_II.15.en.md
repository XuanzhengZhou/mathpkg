---
role: proof
locale: en
of_concept: convergence-in-metric-iff-convergence-in-measure
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "15. The space (S)"
---

# Proof of Convergence in Metric iff Convergence in Measure

**Lemma (15.4).** Suppose $u_n \in [\mathcal{M}]$ ($n = 1, 2, 3, \ldots$) and $u \in [\mathcal{M}]$; say $u_n = [f_n]$ and $u = [f]$. Then (i) $u_n \to u$ for $d$ iff $f_n \to f$ in measure; (ii) $u_n$ is Cauchy for $d$ iff $f_n$ is fundamental in measure.

*Proof.* (i) By the invariance of $d$, we can suppose $u = \theta$; thus the problem is to show that $d(u_n, \theta) \to 0$ iff $f_n \to 0$ in measure.

Suppose $d(u_n, \theta) \to 0$, that is,

$$\int \frac{|f_n|}{1 + |f_n|} d\mu \to 0.$$

Let $\eta > 0$ and write $E_n = \{x : |f_n(x)| \geq \eta\}$; it is to be shown that $\mu(E_n) \to 0$. If $|f_n(x)| \geq \eta$ then

$$\frac{|f_n(x)|}{1 + |f_n(x)|} \geq \frac{\eta}{1 + \eta},$$

so

$$\mu(E_n) \cdot \frac{\eta}{1 + \eta} \leq \int_{E_n} \frac{|f_n|}{1 + |f_n|} d\mu \leq \int \frac{|f_n|}{1 + |f_n|} d\mu \to 0,$$

hence $\mu(E_n) \to 0$, so $f_n \to 0$ in measure.

Conversely, suppose $f_n \to 0$ in measure. Let $\varepsilon > 0$. Define $g_n = \frac{|f_n|}{1 + |f_n|}$; note $0 \leq g_n \leq 1$. Write $E_n = \{x : |f_n(x)| \geq \varepsilon\}$. Then

$$\int g_n d\mu = \int_{E_n} g_n d\mu + \int_{\complement E_n} g_n d\mu.$$

Since $g_n \leq 1$, the first integral is bounded by $\mu(E_n) \to 0$. On $\complement E_n$, $|f_n(x)| < \varepsilon$, so $g_n(x) \leq |f_n(x)| < \varepsilon$, and the second integral is at most $\varepsilon \cdot \mu(X)$ (assuming the measure is finite). For sufficiently large $n$, $\mu(E_n) < \varepsilon$, giving

$$\int g_n d\mu \leq \varepsilon + \varepsilon \mu(X),$$

which can be made arbitrarily small. Thus $d(u_n, \theta) \to 0$.

(ii) The proof is similar to (i), replacing the limit with the Cauchy condition: $f_n - f_m \to 0$ in measure as $n, m \to \infty$. $\square$
