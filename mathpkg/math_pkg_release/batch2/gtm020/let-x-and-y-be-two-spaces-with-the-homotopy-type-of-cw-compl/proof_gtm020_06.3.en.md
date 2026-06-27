---
locale: en
of_concept: let-x-and-y-be-two-spaces-with-the-homotopy-type-of-cw-compl
role: proof
source_book: gtm020
source_chapter: 6. Change of Structure Group
source_section: '3'
---

We use the description of cohomology as homotopy classes of maps as given in (4.4) to calculate

$$H^n(X \times Y, \Pi) = [X \times Y, K(\Pi, n)]$$

$$= [X, \text{Map}(Y, K(\Pi, n))]$$

$$= \prod_{0 \leq q \leq n} [X, K(H^{n-q}(Y, \Pi), q)]$$

$$= \bigoplus_{0 \leq q \leq n} H^q(X, H^{n-q}(Y, \Pi)).$$

The proves the theorem on the Künneth formula.

Observe that the Künneth formula is equivalent to the mapping space decomposition of (4.6), and from the Künneth formula we obtain another proof of the decomposition (4.6).
