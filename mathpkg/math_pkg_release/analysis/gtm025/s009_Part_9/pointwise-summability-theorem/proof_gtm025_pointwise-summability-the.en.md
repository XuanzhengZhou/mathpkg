---
role: proof
locale: en
of_concept: pointwise-summability-theorem
source_book: gtm025
source_chapter: "21"
source_section: "§21"
---

Write $\varphi(t) = f(x+t) + f(x-t) - 2f(x)$. Then $|f * u_n(x) - f(x)| \leq (2\pi)^{-\frac{1}{2}} \int_0^\infty |\varphi(t)| n u(nt)dt$. Set $\Phi(h) = \int_0^h |\varphi(t)|dt$. Since $x$ is a Lebesgue point, $\frac{1}{h}\Phi(h) < \varepsilon/c$ for small $h$. Split the integral at $1/n$ and $\alpha$, bound each piece by $\varepsilon/3$ using integration by parts and monotonicity of $u$, yielding the result for large $n$. Continuity points are Lebesgue points, so the result holds there too.
