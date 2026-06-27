---
role: proof
locale: en
of_concept: h1-with-trivial-coefficients
source_book: gtm004
source_chapter: "VI"
source_section: "4"
---

# Proof of Theorem 4.6: $H^1(G, A) \cong \operatorname{Hom}(G_{\text{ab}}, A)$ for Trivial $A$

Let $A$ be a trivial $G$-module (i.e. $x a = a$ for all $x \in G$, $a \in A$) and let $B$ be a trivial right $G$-module.

**Cohomology.** From Proposition 4.5, we have

$$H^1(G, A) = \operatorname{coker}(\iota^*: A \to \operatorname{Hom}_{\mathbb{Z}G}(IG, A)), \qquad \iota^*(a)(x-1) = xa - a.$$

Since $A$ is trivial, $xa - a = a - a = 0$, so $\iota^*$ is the zero map and

$$H^1(G, A) \cong \operatorname{Hom}_{\mathbb{Z}G}(IG, A).$$

A $G$-module homomorphism $\varphi: IG \to A$ satisfies $\varphi(x \cdot u) = x \cdot \varphi(u) = \varphi(u)$ (since $A$ is trivial) for all $x \in G$, $u \in IG$. In particular, for $u = y-1$, $x(y-1) = (xy-1) - (x-1)$, and we compute:

$$\varphi((x-1)(y-1)) = \varphi((xy-1) - (x-1) - (y-1)) = \varphi(xy-1) - \varphi(x-1) - \varphi(y-1).$$

On the other hand, by $G$-linearity:

$$\varphi(x(y-1)) = x \cdot \varphi(y-1) = \varphi(y-1).$$

But $x(y-1) = (xy-1) - (x-1)$, so $\varphi(xy-1) - \varphi(x-1) = \varphi(y-1)$, hence

$$\varphi(xy-1) = \varphi(x-1) + \varphi(y-1).$$

This means the map $x \mapsto \varphi(x-1)$ is a group homomorphism $G \to A$. Moreover, $\varphi((x-1)(y-1)) = 0$ for all $x, y \in G$, which means $\varphi$ factors through $IG/(IG)^2$. Therefore any $G$-module homomorphism $\varphi: IG \to A$ corresponds uniquely to an abelian group homomorphism $IG/(IG)^2 \to A$.

By Lemma 4.1, $IG/(IG)^2 \cong G_{\text{ab}}$. Hence

$$H^1(G, A) \cong \operatorname{Hom}(IG/(IG)^2, A) \cong \operatorname{Hom}(G_{\text{ab}}, A).$$

**Homology.** From Proposition 4.2, for $B$ trivial we have $\iota_* = 0$, so

$$H_1(G, B) \cong B \otimes_{\mathbb{Z}G} IG.$$

Since $\mathbb{Z}G$ acts trivially on $B$, the tensor product reduces to the ordinary tensor product of abelian groups modulo the action of $(IG)^2$ (because any element of $(IG)^2$ acts as zero on the trivial module $B$ in the tensor product). More precisely,

$$B \otimes_{\mathbb{Z}G} IG \cong B \otimes_{\mathbb{Z}} (IG/(IG)^2) \cong B \otimes_{\mathbb{Z}} G_{\text{ab}},$$

where the last isomorphism uses Lemma 4.1. Thus

$$H_1(G, B) \cong B \otimes_{\mathbb{Z}} G_{\text{ab}}.$$

This completes the description of $H^1$ and $H_1$ with trivial coefficients.
