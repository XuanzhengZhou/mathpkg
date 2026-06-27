---
role: proof
locale: en
of_concept: kx-is-a-pid
source_book: gtm016
source_chapter: "0.1"
source_section: "0.1"
---

Let $I$ be a nonzero ideal of $K[X]$. Take $f(X)$ to be a nonzero element of $I$ of least degree, and let $g(X)$ be a nonzero element of $I$. We show that $g(X)$ is a multiple $f(X)h(X)$ of $f(X)$. Suppose not, and take $g(X)$ with minimal degree such that $g(X) \in I \setminus \{0\}$ and $g(X)$ is not a multiple of $f(X)$. Let $a_m$ and $b_n$ be the leading coefficients of $f(X)$ and $g(X)$ respectively. Choose $i$ such that $\operatorname{Deg}(f(X)X^i - (a_m/b_n)g(X)) < \operatorname{Deg} g(X)$. Since $f(X), g(X) \in I$, this difference is in $I$. By minimality of the degree of $g(X)$ among non-multiples of $f(X)$, this difference must be a multiple of $f(X)$. But then $g(X) = (b_n/a_m)(f(X)X^i - \text{multiple of }f(X))$ is a multiple of $f(X)$, contradiction. Hence every element of $I$ is a multiple of $f(X)$, so $I = (f(X))$ is principal.
