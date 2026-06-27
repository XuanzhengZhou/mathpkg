---
role: proof
locale: en
of_concept: fubini-theorem
source_book: gtm018
source_chapter: "VII"
source_section: "36"
---

Since a real valued function is integrable if and only if its positive and negative parts are integrable, it is sufficient to consider only non negative functions $h$. In this case, Theorem B asserts that

$$\int h d(\mu \times \nu) = \iint h d\mu d\nu = \iint h d\nu d\mu.$$

Since, therefore, the non negative, measurable functions $f$ and $g$ (defined by $f(x) = \int h(x,y) d\nu(y)$ and $g(y) = \int h(x,y) d\mu(x)$) have finite integrals, it follows that they are integrable. Since, finally, this implies that $f$ and $g$ are finite valued almost everywhere, the sections of $h$ have the desired integrability properties, and the proof is complete.

The proof of the supporting Theorem B (for non negative measurable $h$) proceeds as follows: If $h$ is the characteristic function of a measurable set $E$, then

$$\int h(x,y) d\nu(y) = \nu(E_x) \text{ and } \int h(x,y) d\mu(x) = \mu(E^y),$$

and the desired result follows from the definition of product measure (35.B). In the general case we may find an increasing sequence $\{h_n\}$ of non negative simple functions converging to $h$ everywhere (20.B). Since a simple function is a finite linear combination of characteristic functions, the conclusion of the theorem is valid for every $h_n$ in place of $h$.

By 27.B (the monotone convergence theorem), $\lim_n \int h_n d\lambda = \int h d\lambda$. If $f_n(x) = \int h_n(x,y) d\nu(y)$, then it follows from the properties of the sequence $\{h_n\}$ that $\{f_n\}$ is an increasing sequence of non negative measurable functions converging for every $x$ to $f(x) = \int h(x,y) d\nu(y)$ (cf. 27.B). Hence $f$ is measurable (and obviously non negative); one more application of 27.B yields the conclusion that

$$\lim_n \int f_n d\mu = \int f d\mu.$$

This proves the equality of the double integral and one of the iterated integrals; the truth of the other equality follows similarly.
