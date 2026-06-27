---
role: proof
locale: en
of_concept: intersection-of-primary-ideals-for-p-in-noetherian-ring
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

\textbf{Step 1:} By Krull's theorem (SS 7, Theorem 12, Corollary 2), we have $\bigcap_{n=1}^{\infty} (\mathfrak{p}^e)^n = (0)$ in $R_{\mathfrak{p}}$.

\textbf{Step 2:} The ideals $(\mathfrak{p}^e)^n$ are primary for $\mathfrak{p}^e$, and every ideal in $R_{\mathfrak{p}}$ which is primary for $\mathfrak{p}^e$ contains some power $(\mathfrak{p}^e)^n$ (this follows from the fact that in a noetherian local ring with maximal ideal $\mathfrak{p}^e$, any $\mathfrak{p}^e$-primary ideal contains a power of the maximal ideal).

\textbf{Step 3:} Since contraction maps the set of all primary ideals for $\mathfrak{p}^e$ onto the set of all primary ideals for $\mathfrak{p}$ (by Theorem 19) and preserves intersections (finite and infinite), the intersection of all ideals of $R$ which are primary for $\mathfrak{p}$ is $(0)^c$, that is, the kernel of the canonical homomorphism of $R$ into $R_{\mathfrak{p}}$.

\textbf{Step 4:} By Theorem 19(f) (which itself follows from Theorem 18), this kernel is precisely the ideal $\mathfrak{b}$, the intersection of those primary components of $(0)$ whose radicals are contained in $\mathfrak{p}$.

Thus $\mathfrak{a} = \mathfrak{b}$. Q.E.D.
