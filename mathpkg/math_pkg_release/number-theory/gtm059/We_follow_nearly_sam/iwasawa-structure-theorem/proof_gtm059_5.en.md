---
role: proof
locale: en
of_concept: iwasawa-structure-theorem
source_book: gtm059
source_chapter: "5"
source_section: "5. Iwasawa Theory and Ideal Class Groups"
---

The proof proceeds in several steps. First, using the structure theory of finitely generated modules over the Noetherian ring $\Lambda = \mathbb{Z}_p[[X]]$, one shows that any finitely generated $\Lambda$-module admits a pseudo-isomorphism to a direct sum of modules of the form $\Lambda^r$, $\Lambda/(p^{\mu})$, and $\Lambda/(f^m)$ where $f$ is an irreducible distinguished polynomial.

For the special cases:
(i) If $V = \Lambda/(p^{\mu})$, then $V_n \cong \mathbb{Z}/p^{\mu}\mathbb{Z}[\Gamma_n] \cong (\mathbb{Z}/p^{\mu}\mathbb{Z})^{p^n}$, so $s_n(V) = \mu p^n$.

(ii) If $V = \Lambda/(f)$ where $f$ is a distinguished polynomial of degree $d$, then $f$ and $\omega_n = (1+X)^{p^n} - 1$ are coprime for large $n$, and one obtains $|V_n| = p^{dn}$ up to a bounded factor, so $s_n(V) = dn + c$ for some constant $c$.

In the general case, by the pseudo-isomorphism decomposition, the $s_n$ function is additive, giving the formula $s_n(V) = \mu p^n + \lambda n + \nu$ for $n$ sufficiently large, where $\mu$ is the sum of the $\mu_i$ from the $p$-torsion factors, and $\lambda$ is the sum of the degrees of the distinguished polynomial factors.
