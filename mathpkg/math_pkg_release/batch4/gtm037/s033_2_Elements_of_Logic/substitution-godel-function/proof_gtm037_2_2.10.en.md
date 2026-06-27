---
role: proof
locale: en
of_concept: substitution-godel-function
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

The proof constructs $s$ via an auxiliary function $s'$ defined using iterated substitution. Using the fact that simultaneous substitution can be obtained by iterated ordinary substitution (as described after 10.74):

$$\varphi(\sigma_0, \dots, \sigma_{m-1}) = \text{Subf}_{\sigma_0}^{v(k+n+1)} \text{Subf}_{\sigma_0}^{v(k+n+2)} \cdots \text{Subf}_{\sigma_0}^{v(k+n+m)} \psi,$$

one defines $s'$ with the recursive function $f$ acting on the Godel numbers of the successive substitution steps:

$$s'(x, y_0, \ldots, y_{m-1}) = f\big(gv(h(x, y_0, \ldots, y_{m-1}) + \ell f'''(x, y_0, \ldots, y_{m-1}) + 1),$$
$$y_0, f(gv(h(x, y_0, \ldots, y_{m-1}) + \ell f'''(x, y_0, \ldots, y_{m-1}) + 2), y_1, \ldots,$$
$$f(gv(h(x, y_0, \ldots, y_{m-1}) + \ell f'''(x, y_0, \ldots, y_{m-1}) + m, y_{m-1}, f^{iv}(x, y_0, \ldots, y_{m-1})) \cdots)\big).$$

The desired function $s$ is obtained from $s'$ by a simple and obvious definition by cases (returning $0$ when the inputs do not encode the appropriate formulas and terms). Since all constituent functions $f$, $gv$, $h$, $\ell$, $f'''$, and $f^{iv}$ are recursive (or primitive recursive), $s$ is recursive. $\square$

[Note: The full technical detail of the construction relies on notation and recursive function definitions established earlier in the chapter.]
