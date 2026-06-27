---
role: proof
locale: en
of_concept: halting-problem-recursive-insolubility
source_book: gtm022
source_chapter: "5"
source_section: "5"
---

Let $M_n$ denote the $n$th Turing machine and put $f_n = \Psi_{M_n}^{(1,1)}$. The problem is to determine those $(n, r)$ for which $f_n(r)$ exists. We show that there is no Turing machine which computes for each $n$ whether or not $f_n(n)$ exists.

Suppose, for contradiction, that the function $f: \mathbb{N} \to \mathbb{N}$ defined by

$$f(n) = \begin{cases} 1 & \text{if } f_n(n) \text{ exists}, \\ 0 & \text{otherwise}, \end{cases}$$

is recursive. Then the function $g: \mathbb{N} \to \mathbb{N}$ defined by

$$g(n) = \begin{cases} f_n(n) + 1 & \text{if } f_n(n) \text{ exists}, \\ 0 & \text{otherwise}, \end{cases}$$

would also be recursive. Since $g$ is recursive, there exists a Turing machine $M_k$ such that $g = f_k = \Psi_{M_k}^{(1,1)}$. Now consider $g(k)$. If $f_k(k)$ exists, then $g(k) = f_k(k) + 1 \neq f_k(k)$, contradicting $g = f_k$. If $f_k(k)$ does not exist, then $g(k) = 0$, which means $f_k(k) = g(k) = 0$ exists, again a contradiction. Therefore $f$ cannot be recursive, and consequently the stopping problem is recursively insoluble.
