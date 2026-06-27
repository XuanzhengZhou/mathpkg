---
role: proof
locale: en
of_concept: dedekind-domain-group-characterization
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

The necessity is clear, since every fractionary ideal of a Dedekind domain is invertible by Theorem 11.

Conversely, if $\mathcal{I}$ is a group, every ideal in $R$ has a finite basis (Lemma 3), and $R$ is noetherian. Using the fact that $R$ is noetherian, we can now prove, by an indirect argument, that every proper integral ideal in $R$ is a product of prime ideals. Take a maximal counterexample $\mathfrak{a}$ (which exists since $R$ is noetherian). Then $\mathfrak{a}$ is not prime, so it is properly contained in some prime ideal $\mathfrak{p}$. Since $\mathfrak{p}$ is invertible (as all ideals are), we have $\mathfrak{a} = \mathfrak{p} \cdot (\mathfrak{a}:\mathfrak{p})$ with $\mathfrak{a} \subsetneq (\mathfrak{a}:\mathfrak{p})$. By maximality of $\mathfrak{a}$, the ideal $(\mathfrak{a}:\mathfrak{p})$ factors into prime ideals, and adding the factor $\mathfrak{p}$ gives a prime factorization of $\mathfrak{a}$, contradiction. Thus every proper ideal factors into prime ideals, and the maximality of proper prime ideals follows from the group property. Therefore $R$ is a Dedekind domain.
