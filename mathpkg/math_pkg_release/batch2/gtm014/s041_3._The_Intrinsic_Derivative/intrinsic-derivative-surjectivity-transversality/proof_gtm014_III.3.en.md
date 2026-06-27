---
role: proof
locale: en
of_concept: intrinsic-derivative-surjectivity-transversality
source_book: gtm014
source_chapter: "III"
source_section: "3"
---

This follows immediately from Proposition 3.6. By Proposition 3.6, the intrinsic derivative $(D\rho)_x$ is the composite
$$
T_x X \xrightarrow{(d\rho)_x} T_\sigma \operatorname{Hom}(E, F) \longrightarrow N_\sigma \cong \operatorname{Hom}(K_\sigma, L_\sigma),
$$
where $N_\sigma$ is the normal space to $L^r(E, F)$ in $\operatorname{Hom}(E, F)$.

Now $(D\rho)_x$ is surjective if and only if the image of $T_x X$ under $(d\rho)_x$ projects onto the full normal space $N_\sigma$. By the definition of the normal space, $T_\sigma \operatorname{Hom}(E, F) = T_\sigma L^r(E, F) \oplus N_\sigma$ (canonically identified). Thus the surjectivity condition is equivalent to
$$
(d\rho)_x(T_x X) + T_\sigma L^r(E, F) = T_\sigma \operatorname{Hom}(E, F),
$$
which is precisely the condition that $\rho$, viewed as a map $X \to \operatorname{Hom}(E, F)$, is transverse to the submanifold $L^r(E, F)$ at $x$.
