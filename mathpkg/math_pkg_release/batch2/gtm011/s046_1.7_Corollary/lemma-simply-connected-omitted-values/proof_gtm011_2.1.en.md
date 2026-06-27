---
role: proof
locale: en
of_concept: lemma-simply-connected-omitted-values
source_book: gtm011
source_chapter: "2"
source_section: "2.1"
---

Since $G$ is simply connected and $f$ never vanishes on $G$, there is an analytic branch of $\log f$ on $G$; denote it by $\ell$, so that $e^{\ell} = f$. Define

$$F = \frac{1}{2\pi i} \ell.$$

Since $f$ also omits the value $1$, the function $F$ cannot assume any integer value (for if $F(z) = n \in \mathbb{Z}$, then $\ell(z) = 2\pi i n$, giving $f(z) = 1$). Thus $\sqrt{F}$ and $\sqrt{F-1}$ are well-defined analytic functions on $G$. Define

$$H = \sqrt{F} - \sqrt{F-1}.$$

Then $H$ never vanishes on $G$, for if $H(z) = 0$ then $\sqrt{F(z)} = \sqrt{F(z)-1}$, which is impossible. Since $G$ is simply connected, $\log H$ is defined; choose a branch and denote it by $g$, so that $e^g = H$.

A direct computation yields

$$\frac{1}{H} = \frac{1}{\sqrt{F} - \sqrt{F-1}} = \sqrt{F} + \sqrt{F-1},$$

so that $H + \frac{1}{H} = 2\sqrt{F}$, and therefore $\frac{1}{2}(H + \frac{1}{H})^2 = 2F$.

Now $H + \frac{1}{H} = e^g + e^{-g} = 2\cosh g$, hence $(2\cosh g)^2 = 4\cosh^2 g = 4F$, giving $F = \cosh^2 g$. Consequently,

$$2\pi i F = 2\pi i \cosh^2 g = \pi i(1 + \cosh(2g)).$$

Taking exponentials,

$$f = e^{\ell} = e^{2\pi i F} = \exp[\pi i + \pi i \cosh(2g)] = -\exp[\pi i \cosh(2g)],$$

as required.
