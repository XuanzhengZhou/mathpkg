---
role: proof
locale: en
of_concept: type-pq-properties
source_book: gtm038
source_chapter: "VII"
source_section: "1"
---

(1) For $\bar{\varphi}$, we have
$$\bar{\varphi}(c\xi_1, \ldots, c\xi_r) = \overline{\varphi(c\xi_1, \ldots, c\xi_r)} = \overline{c^p \bar{c}^q \varphi(\xi_1, \ldots, \xi_r)} = \bar{c}^p c^q \bar{\varphi}(\xi_1, \ldots, \xi_r).$$
Hence $\bar{\varphi}$ is of type $(q, p)$.

(2) For addition:
$$(\varphi + \psi)(c\xi_1, \ldots, c\xi_r) = \varphi(c\xi_1, \ldots, c\xi_r) + \psi(c\xi_1, \ldots, c\xi_r) = c^p \bar{c}^q \varphi(\xi_1, \ldots, \xi_r) + c^p \bar{c}^q \psi(\xi_1, \ldots, \xi_r)$$
$$= c^p \bar{c}^q (\varphi + \psi)(\xi_1, \ldots, \xi_r).$$
For scalar multiplication:
$$(c \cdot \varphi)(\xi_1, \ldots, \xi_r) = c \cdot \varphi(\xi_1, \ldots, \xi_r)$$
and scaling the arguments gives:
$$\varphi(c\xi_1, \ldots, c\xi_r) = c^p \bar{c}^q \varphi(\xi_1, \ldots, \xi_r).$$
Thus $\varphi + \psi$ and $c \cdot \varphi$ are of type $(p, q)$.

(3) For the wedge product, using the definition:
$$(\varphi \wedge \psi)(c\xi_1, \ldots, c\xi_{r+s}) = \frac{1}{r!s!} \sum_{\sigma \in \mathfrak{S}_{r+s}} (\operatorname{sgn} \sigma) \, \varphi(c\xi_{\sigma(1)}, \ldots, c\xi_{\sigma(r)}) \cdot \psi(c\xi_{\sigma(r+1)}, \ldots, c\xi_{\sigma(r+s)})$$
$$= c^p \bar{c}^q c^{p'} \bar{c}^{q'} \cdot \frac{1}{r!s!} \sum_{\sigma} (\operatorname{sgn} \sigma) \, \varphi(\xi_{\sigma(1)}, \ldots) \, \psi(\xi_{\sigma(r+1)}, \ldots)$$
$$= c^{p+p'} \bar{c}^{q+q'} (\varphi \wedge \psi)(\xi_1, \ldots, \xi_{r+s}).$$
Hence $\varphi \wedge \psi$ is of type $(p + p', q + q')$.
