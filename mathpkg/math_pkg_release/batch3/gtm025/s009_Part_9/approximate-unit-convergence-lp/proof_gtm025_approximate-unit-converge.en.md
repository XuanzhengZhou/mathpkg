---
role: proof
locale: en
of_concept: approximate-unit-convergence-lp
source_book: gtm025
source_chapter: "21"
source_section: "SS 21"
---

Let $f \in \mathfrak{L}_p(R)$ and $\varepsilon > 0$. Obtain a neighborhood $V$ of $0$ with $2\|f_{-y}-f\|_p < \varepsilon$ for $y \in V$ via (13.24). Choose $n_0$ with $4\|f\|_p \int_{V'} u_n(y)dy < \varepsilon$ for $n \geq n_0$. For $h \in \mathfrak{L}_{p'}(R)$ with $\|h\|_{p'}=1$, split the convolution integral over $V$ and $V'$ to obtain $|\int_R (f*u_n - f)h dx| < \varepsilon$, giving $\|f*u_n - f\|_p < \varepsilon$.
