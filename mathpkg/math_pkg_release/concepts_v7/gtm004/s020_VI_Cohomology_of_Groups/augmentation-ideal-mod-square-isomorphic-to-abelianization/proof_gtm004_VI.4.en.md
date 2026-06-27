---
role: proof
locale: en
of_concept: augmentation-ideal-mod-square-isomorphic-to-abelianization
source_book: gtm004
source_chapter: "VI"
source_section: "4"
---

# Proof of Lemma 4.1: $IG/(IG)^2 \cong G_{\text{ab}}$

Recall that $G_{\text{ab}} = G/G'$, where $G' = [G, G]$ is the commutator subgroup of $G$. We construct two mutually inverse homomorphisms.

**Construction of $\psi: G \to IG/(IG)^2$.** Define

$$\psi(x) = (x-1) + (IG)^2, \qquad x \in G.$$

We verify that $\psi$ is a group homomorphism. For $x, y \in G$,

$$\psi(xy) = (xy-1) + (IG)^2 = \big((x-1)(y-1) + (x-1) + (y-1)\big) + (IG)^2.$$

Since $(x-1)(y-1) \in (IG)^2$, we have

$$\psi(xy) = (x-1) + (y-1) + (IG)^2 = \psi(x) + \psi(y).$$

Thus $\psi$ is a homomorphism from $G$ into the abelian group $IG/(IG)^2$. By the universal property of the abelianization, $\psi$ factors uniquely through $G_{\text{ab}}$, yielding a homomorphism

$$\psi'': G_{\text{ab}} = G/G' \longrightarrow IG/(IG)^2, \qquad x G' \mapsto (x-1) + (IG)^2.$$

**Construction of $\varphi': IG \to G_{\text{ab}}$.** Recall that $IG$ is the free abelian group on $\{x-1 \mid 1 \neq x \in G\}$ (Lemma 1.2). Define $\varphi'$ on generators by

$$\varphi'(x-1) = x G' \in G_{\text{ab}}, \qquad x \in G, x \neq 1,$$

and extend $\mathbb{Z}$-linearly. We must check that $\varphi'$ vanishes on $(IG)^2$. For $x, y \in G$, using the relation in $IG$:

$$(x-1)(y-1) = (xy-1) - (x-1) - (y-1).$$

Applying $\varphi'$:

$$\varphi'((x-1)(y-1)) = \varphi'(xy-1) - \varphi'(x-1) - \varphi'(y-1) = (xy)G' - xG' - yG'.$$

In the abelian group $G_{\text{ab}}$, this equals $(xy)(x^{-1})(y^{-1}) G' = [x, y] G' = G'$, i.e. the identity element. Hence $\varphi'$ vanishes on all products $(x-1)(y-1)$, and therefore on the entire ideal $(IG)^2$. Thus $\varphi'$ induces a homomorphism

$$\varphi'': IG/(IG)^2 \longrightarrow G_{\text{ab}}.$$

**Inverse check.** For $x \in G$, $\varphi''(\psi''(xG')) = \varphi''((x-1) + (IG)^2) = xG'$, so $\varphi'' \circ \psi'' = \text{id}$. Conversely, $\psi''(\varphi''((x-1) + (IG)^2)) = \psi''(xG') = (x-1) + (IG)^2$, so $\psi'' \circ \varphi'' = \text{id}$.

Therefore $IG/(IG)^2 \cong G_{\text{ab}}$, as desired.
