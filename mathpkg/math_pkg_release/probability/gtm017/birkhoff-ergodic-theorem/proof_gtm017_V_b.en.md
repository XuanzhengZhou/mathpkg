---
role: proof
locale: en
of_concept: birkhoff-ergodic-theorem
source_book: gtm017
source_chapter: "V"
source_section: "b"
---
The proof uses the maximal ergodic lemma: for any constant $\beta$ and invariant set $M$,
$$\int_{M \cap \{\sup S_n/n > \beta\}} (f(w) - \beta) dP \geq 0.$$

With this, one shows $\limsup S_n/n$ and $\liminf S_n/n$ are invariant functions. Using the maximal lemma again proves they are equal almost everywhere, so the limit $y(w) = \lim S_n/n$ exists.

Uniform integrability of $\{S_n/n\}$ implies $L^1$ convergence to $y(w)$. Since $y$ is invariant, $y = E(y|\mathcal{G})$. But also $\int_M y dP = \int_M f dP$ for invariant $M$, so $y = E(f|\mathcal{G})$.
