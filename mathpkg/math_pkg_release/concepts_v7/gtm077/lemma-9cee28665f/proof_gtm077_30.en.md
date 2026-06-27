---
role: proof
locale: en
of_concept: lemma-9cee28665f
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of If $r > 0$, then to each system of real numbers $c_1, \ldots, c_r$, not all vanishing, there is asso

This second important conclusion in Dirichlet's train of thought rests on Minkowski's Theorem 95.

If $\varkappa_1, \ldots, \varkappa_n$ are $n$ positive quantities such that

$$\varkappa_1 \cdot \varkappa_2 \cdots \varkappa_n = |\sqrt{d}|,$$
$$\varkappa_{p+r_2} = \varkappa_p \quad \text{for } p = r_1 + 1, \ldots, r_1 + r_2,$$

then by Theorem 95 there is a nonzero integer $\alpha$ in $K$ (whose norm thus has at least absolute value 1) such that

$$|\alpha^{(i)}| \leq \varkappa_i \quad \text{for } i = 1, 2, \ldots, n, \quad 1 \leq |N(\alpha)| \leq \sqrt{d}.$$

From this it follows that

$$|\alpha^{(i)}| \geq \frac{1}{|\alpha^{(1)}| \cdots |\alpha^{(i-1)}| \cdot |\alpha^{(i+1)}| \cdots |\alpha^{(n)}|} \geq \frac{1}{\varkappa_1 \cdots \varkappa_{i-1} \varkappa_{i+1} \cdots \varkappa_n}.$$

By choosing the $\varkappa_i$ appropriately and considering the linear form $L(\alpha) = c_1 \log|\alpha^{(1)}| + \cdots + c_r \log|\alpha^{(r)}|$, one constructs infinitely many integers $\alpha_h$ with $|N(\alpha_h)| \leq \sqrt{d}$ and strictly increasing $L(\alpha_h)$. These infinitely many principal ideals $(\alpha_h)$ cannot all be distinct; hence there exist distinct $h, m$ such that $(\alpha_h) = (\alpha_m)$, so $\alpha_m = \varepsilon \alpha_h$ for some unit $\varepsilon$. Then

$$L(\varepsilon) = L(\alpha_m) - L(\alpha_h) \neq 0,$$

proving Lemma (b).
