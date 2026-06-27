---
role: proof
locale: en
of_concept: classification-irreps-d-infty
source_book: gtm042
source_chapter: "5"
source_section: "5.5"
---

The classification follows from the Peter-Weyl theorem for compact groups. The characters
$$
\{1 = \psi_{1}, \; \psi_{2}, \; \chi_{h} \mid h = 1, 2, \ldots\}
$$
form an orthonormal basis for the space of square-integrable class functions on $D_{\infty}$ with respect to the invariant measure $d\alpha/4\pi$ on each component.

One verifies the orthogonality relations using the explicit integration formula:
$$
\int_{D_{\infty}} f(t)\,dt = \frac{1}{4\pi} \int_{0}^{2\pi} f(r_{\alpha})\,d\alpha + \frac{1}{4\pi} \int_{0}^{2\pi} f(s r_{\alpha})\,d\alpha.
$$

For $\chi_{h}$ with itself:
$$
\langle \chi_{h}, \chi_{h} \rangle = \frac{1}{4\pi} \int_{0}^{2\pi} 4 \cos^{2}(h\alpha)\,d\alpha + \frac{1}{4\pi} \int_{0}^{2\pi} 0\,d\alpha = \frac{1}{\pi} \int_{0}^{2\pi} \cos^{2}(h\alpha)\,d\alpha = 1.
$$

For distinct $h \neq k$:
$$
\langle \chi_{h}, \chi_{k} \rangle = \frac{1}{4\pi} \int_{0}^{2\pi} 4 \cos(h\alpha) \cos(k\alpha)\,d\alpha = \frac{1}{\pi} \int_{0}^{2\pi} \cos(h\alpha) \cos(k\alpha)\,d\alpha = 0.
$$

The degree-1 characters $\psi_{1}, \psi_{2}$ are clearly orthogonal to each other and to all $\chi_{h}$ (since $\chi_{h}$ vanishes on reflections while $\psi_{1}, \psi_{2}$ are constant there, and the rotation integrals $\int \cos(h\alpha)\,d\alpha = 0$).

Since the characters form a complete orthonormal system and each corresponds to an irreducible representation, these exhaust all irreducible representations of $D_{\infty}$ up to isomorphism.
