---
role: proof
locale: en
of_concept: perturbation-of-minimum
source_book: gtm060
source_chapter: "6"
source_section: "25"
---

We have
$$f'_\varepsilon(x) = Ax + C\varepsilon + O(x^2) + O(\varepsilon x).$$

For sufficiently small $\varepsilon$, apply the implicit function theorem to $f'_\varepsilon(x)$. Since $f'_\varepsilon(0) = C\varepsilon + O(\varepsilon^2)$ and $\frac{\partial}{\partial x} f'_\varepsilon(x) \big|_{x=0} = A + O(\varepsilon) \neq 0$, there exists a unique $x_\varepsilon$ near $0$ such that $f'_\varepsilon(x_\varepsilon) = 0$. Solving $Ax_\varepsilon + C\varepsilon = 0$ to leading order gives $x_\varepsilon = -C\varepsilon/A + O(\varepsilon^2)$. The second derivative is $f''_\varepsilon(x_\varepsilon) = A + O(\varepsilon)$, confirming the minimum is non-degenerate for small $\varepsilon$.
