---
role: proof
locale: en
of_concept: boundary-construction-for-dual-kunneth-splitting
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "3. The Dual Künneth Theorem"
---

# Proof of Boundary Construction for the Dual Künneth Splitting

**Lemma 3.2.** Given the construction in the proof of Theorem 3.1, the family of morphisms $\beta = \{\beta_{-p,q}\}$ defined by
$$\beta_{-p,q} = \langle \alpha_{-p,q}, (-1)^n \bar{\partial}^{-1} \circ \alpha_{-p+1,q-1} \circ \partial \rangle: C_p = Z_p \oplus Y_p \to D_{p+n}$$
is a boundary in $\operatorname{Hom}_\Lambda(C, D)$; that is, there exists $\gamma$ such that $\partial^H(\gamma) = \beta$.

**Proof.** Define $\gamma = \{\gamma_{-p,q}\}$ by setting, for each $p$, $q$,
$$\gamma_{-p,q} = \bar{\partial}^{-1} \circ \alpha_{-p,q-1}$$
on $Z_p$, and extending trivially to all of $C_p$. More precisely, we need to construct $\gamma: C_p \to D_{p+n-1}$ such that (3.7) holds.

Using the differential formula (1.6) for the Hom complex:
$$(\partial^H \gamma)_{-p,q} = (-1)^n \gamma_{-p+1,q} \partial + \bar{\partial} \gamma_{-p,q+1}.$$

We verify this on each summand of $C_p = Z_p \oplus Y_p$:

**On $Z_p$:** Since $Z_p$ consists of cycles, $\partial|_{Z_p} = 0$, so the first term vanishes. Thus
$$(\partial^H \gamma)_{-p,q}|_{Z_p} = \bar{\partial} \gamma_{-p,q+1}|_{Z_p} = \bar{\partial} \circ \bar{\partial}^{-1} \circ \alpha_{-p,q} = \alpha_{-p,q},$$
by the definition of $\gamma$ in (3.5).

**On $Y_p$:** For $y \in Y_p$, we have $\partial y \in B_{p-1} \subseteq Z_{p-1}$. The first term in $\partial^H \gamma$ acts as:
$$(-1)^n \gamma_{-p+1,q} \partial(y) = (-1)^n \bar{\partial}^{-1} \circ \alpha_{-p+1,q-1} \circ \partial(y),$$
since $\partial y \in Z_{p-1}$ and $\gamma$ on $Z_{p-1}$ is defined as $\bar{\partial}^{-1} \circ \alpha_{-p+1,q-1}$.

The second term $\bar{\partial} \gamma_{-p,q+1}$ on $Y_p$ gives zero because $\gamma$ is defined via $\bar{\partial}^{-1}$ on cycles, and on $Y_p$ the extension is chosen such that no additional contribution appears.

Thus on $Y_p$:
$$(\partial^H \gamma)_{-p,q} = (-1)^n \bar{\partial}^{-1} \circ \alpha_{-p+1,q-1} \circ \partial,$$
which is precisely the second component of $\beta_{-p,q}$.

Combining both summands, we obtain
$$(\partial^H \gamma)_{-p,q} = \langle \alpha_{-p,q}, (-1)^n \bar{\partial}^{-1} \circ \alpha_{-p+1,q-1} \circ \partial \rangle = \beta_{-p,q},$$
proving (3.7). Hence $\beta$ is a boundary. $\square$
