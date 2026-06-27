---
role: proof
locale: en
of_concept: product-of-induced-paths
source_book: gtm057
source_chapter: "II"
source_section: "4"
---
Since $a \cdot b$ is defined, $a(\|a\|) = b(0)$. Consequently,
$$fa(\|fa\|) = fa(\|a\|) = f(a(\|a\|)) = f(b(0)) = fb(0),$$
so $fa \cdot fb$ is defined. Furthermore,
$$f(a \cdot b)(t) = f((a \cdot b)(t)) = \begin{cases} f(a(t)), & 0 \leq t \leq \|a\|, \\ f(b(t - \|a\|)), & \|a\| \leq t \leq \|a\| + \|b\| \end{cases} = (fa \cdot fb)(t).$$
