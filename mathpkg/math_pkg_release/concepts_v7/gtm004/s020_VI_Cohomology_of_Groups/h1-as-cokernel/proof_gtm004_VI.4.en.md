---
role: proof
locale: en
of_concept: h1-as-cokernel
source_book: gtm004
source_chapter: "VI"
source_section: "4"
---

# Proof of Proposition 4.5: $H^1(G, A)$ as Cokernel

By definition, $H^1(G, A) = \operatorname{Ext}_{\mathbb{Z}G}^1(\mathbb{Z}, A)$. To compute this, apply the functor $\operatorname{Hom}_{\mathbb{Z}G}(-, A)$ to the standard free presentation of $\mathbb{Z}$:

$$0 \longrightarrow IG \xrightarrow{\iota} \mathbb{Z}G \xrightarrow{\varepsilon} \mathbb{Z} \longrightarrow 0.$$

Since $\mathbb{Z}G$ is $\mathbb{Z}G$-free (hence projective), applying $\operatorname{Hom}_{\mathbb{Z}G}(-, A)$ yields an exact sequence

$$0 \longrightarrow \operatorname{Hom}_{\mathbb{Z}G}(\mathbb{Z}, A) \longrightarrow \operatorname{Hom}_{\mathbb{Z}G}(\mathbb{Z}G, A) \xrightarrow{\iota^*} \operatorname{Hom}_{\mathbb{Z}G}(IG, A) \longrightarrow \operatorname{Ext}_{\mathbb{Z}G}^1(\mathbb{Z}, A) \longrightarrow 0.$$

Now $\operatorname{Hom}_{\mathbb{Z}G}(\mathbb{Z}G, A) \cong A$ via the isomorphism $\varphi \mapsto \varphi(1)$. Under this identification, the map $\iota^*$ corresponds to

$$\iota^*: A \longrightarrow \operatorname{Hom}_{\mathbb{Z}G}(IG, A), \qquad \iota^*(a)(x-1) = x a - a,$$

for $a \in A$, $x \in G$. Indeed, the inclusion $\iota: IG \hookrightarrow \mathbb{Z}G$ sends $x-1$ to $x-1$, so $\iota^*(\varphi)(x-1) = \varphi(x-1) = \varphi(x) - \varphi(1) = x \varphi(1) - \varphi(1)$, and setting $a = \varphi(1)$ gives the formula.

By exactness of the sequence, the cokernel of $\iota^*$ is $\operatorname{Ext}_{\mathbb{Z}G}^1(\mathbb{Z}, A)$. Therefore

$$H^1(G, A) = \operatorname{coker}\big(\iota^*: A \longrightarrow \operatorname{Hom}_{\mathbb{Z}G}(IG, A)\big),$$

with $\iota^*(a)(x-1) = x a - a$.

**Special case: trivial $A$.** If $A$ is a trivial $G$-module, then $xa = a$ for all $x \in G$, so $\iota_*$ is the zero map. In this case $H^1(G, A) \cong \operatorname{Hom}_{\mathbb{Z}G}(IG, A)$.
