---
role: proof
locale: en
of_concept: maschke-theorem-homological
source_book: gtm004
source_chapter: "X. Survey of Some Applications"
source_section: "4. Modular Representation Theory"
---

# Proof of Theorem 4.1 (Maschke) — Homological Formulation

Let $G$ be a finite group and let $k$ be a field of characteristic $p$. The linear representations of $G$ over $k$ correspond to the finite-dimensional $kG$-modules.

Maschke's classical theorem (Theorem 16.6 in Chapter VI) states that the $kG$-modules are semisimple if $p$ does not divide the group order $|G|$. In homological terms, semisimplicity is equivalent to the vanishing of all $\operatorname{Ext}^1$ groups between $kG$-modules. Therefore, if $p \nmid |G|$, then $\operatorname{Ext}_{kG}^1(A, B) = 0$ for all $kG$-modules $A, B$.

For the converse, suppose $p$ divides $|G|$. Then one can exhibit specific $kG$-modules $A, B$ with $\operatorname{Ext}_{kG}^1(A, B) \neq 0$. A standard construction uses the failure of complete reducibility in the modular case: the trivial module $k$ may appear as a submodule of a nonsplit extension. Indeed, if $p \mid |G|$, the augmentation ideal of $kG$ provides a nonsplit extension, yielding a nonzero element in $\operatorname{Ext}_{kG}^1(k, \ker(\varepsilon))$, where $\varepsilon: kG \to k$ is the augmentation map.

Thus we have the equivalence:

> **Theorem 4.1 (Maschke).** There exist $kG$-modules $A, B$ with $\operatorname{Ext}_{kG}^1(A, B) \neq 0$ if and only if $p$ divides the group order $|G|$.

The forward direction (semisimplicity when $p \nmid |G|$) is the content of Maschke's classical theorem; the converse follows from the existence of a nonsplit extension of the trivial module in the modular case.
