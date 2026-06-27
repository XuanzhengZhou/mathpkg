---
role: proof
locale: en
of_concept: discrete-closed-family-fsigma
source_book: gtm002
source_chapter: "16"
source_section: "The Banach Category Theorem"
---

For each $\alpha \in A$ and each positive integer $n$, let
$$F_{\alpha,n} = \{x \in F_\alpha : d(x, X - G_\alpha) \geq 1/n\}.$$
Then $F_{\alpha,n}$ is a closed set, and $F_\alpha = \bigcup_{n=1}^{\infty} F_{\alpha,n}$.

If $\alpha \neq \beta$, we have $\varrho(x, y) \geq 1/n$ for every $x \in F_{\alpha,n}$ and $y \in F_{\beta,n}$. Hence any convergent sequence contained in the set $F_n = \bigcup_{\alpha \in A} F_{\alpha,n}$ must, except for a finite number of terms, be contained in a single set $F_{\alpha,n}$. It follows that $F_n$ is closed, and that
$$E = \bigcup_{\alpha \in A} F_\alpha = \bigcup_{n=1}^{\infty} F_n$$
is an $F_\sigma$. $\square$
