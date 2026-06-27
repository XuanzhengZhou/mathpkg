---
role: proof
locale: en
of_concept: derivations-correspond-to-homomorphisms-from-augmentation-ideal
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of Derivations Correspond to Homomorphisms from the Augmentation Ideal

**Theorem 5.1.** There is a natural isomorphism of abelian groups

$$\eta: \operatorname{Der}(G, A) \xrightarrow{\cong} \operatorname{Hom}_G(IG, A)$$

given by $\eta(d)(x-1) = dx$ for $x \in G$. Its inverse sends a $G$-module homomorphism $\varphi: IG \to A$ to the derivation $d_\varphi$ defined by $d_\varphi(x) = \varphi(x-1)$.

*Proof.* Given a derivation $d: G \to A$, define a map $\varphi_d: IG \to A$ on the generators $x-1$ of $IG$ by

$$\varphi_d(x-1) = dx, \quad x \in G.$$

We claim that $\varphi_d$ is a $G$-module homomorphism. Indeed, for $x, y \in G$,

$$\begin{aligned}
\varphi_d(x(y-1)) &= \varphi_d\big((xy-1) - (x-1)\big) \\
&= d(xy) - dx \\
&= dx + x(dy) - dx \qquad \text{(since $d$ is a derivation)} \\
&= x \circ (dy) \\
&= x \circ \varphi_d(y-1).
\end{aligned}$$

Thus $\varphi_d$ is a $G$-module homomorphism. We set $\eta(d) = \varphi_d$. It is clear that $\eta$ is a homomorphism of abelian groups: for derivations $d_1, d_2$, one has $\eta(d_1 + d_2)(x-1) = (d_1 + d_2)(x) = d_1 x + d_2 x = \eta(d_1)(x-1) + \eta(d_2)(x-1)$.

Conversely, given a $G$-module homomorphism $\varphi: IG \to A$, define a map $d_\varphi: G \to A$ by

$$d_\varphi(x) = \varphi(x-1), \quad x \in G.$$

We claim that $d_\varphi$ is a derivation. Indeed,

$$\begin{aligned}
d_\varphi(xy) &= \varphi(xy - 1) \\
&= \varphi\big(x(y-1) + (x-1)\big) \\
&= x \varphi(y-1) + \varphi(x-1) \\
&= x d_\varphi(y) + d_\varphi(x).
\end{aligned}$$

Thus $d_\varphi \in \operatorname{Der}(G, A)$. The two constructions are inverse to each other:

$$d_{\varphi_d}(x) = \varphi_d(x-1) = dx,$$

$$\varphi_{d_\varphi}(x-1) = d_\varphi(x) = \varphi(x-1).$$

Hence $\eta$ is an isomorphism of abelian groups. The naturality in $G$ and in the $G$-module $A$ is straightforward to verify. $\square$
