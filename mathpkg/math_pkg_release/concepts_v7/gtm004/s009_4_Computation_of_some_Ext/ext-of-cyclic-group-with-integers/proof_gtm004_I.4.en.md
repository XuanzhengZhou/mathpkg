---
role: proof
locale: en
of_concept: ext-of-cyclic-group-with-integers
source_book: gtm004
source_chapter: "I"
source_section: "4. Computation of some Ext-Groups"
---

# Proof: $\operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z}) \cong \mathbb{Z}_r$

Here $\operatorname{Ext}$ denotes $\operatorname{Ext}_{\mathbb{Z}}$, the Ext functor over the ring of integers.

## Preliminaries

Since $\mathbb{Z}$ is a projective $\mathbb{Z}$-module, Proposition 2.6 yields

$$\operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) = 0 = \operatorname{Ext}(\mathbb{Z}, \mathbb{Z}_q)$$

for any integer $q$.

## Computation of $\operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z})$

To compute $\operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z})$, we use the projective presentation

$$\mathbb{Z} \xrightarrow{\;\mu\;} \mathbb{Z} \xrightarrow{\;\varepsilon\;} \mathbb{Z}_r \longrightarrow 0,$$

where $\mu$ is multiplication by $r$ and $\varepsilon$ is the canonical projection modulo $r$. (Note that $\mathbb{Z}$ is projective over itself.)

Applying the contravariant functor $\operatorname{Hom}(-, \mathbb{Z})$ to this projective presentation yields, by the definition of $\operatorname{Ext}$ (Proposition 2.6), the exact sequence

$$\operatorname{Hom}(\mathbb{Z}_r, \mathbb{Z}) \longrightarrow \operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \xrightarrow{\;\mu^*\;} \operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \longrightarrow \operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z}) \longrightarrow 0.$$

Now we evaluate each term:

- $\operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}$, via the isomorphism sending a homomorphism $\varphi$ to $\varphi(1)$.
- $\operatorname{Hom}(\mathbb{Z}_r, \mathbb{Z}) = 0$, because any homomorphism from a finite cyclic group to the infinite cyclic group must be zero (there are no elements of finite order in $\mathbb{Z}$ except $0$).
- Under the identification $\operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}$, the induced map $\mu^*$ is again multiplication by $r$. Indeed, for $\varphi \in \operatorname{Hom}(\mathbb{Z}, \mathbb{Z})$, we have $\mu^*(\varphi) = \varphi \circ \mu$, and evaluating at $1$:

  $$(\varphi \circ \mu)(1) = \varphi(r \cdot 1) = \varphi(r) = r \cdot \varphi(1),$$

  so $\mu^*$ corresponds to the map $\mathbb{Z} \xrightarrow{r} \mathbb{Z}$.

Thus the exact sequence becomes

$$0 \longrightarrow \mathbb{Z} \xrightarrow{\;r\;} \mathbb{Z} \longrightarrow \operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z}) \longrightarrow 0.$$

Since the cokernel of multiplication by $r$ on $\mathbb{Z}$ is $\mathbb{Z}/r\mathbb{Z} \cong \mathbb{Z}_r$, we obtain

$$\operatorname{Ext}(\mathbb{Z}_r, \mathbb{Z}) \cong \mathbb{Z}_r.$$
