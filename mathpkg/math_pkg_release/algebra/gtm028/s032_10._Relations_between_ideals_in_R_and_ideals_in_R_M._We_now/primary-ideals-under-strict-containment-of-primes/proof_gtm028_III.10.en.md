---
role: proof
locale: en
of_concept: primary-ideals-under-strict-containment-of-primes
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

By passage to the quotient ring $R/(\mathfrak{q} \cap \mathfrak{u})$, we may suppose that $\mathfrak{q} \cap \mathfrak{u} = (0)$ (see the Remark at the end of SS 5, p. 213, regarding reduction by a common intersection).

Then, by Theorem 20, the intersection of all primary ideals belonging to $\mathfrak{p}$ is $(0)$.

Since $\mathfrak{q} \not\subset \mathfrak{v}$ (otherwise $\mathfrak{q}$ would have radical contained in $\mathfrak{v}$, contradicting that $\mathfrak{q}$ is $\mathfrak{p}$-primary with $\mathfrak{v} < \mathfrak{p}$), we have $\mathfrak{q} \neq (0)$.

Now, if every $\mathfrak{p}$-primary ideal contained $\mathfrak{q}$, then $\mathfrak{q}$ would be contained in the intersection of all $\mathfrak{p}$-primary ideals, which is $(0)$, a contradiction. Hence there exists an ideal $\mathfrak{q}''$ primary for $\mathfrak{p}$ such that $\mathfrak{q}'' \not\supset \mathfrak{q}$.

Set $\mathfrak{q}' = \mathfrak{q} \cap \mathfrak{q}''$. Since the intersection of two $\mathfrak{p}$-primary ideals is again $\mathfrak{p}$-primary, $\mathfrak{q}'$ is primary for $\mathfrak{p}$. Moreover, $\mathfrak{q}' < \mathfrak{q}$ (strict containment, since $\mathfrak{q}'' \not\supset \mathfrak{q}$), and
$$\mathfrak{q}' \cap \mathfrak{u} = (\mathfrak{q} \cap \mathfrak{q}'') \cap \mathfrak{u} = (\mathfrak{q} \cap \mathfrak{u}) \cap \mathfrak{q}'' = (0) = \mathfrak{q} \cap \mathfrak{u},$$
since $\mathfrak{q} \cap \mathfrak{u} = (0)$ in the quotient ring.

This completes the proof of the lemma.
