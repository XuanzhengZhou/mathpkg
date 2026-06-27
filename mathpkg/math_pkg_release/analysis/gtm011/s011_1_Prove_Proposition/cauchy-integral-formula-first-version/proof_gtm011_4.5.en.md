---
role: proof
locale: en
of_concept: cauchy-integral-formula-first-version
source_book: gtm011
source_chapter: "4"
source_section: "5"
---

Define
$$
g(z) = \int_{\gamma} \frac{f(w)}{w - z} \, dw
$$
for $z$ in $H = \mathbb{C} - \{\gamma\}$. By Lemma 5.1, $g$ is analytic on $H$. Moreover, by an analogue of Leibniz's rule, $g$ is analytic on $G$; that is, $g$ is an entire function. But Theorem 4.4 implies that $H$ contains a neighborhood of $\infty$ in $\mathbb{C}_{\infty}$. Since $f$ is bounded on $\{\gamma\}$ and $\lim_{z \to \infty} (w - z)^{-1} = 0$ uniformly for $w$ in $\{\gamma\}$,
$$
\lim_{z \to \infty} g(z) = \lim_{z \to \infty} \int_{\gamma} \frac{f(w)}{w - z} \, dw = 0.
$$
In particular, there is an $R > 0$ such that $|g(z)| \leq 1$ for $|z| \geq R$. Since $g$ is bounded on $\overline{B}(0; R)$, it follows that $g$ is a bounded entire function. Hence $g$ is constant by Liouville's Theorem. But then the limit condition gives $g \equiv 0$. That is, if $a \in G - \{\gamma\}$ then
$$
0 = \int_{\gamma} \frac{f(z) - f(a)}{z - a} \, dz
= \int_{\gamma} \frac{f(z)}{z - a} \, dz - f(a) \int_{\gamma} \frac{dz}{z - a}.
$$
Since $\int_{\gamma} \frac{dz}{z - a} = 2\pi i \, n(\gamma; a)$, we obtain
$$
n(\gamma; a) f(a) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(z)}{z - a} \, dz.
$$
