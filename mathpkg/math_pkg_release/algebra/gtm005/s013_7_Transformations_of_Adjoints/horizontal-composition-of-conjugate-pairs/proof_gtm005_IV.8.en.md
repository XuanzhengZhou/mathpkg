---
role: proof
locale: en
of_concept: horizontal-composition-of-conjugate-pairs
source_book: gtm005
source_chapter: "IV"
source_section: "8. Composition of Adjoints"
---

The proof may be visualized by the diagram of hom-sets:

$$
\begin{array}{ccc}
D(\bar{F}'F'x, d) & \cong & A(F'x, \bar{G}'d) & \cong & X(x, G'\bar{G}'d) \\
\downarrow & & \downarrow & & \downarrow \\
D(\bar{F}Fx, d) & \cong & A(Fx, \bar{G}d) & \cong & X(x, G\bar{G}d)
\end{array}
$$

The left vertical arrow is induced by $\bar{\sigma}\sigma : \bar{F}F \to \bar{F}'F'$, and the right vertical arrow is induced by $\tau\bar{\tau} : G'\bar{G}' \to G\bar{G}$. Each square of the diagram commutes because $\langle \bar{\sigma}, \bar{\tau} \rangle$ and $\langle \sigma, \tau \rangle$ are conjugate pairs, so the outer rectangle commutes, establishing that $\langle \bar{\sigma}\sigma, \tau\bar{\tau} \rangle$ is a conjugate pair for the composite adjunctions.

More explicitly: start with an arrow $\bar{F}'F'x \to d$ in $D$. Applying the adjunction $\langle \bar{F}', \bar{G}' \rangle$ maps it to $F'x \to \bar{G}'d$ in $A$. Precomposition with $\sigma_x : Fx \to F'x$ sends this to $Fx \to \bar{G}'d$. The conjugation condition for $\langle \bar{\sigma}, \bar{\tau} \rangle$ then translates this to an arrow $x \to G\bar{G}d$ in $X$. The same result is obtained by first applying $\bar{\sigma}$ then $\sigma$, which corresponds to horizontal composition $\bar{\sigma}\sigma$, together with the corresponding $\tau\bar{\tau}$ on the right adjoint side.
