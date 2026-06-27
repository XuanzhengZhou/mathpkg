---
role: proof
locale: en
of_concept: completeness-limit-proposition
source_book: gtm004
source_chapter: "VIII"
source_section: "8"
---

# Proof of Completeness Characterized by Limits

**Proposition 8.3.** Let the filtered object $X$ be given by the notation (8.4), i.e.,

$$X^{p-1} \xrightarrow{\xi^p} X^p \xrightarrow{\nu^p} X \xrightarrow{\eta_p} X_p \xrightarrow{\xi_p} X_{p+1},$$

and set $X_q^p = X^p / X^q$ for $q \leq p$, with the obvious transition maps $\sigma_q^p: X_q^p \to X_{q+1}^p$ and $\varrho_q^p: X_q^p \to X_q^{p+1}$.

(i) If the filtration is right complete, then

$$\varprojlim_q\, (X_q^p, \sigma_q^p) = X^p.$$

(ii) If the filtration is left complete, then

$$\varinjlim_p\, (X_q^p, \varrho_q^p) = X_q.$$

**Proof.** (i) Apply Proposition 8.2 with $Y = X^p$ and $\mu = \nu^p: X^p \to X$. Here the factorization $X^q \to X^p \to X$ is simply the composition of inclusions $X^q \subseteq X^p \subseteq X$, so $\nu'^q: X^q \to X^p$ is the inclusion and $\mu = \nu^p$ is independent of $q$. Then $Y_q = X^p / X^q = X_q^p$, and the map $\xi'_q: Y_q \to Y_{q+1}$ is precisely $\sigma_q^p$. Since right completeness means $(X; \eta_p) = \varprojlim (X_p, \xi_p)$, Proposition 8.2 gives $(X^p; \eta'_q) = \varprojlim (X_q^p, \sigma_q^p)$, which is exactly the claim.

(ii) By duality, apply the dual of Proposition 8.2 to the cofiltration. Left completeness means $X = \varinjlim X^p$, and the dual argument yields $X_q = \varinjlim_p (X_q^p, \varrho_q^p)$. $\square$
