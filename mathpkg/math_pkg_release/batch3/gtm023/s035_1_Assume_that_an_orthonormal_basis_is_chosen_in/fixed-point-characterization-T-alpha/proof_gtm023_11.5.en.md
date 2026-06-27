---
role: proof
locale: en
of_concept: fixed-point-characterization-T-alpha
source_book: gtm023
source_chapter: "XI"
source_section: "§5. Application to Lorentz-transformations, 11.19"
---

Assume $T_{\alpha} \iota = \iota$. This means $\alpha \circ \tilde{\alpha} = \iota$, whence $\alpha = \tilde{\alpha}^{-1}$. From the definition $T_{\alpha} \sigma = \sigma$ for all $\sigma \in S$, i.e. $\alpha \circ \sigma \circ \tilde{\alpha} = \sigma$. Using $\tilde{\alpha} = \alpha^{-1}$, we obtain

$$\alpha \circ \sigma = \sigma \circ \alpha \quad \text{for every } \sigma \in S. \tag{11.82}$$

To show that $\alpha = \pm \iota$, select an arbitrary unit vector $e \in C$ and define a selfadjoint mapping $\sigma$ by

$$\sigma z = (z, e) e \quad z \in C.$$

Then

$$(\sigma \circ \alpha) e = (\alpha e, e) e \quad \text{and} \quad (\alpha \circ \sigma) e = \alpha e.$$

By (11.82), these are equal, so

$$\alpha e = (\alpha e, e) e.$$

Thus every vector $\alpha e$ is a scalar multiple of $e$. By linearity, $\alpha = \lambda \iota$ for some complex constant $\lambda$. Since $\det \alpha = 1$, we have $\lambda^2 = 1$, so $\lambda = \pm 1$. Therefore $\alpha = \pm \iota$.
