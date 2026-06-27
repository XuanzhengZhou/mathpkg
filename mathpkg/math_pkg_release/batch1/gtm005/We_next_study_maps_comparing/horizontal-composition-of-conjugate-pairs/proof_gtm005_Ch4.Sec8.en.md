---
role: proof
locale: en
of_concept: horizontal-composition-of-conjugate-pairs
source_book: gtm005
source_chapter: "IV"
source_section: "8"
---

**Proof.** The proof may be visualized by the following diagram of hom-sets:
\[
\begin{array}{ccccc}
D(\bar{F}'F'x, d) & \cong & A(F'x, \bar{G}'d) & \cong & X(x, G'\bar{G}'d) \\
\downarrow & & \downarrow & & \downarrow \\
D(\bar{F}Fx, d) & \cong & A(Fx, \bar{G}d) & \cong & X(x, G\bar{G}d)
\end{array}
\]

The top row is the composite adjunction for $\langle \bar{F}', \bar{G}' \rangle \circ \langle F', G' \rangle$, and the bottom row is the composite adjunction for $\langle \bar{F}, \bar{G} \rangle \circ \langle F, G \rangle$. The vertical maps are induced by $\bar{\sigma}\sigma$ on the left and $\tau\bar{\tau}$ on the right. The commutativity of the left square follows from the conjugacy of $\langle \bar{\sigma}, \bar{\tau} \rangle$, and the commutativity of the right square follows from the conjugacy of $\langle \sigma, \tau \rangle$. Hence the entire diagram commutes, which is precisely the condition that $\langle \bar{\sigma}\sigma, \tau\bar{\tau} \rangle$ is a conjugate pair for the composite adjunctions.
