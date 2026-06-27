---
role: proof
locale: en
of_concept: fourier-expansion-of-discriminant
source_book: gtm041
source_chapter: "6"
source_section: "6.1"
---

The Fourier expansion of $\Delta(\tau)$ is stated in this section as a known fact:

$$\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n) e^{2\pi i n \tau}.$$

The derivation of this expansion follows from the periodicity of $\Delta(\tau)$. Since $\Delta(\tau + 1) = \Delta(\tau)$ (as a consequence of the modular transformation property with the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \in \Gamma$), $\Delta$ admits a Fourier series expansion in $q = e^{2\pi i \tau}$. The fact that the sum starts at $n = 1$ (no constant term) reflects that $\Delta$ is a cusp form, vanishing as $\tau \to i\infty$. The coefficients $\tau(n)$ are by definition Ramanujan's tau function. The factor $(2\pi)^{12}$ is a normalization that makes the $\tau(n)$ integers. The detailed computation of this expansion is presented in later sections of the book.
