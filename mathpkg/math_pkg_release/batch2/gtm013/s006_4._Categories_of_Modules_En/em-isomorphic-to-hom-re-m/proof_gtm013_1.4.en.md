---
role: proof
locale: en
of_concept: em-isomorphic-to-hom-re-m
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

First note that $eM$ is a left $eRe$-module via $(ere, ex) \mapsto erex$, and a right $S$-module by restriction. Dually, $Mf$ is a right $fSf$-module.

Define $\rho: eM \to \operatorname{Hom}_R(Re, M)$ by $\rho(em)(re) = rem$ for $em \in eM$, $re \in Re$. The map is well-defined: if $re = r'e$, then $(r-r')e = 0$, so $rem = r'em$. It is an $R$-homomorphism: $\rho(em)(r \cdot se) = \rho(em)(rse) = rsem = r(sem) = r\rho(em)(se)$.

Injectivity: if $\rho(em) = 0$, then $\rho(em)(e) = eem = em = 0$.

Surjectivity: given $f \in \operatorname{Hom}_R(Re, M)$, set $x = f(e) \in M$. Since $f(e) = f(e^2) = ef(e)$, we have $x = ex \in eM$. Then $\rho(x)(re) = r(ex) = rf(e) = f(re)$.

The bimodule structure is preserved: for the left $eRe$-action, $\rho((ere)(em))(se) = s(ere)(em) = sereem = serrem'$ (where $m' = em$), which matches the induced action on the Hom set. The right $S$-action is preserved similarly. The proof for $\lambda$ is symmetric.
