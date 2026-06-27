---
role: proof
locale: en
of_concept: "stopping-problem"
source_book: gtm022
source_chapter: "IX"
source_section: "5"
---
Proof. Put $f_n = \Psi_{M_n}^{(1,1)}$. Suppose the function $f: \mathbb{N} \to \mathbb{N}$ defined by $f(n) = 1$ if $f_n(n)$ exists, $f(n) = 0$ otherwise, is recursive. Then the function $g(n) = f_n(n) + 1$ if $f_n(n)$ exists, $g(n) = 0$ otherwise, is recursive. Since $g$ is recursive, $g = f_m$ for some $m$. Then consider $g(m) = f_m(m) + 1 = f_m(m)$ if $f_m(m)$ exists, a contradiction. Hence $f$ is not recursive, and the stopping problem is insoluble. $\square$
