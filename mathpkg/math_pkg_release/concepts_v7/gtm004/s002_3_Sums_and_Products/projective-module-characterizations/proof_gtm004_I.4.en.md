---
role: proof
locale: en
of_concept: projective-module-characterizations
source_book: gtm004
source_chapter: "I. Modules"
source_section: "4. Free and Projective Modules"
---

# Proof of Equivalent Characterizations of Projective Modules

**(1) $\Rightarrow$ (2).** By Theorem 2.1, the sequence

$$0 \to \operatorname{Hom}_\Lambda(P, A) \xrightarrow{\mu_*} \operatorname{Hom}_\Lambda(P, B) \xrightarrow{\varepsilon_*} \operatorname{Hom}_\Lambda(P, C) \to 0$$

is exact at $\operatorname{Hom}_\Lambda(P, A)$ and $\operatorname{Hom}_\Lambda(P, B)$. We only need to show exactness at $\operatorname{Hom}_\Lambda(P, C)$, i.e., that $\varepsilon_*$ is surjective. This is precisely the defining property of a projective module: for any $\gamma : P \to C$, there exists $\beta : P \to B$ such that $\varepsilon \beta = \gamma$, i.e., $\varepsilon_*(\beta) = \gamma$. Hence the sequence is exact.

**(2) $\Rightarrow$ (3).** Consider the short exact sequence $\ker \varepsilon \hookrightarrow B \xrightarrow{\varepsilon} P$ where $\varepsilon : B \to P$ is surjective. By (2), the induced sequence

$$0 \to \operatorname{Hom}_\Lambda(P, \ker \varepsilon) \to \operatorname{Hom}_\Lambda(P, B) \xrightarrow{\varepsilon_*} \operatorname{Hom}_\Lambda(P, P) \to 0$$

is exact at $\operatorname{Hom}_\Lambda(P, P)$. Therefore $\varepsilon_*$ is surjective, so there exists $\beta : P \to B$ such that $\varepsilon_*(\beta) = \varepsilon \beta = 1_P$, as required.

**(3) $\Rightarrow$ (4).** Let $P \cong B/A$, giving an exact sequence $A \hookrightarrow B \xrightarrow{\varepsilon} P$ with $\varepsilon$ surjective. By (3), there exists $\beta : P \to B$ with $\varepsilon \beta = 1_P$. By Lemma 4.6, $B \cong A \oplus P$, so $P$ is a direct summand in $B$.

**(4) $\Rightarrow$ (5).** By Proposition 4.3, $P$ is a quotient of some free module $P'$. By (4), $P$ is a direct summand in $P'$.

**(5) $\Rightarrow$ (1).** By (5), $P' \cong P \oplus Q$ where $P'$ is free. Free modules are projective (Proposition 4.4), so by Proposition 4.5, $P$ is projective.
