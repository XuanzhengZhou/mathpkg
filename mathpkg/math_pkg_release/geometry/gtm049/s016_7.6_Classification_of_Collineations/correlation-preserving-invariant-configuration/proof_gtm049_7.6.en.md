---
role: proof
locale: en
of_concept: correlation-preserving-invariant-configuration
source_book: gtm049
source_chapter: "7"
source_section: "7.6"
---

**Proof.** By Proposition 10, there is a module isomorphism $g$ of $V_f$ onto $(V^*)_{f^t}$. We show that the correlation $\mathcal{P}(g)_\circ$ has the required property.

For any $v$ in $V$ we have

$$vfg = (Xv)g = X(vg) = vgf^t.$$

Hence, for any $v, w$ in $V$,

$$(vf)(wg) = v(wgf^t),$$

by the definition of $f^t$,

$$= v(wfg),$$

by the last equation.

Suppose $M$ is $f$-invariant. Then for all $v$ in $(Mg)^\circ$ and all $w$ in $M$,

$$v(wfg) = 0,$$

whence

$$(vf)(wg) = 0.$$

Thus $(Mg)^\circ f \subset (Mg)^\circ$ and so $(Mg)^\circ$ is $f$-invariant. On the other hand, if $(Mg)^\circ$ is $f$-invariant, then

$$(vf)(wg) = 0$$

for all $v$ in $(Mg)^\circ$ and all $w$ in $M$ and therefore

$$v(wfg) = 0.$$

This shows that $Mfg \subset (Mg)^{\circ\circ} = Mg$ and so $Mf \subset M$, i.e., $M$ is $f$-invariant.

Thus the correlation $\mathcal{P}(g)_\circ$ sends the set of $f$-invariant subspaces to itself, mapping the invariant configuration of $\mathcal{P}(f)$ onto itself.
