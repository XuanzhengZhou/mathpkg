---
role: proof
locale: en
of_concept: pion-neutral-decay-kinematics
source_book: gtm048
source_chapter: "3"
source_section: "3.8"
---

The "if" assertion is trivial: direct substitution shows that Definition 3.8.4a and 3.8.4b hold for the given expressions.

To show the converse, choose an instantaneous observer $(z, Z)$ with $Z \in \operatorname{span} \pi_*$. Let $e_\pi, e_\alpha, e_\beta$ and $p_\pi, p_\alpha, p_\beta$ be the respective energies and 3-momenta observed by $(z, Z)$. Note that $Z \in \operatorname{span} \pi_*$ implies $p_\pi = 0$ (the observer is at rest relative to the pion, i.e., the center-of-mass frame).

Algebra shows that Definition 3.8.4a and 3.8.4b hold iff:
$$e_\pi = m = e_\alpha + e_\beta, \quad e_\alpha = |p_\alpha| > 0, \quad e_\beta = |p_\beta| > 0, \quad p_\alpha = -p_\beta.$$

From $e_\pi = m$ (the pion's total energy in its rest frame is its rest mass), conservation of 4-momentum gives $\pi_* = \alpha_* + \beta_*$. Since $\alpha$ and $\beta$ are photons, their 4-momenta are lightlike: $g(\alpha_*, \alpha_*) = g(\beta_*, \beta_*) = 0$. Conservation of charge (Definition 3.8.4b) is trivial since the pion has charge $0$ and both photons have charge $0$.

From $p_\alpha = -p_\beta$ we have that $\alpha_*$ and $\beta_*$ have equal and opposite spatial parts in the center-of-mass frame. Writing $\alpha_* = \pi_*/2 + V$ and $\beta_* = \pi_*/2 - V$ for some spacelike vector $V \in M_z$, the condition $g(\alpha_*, \alpha_*) = 0$ yields
$$g(\pi_*/2 + V, \pi_*/2 + V) = -\frac{m^2}{4} + 2g(\pi_*/2, V) + g(V, V) = 0.$$

Since $g(\pi_*, V) = 0$ (otherwise $p_\alpha \neq -p_\beta$), we get $g(V, V) = m^2/4$. Setting $W = 2V/m$ gives $g(W, W) = 1$ and $g(\pi_*, W) = 0$, so $W$ is a spacelike unit vector orthogonal to $\pi_*$. The desired expressions for $\alpha_*$ and $\beta_*$ follow.
