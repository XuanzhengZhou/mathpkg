---
role: proof
locale: en
of_concept: change-of-order-for-iterated-ends
source_book: gtm005
source_chapter: "IX"
source_section: "8. Iterated Ends and Limits"
---

**Proof.** The result follows from the Fubini theorem for iterated ends (Proposition of this section). By expanding the double end $\int_{\langle p, c \rangle} S(p, p, c, c)$ in two ways as iterated ends, one obtains:

$$\int_{\langle p, c \rangle} S(p, p, c, c) \cong \int_p \left[ \int_c S(p, p, c, c) \right]$$

and also, by symmetry (exchanging the roles of $P$ and $C$),

$$\int_{\langle p, c \rangle} S(p, p, c, c) \cong \int_c \left[ \int_p S(p, p, c, c) \right].$$

Since isomorphisms are invertible and compose, this yields the desired isomorphism

$$\int_p \left[ \int_c S(p, p, c, c) \right] \cong \int_c \left[ \int_p S(p, p, c, c) \right].$$

The existence conditions ensure that both inner ends required for the application of the Fubini proposition are satisfied in both orders.
