---
role: proof
locale: en
of_concept: adjoint-involution
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

For all $a, b \in V$, we compute:
$$\sigma(af^{**}, b) = \sigma(a, bf^*) \quad \text{(by definition of } f^{**})$$
$$= \overline{\sigma(bf^*, a)} \quad \text{(by conjugate symmetry of } \sigma)$$
$$= \overline{\sigma(b, af)} \quad \text{(by definition of } f^*)$$
$$= \sigma(af, b) \quad \text{(by conjugate symmetry of } \sigma).$$

Since $\sigma$ is non-degenerate and $\sigma(af^{**}, b) = \sigma(af, b)$ for all $a, b \in V$, we conclude that $f^{**} = f$.
