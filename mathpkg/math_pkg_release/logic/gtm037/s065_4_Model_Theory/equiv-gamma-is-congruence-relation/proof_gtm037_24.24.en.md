---
role: proof
locale: en
of_concept: equiv-gamma-is-congruence-relation
source_book: gtm037
source_chapter: "24"
source_section: "24"
---

The relation $\equiv_\Gamma$ is a congruence relation on $\mathfrak{Fr}_\mathcal{L}$ because it respects all operations. Specifically:
(i) $\Gamma \vdash_{\text{eq}} \sigma = \sigma$ (reflexivity);
(ii) if $\Gamma \vdash_{\text{eq}} \sigma = \tau$, then $\Gamma \vdash_{\text{eq}} \tau = \sigma$ (symmetry);
(iii) if $\Gamma \vdash_{\text{eq}} \sigma = \tau$ and $\Gamma \vdash_{\text{eq}} \tau = \rho$, then $\Gamma \vdash_{\text{eq}} \sigma = \rho$ (transitivity);
(iv) if $O$ is an operation symbol of rank $m$, and $\sigma_i = \tau_i$ are all in the relation, then $O\sigma_0\cdots\sigma_{m-1} = O\tau_0\cdots\tau_{m-1}$ is also in the relation (compatibility with operations).

These follow from the definition of $\Gamma$-eqthm as the intersection of all sets of equations satisfying closure conditions (i)-(iv) of Definition 24.17.
