---
role: proof
locale: en
of_concept: normal-mapping-spectral-theorem
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

We proceed by induction on $\dim W$. If $\dim W = 1$, any nonzero vector spans a cartesian basis and is trivially an eigenvector.

Assume the result holds for all dimensions $< n$ and let $\dim W = n$. Since $f$ is a linear operator on a finite dimensional complex vector space, $f$ has at least one eigenvalue $x \in \mathbb{C}$ with corresponding eigenvector $w \neq 0$. Thus $w f = x w$, i.e., $[w]f \subseteq [w]$.

By Exercise 4(ii), $w f^* = \bar{x} w$, so $[w]f^* \subseteq [w]$.

By Exercise 4(iii), the hypothesis $[w]f \subseteq [w]$ implies $[w]^\perp f \subseteq [w]^\perp$. Similarly, $[w]^\perp f^* \subseteq [w]^\perp$.

Let $f_1 = f|_{[w]^\perp}$ be the restriction of $f$ to $[w]^\perp$. Then $f_1$ is a normal mapping on the Hilbert space $([w]^\perp, \sigma|_{[w]^\perp})$ of dimension $n-1$ (or less). By the induction hypothesis, $[w]^\perp$ has a cartesian basis consisting of eigenvectors of $f_1$, hence of $f$.

Adjoining the normalized eigenvector $w/\|w\|$ to this basis yields a cartesian basis of $W$ consisting entirely of eigenvectors of $f$. (This is the deduction required in Exercise 4 of the source text.)
