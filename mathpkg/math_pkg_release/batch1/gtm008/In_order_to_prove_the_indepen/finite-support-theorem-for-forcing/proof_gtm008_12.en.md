---
role: proof
locale: en
of_concept: finite-support-theorem-for-forcing
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

Take $m$ to be the maximum of all $i \in \omega$ for which $F_i$ occurs in $arphi$ or $t$ or $p_i$ is not $1_i$.

By construction, any $\pi \in \mathbf{G}_m$ (the group of permutations of $\omega$ that fix all $i < m$) satisfies:
- $\pi(t) = t$ since $t$ only involves predicate symbols $F_i$ with $i < m$, and these indices are fixed by $\pi$.
- $\pi(arphi) = arphi$ since $arphi$ only involves predicate symbols $F_i$ with $i < m$, and these indices are fixed by $\pi$.
- $\pi(p) = p$ since $p$ has $p_i = 1_i$ for all $i \geq m$ (by definition of the weak product), so permuting coordinates $i \geq m$ does not change $p$.

Thus $m$ has the required properties.
