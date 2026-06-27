---
role: proof
locale: en
of_concept: turing-computable-closed-under-minimalization
source_book: gtm037
source_chapter: "3"
source_section: "9"
---

Let $f$ be an $m$-ary special function, $m > 1$, and suppose that $f$ is computed by a machine $M$. Let $g(x_0, \ldots, x_{m-2}) = \mu y [f(x_0, \ldots, x_{m-2}, y) = 0]$ for all $x_0, \ldots, x_{m-2} \in \omega$. Then the following machine computes $g$:

$$T_{\text{left}} \rightarrow T_1 \rightarrow T_{\text{left}} \right$$

(The proof proceeds by constructing a Turing machine that iteratively computes $f(x_0, \ldots, x_{m-2}, y)$ for $y = 0, 1, 2, \ldots$, checking after each computation whether the result is $0$, and halting with the first such $y$.)
