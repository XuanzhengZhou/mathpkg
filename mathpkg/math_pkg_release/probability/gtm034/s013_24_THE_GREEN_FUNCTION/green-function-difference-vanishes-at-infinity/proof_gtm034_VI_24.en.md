---
role: proof
locale: en
of_concept: green-function-difference-vanishes-at-infinity
source_book: gtm034
source_chapter: "VI"
source_section: "24"
---

Assume the contrary: there exists \(\epsilon > 0\) and a sequence \(x_n\) with \(|x_n| \to \infty\) such that \(|u(x_n + t) - u(x_n)| > \epsilon\) for some \(t\). By the diagonal process, extract a subsequence \(y_n\) such that \(u(y_n + y) \to v(y)\) for all \(y \in R\), with \(|v(t) - v(0)| \geq \epsilon\). Since \(u(x) = G(x,0)\) satisfies \(u(x) = \sum P(x,y)u(y) + \delta(x,0)\), taking limits yields \(v(x) = \sum P(x,y)v(y)\), so \(v\) is regular. By T1, \(v\) must be constant, contradicting \(v(t) \neq v(0)\).
