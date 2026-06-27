---
locale: en
of_concept: kunneth-formula-for-cohomology
role: proof
source_book: gtm020
source_chapter: "4"
source_section: "4.7"
---

We use the description of cohomology as homotopy classes of maps as given in (4.4) to calculate

$$H^n(X \times Y, \Pi) = [X \times Y, K(\Pi, n)]$$

$$= [X, \text{Map}(Y, K(\Pi, n))]$$

$$= \prod_{0 \leq q \leq n} [X, K(H^{n-q}(Y, \Pi), q)]$$

$$= \bigoplus_{0 \leq q \leq n} H^q(X, H^{n-q}(Y, \Pi)).$$

This proves the theorem on the Kunneth formula.

Observe that the Kunneth formula is equivalent to the mapping space decomposition of (4.6), and from the Kunneth formula we obtain another proof of the decomposition (4.6).
