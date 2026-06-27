---
role: proof
locale: en
of_concept: symplectic-form-integral-invariant
source_book: gtm060
source_chapter: "8"
source_section: "38"
---

This theorem is a direct reformulation of the theorem that a Hamiltonian phase flow preserves the symplectic structure ($(g^t)^* \omega^2 = \omega^2$). By definition, a differential form $\omega$ is an integral invariant of $g$ if and only if $g^*\omega = \omega$. Therefore, the equality $(g^t)^* \omega^2 = \omega^2$ is precisely the statement that $\omega^2$ is an integral invariant of $g^t$.

The proof that $(g^t)^* \omega^2 = \omega^2$ proceeds via the track construction: for any closed $2$-chain $c$, apply the boundary formula $\partial(Jc) = g^\tau c - c - J\partial c$, integrate $\omega^2$, use Stokes' theorem together with $d\omega^2 = 0$ to obtain $\int_{g^\tau c} \omega^2 = \int_c \omega^2$, which implies $(g^\tau)^* \omega^2 = \omega^2$.
