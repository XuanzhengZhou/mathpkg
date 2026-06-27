---
role: proof
locale: en
of_concept: levi-monotone-convergence
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

We may suppose with no loss of generality that $\int_X f_1 d\mu < \infty$, and in view of (12.16) that no $f_k$ assumes the value $-\infty$. If any $\int_X f_k d\mu$ is equal to $\infty$, the result is trivial. Otherwise, for $k \in N$, we define\n\n$$g_k(x) = \begin{cases} f_{k+1}(x) - f_k(x) & \text{if } f_k(x) < \infty, \\ \infty & \text{otherwise.} \end{cases}$$\n\nThen $\lim_{n \to \infty} f_n = f_1 + \sum_{k=1}^{\infty} g_k$, and so by (12.21) and (12.19),\n\n$$\int_X (\lim f_n) d\mu = \int_X f_1 d\mu + \sum_{k=1}^{\infty} \int_X g_k d\mu = \lim_{n \to \infty} \int_X f_n d\mu.$$
