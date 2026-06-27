---
role: proof
locale: en
of_concept: orthogonality-of-characters
source_book: gtm007
source_chapter: "VI"
source_section: "1"
---

This follows from Proposition 4 applied to the dual group $\widehat{G}$.

Specifically, for $x \in G$, consider the evaluation $\varepsilon(x) \in \widehat{\widehat{G}}$ defined by $\varepsilon(x)(\chi) = \chi(x)$. If $x = 1$, then $\chi(1) = 1$ for all $\chi \in \widehat{G}$, so the sum is $|\widehat{G}| = n$.

If $x \neq 1$, then $\varepsilon(x)$ is a non-identity element of $\widehat{\widehat{G}}$. By applying the corollary (or Proposition 4) to the group $\widehat{G}$ at the element $\varepsilon(x)$, we obtain
$$\sum_{\chi \in \widehat{G}} \varepsilon(x)(\chi) = 0,$$
which is exactly $\sum_{\chi \in \widehat{G}} \chi(x) = 0$.
