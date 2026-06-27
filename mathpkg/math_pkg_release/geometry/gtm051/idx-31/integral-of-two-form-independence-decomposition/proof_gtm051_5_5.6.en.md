---
role: proof
locale: en
of_concept: integral-of-two-form-independence-decomposition
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

**Proof.** Consider the common refinement $\{P_\rho \cap P'_{\rho'}\}$, which is also a polygonal decomposition of $M$.

For the decomposition $\Pi$, we have
$$\sum_\rho \iint_{P_\rho} \Omega = \sum_\rho \sum_{\rho'} \iint_{P_\rho \cap P'_{\rho'}} \Omega,$$
since each $P_\rho$ can be subdivided into the pieces $P_\rho \cap P'_{\rho'}$ and the integral is additive over such subdivisions.

Similarly, for the decomposition $\Pi'$:
$$\sum_{\rho'} \iint_{P'_{\rho'}} \Omega = \sum_{\rho'} \sum_\rho \iint_{P_\rho \cap P'_{\rho'}} \Omega.$$

Both sums equal $\sum_{\rho,\rho'} \iint_{P_\rho \cap P'_{\rho'}} \Omega$, hence they are equal to each other. $\square$
