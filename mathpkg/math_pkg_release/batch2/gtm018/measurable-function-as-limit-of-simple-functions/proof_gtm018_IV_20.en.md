---
role: proof
locale: en
of_concept: measurable-function-as-limit-of-simple-functions
source_book: gtm018
source_chapter: "IV"
source_section: "20"
---
**Proof.** Suppose $f \geq 0$. For each $n = 1,2,\dots$ and $x \in X$, define
$$f_n(x) = \begin{cases} \frac{i-1}{2^n} & \text{if } \frac{i-1}{2^n} \leq f(x) < \frac{i}{2^n}, \quad i = 1,\dots,2^n n, \\ n & \text{if } f(x) \geq n. \end{cases}$$
Each $f_n$ is a non negative simple function, and $\{f_n\}$ is increasing. If $f(x) < \infty$, then for sufficiently large $n$, $0 \leq f(x) - f_n(x) < 1/2^n$. If $f(x) = \infty$, then $f_n(x) = n \to \infty$. Thus $f_n(x) \to f(x)$ for all $x$. For general $f$, write $f = f^+ - f^-$ and apply the result to each part separately.
