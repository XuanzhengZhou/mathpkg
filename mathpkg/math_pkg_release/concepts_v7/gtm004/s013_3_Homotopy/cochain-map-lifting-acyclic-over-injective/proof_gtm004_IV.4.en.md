---
role: proof
locale: en
of_concept: cochain-map-lifting-acyclic-over-injective
source_book: gtm004
source_chapter: "IV"
source_section: "4. Projective and Injective Resolutions"
---

# Proof of Lifting of Cochain Maps from Acyclic to Injective Complexes

**Theorem 4.4.** Let

$$C : C^0 \rightarrow C^1 \rightarrow \cdots \rightarrow C^n \xrightarrow{\delta} C^{n+1} \rightarrow \cdots$$

be acyclic and let

$$D : D^0 \rightarrow D^1 \rightarrow \cdots \rightarrow D^n \xrightarrow{\delta} D^{n+1} \rightarrow \cdots$$

be injective (both positive cochain complexes). Then there exists, to every homomorphism $\bar{\varphi} : H^0(C) \rightarrow H^0(D)$, a cochain map $\varphi : C \rightarrow D$ inducing $\bar{\varphi}$. Moreover, two cochain maps $\varphi, \psi : C \rightarrow D$ inducing the same $\bar{\varphi}$ are homotopic.

*Proof.* This is the dual statement of Theorem 4.1. We outline the dualization.

Recall that a positive cochain complex $C$ is a sequence

$$0 \rightarrow C^0 \xrightarrow{\delta} C^1 \xrightarrow{\delta} C^2 \rightarrow \cdots$$

with $\delta^2 = 0$, $C^n = 0$ for $n < 0$. The cohomology is $H^n(C) = \ker \delta^n / \operatorname{im} \delta^{n-1}$. We call $C$ acyclic if $H^n(C) = 0$ for $n \neq 0$, and injective if each $C^n$ is an injective object.

**Existence of the cochain map.** Construct $\varphi^n : C^n \rightarrow D^n$ inductively using the injectivity of $D^n$ instead of the projectivity of $C_n$ in Theorem 4.1. For $n = 0$, since $C$ is acyclic, $0 \rightarrow H^0(C) \rightarrow C^0 \rightarrow C^1$ is exact. The homomorphism $\bar{\varphi} : H^0(C) \rightarrow H^0(D)$ lifts, via the injectivity of $D^0$ (applied to the embedding $H^0(D) \hookrightarrow D^0$), to $\varphi^0 : C^0 \rightarrow D^0$.

For the inductive step, suppose $\varphi^0, \ldots, \varphi^{n-1}$ have been defined with $\varphi^i \delta = \delta \varphi^{i-1}$ for $i = 1, \ldots, n-1$. Consider $\delta \varphi^{n-1} : C^{n-1} \rightarrow D^n$. One shows that $\delta \varphi^{n-1}$ vanishes on $\operatorname{im}(\delta : C^{n-2} \rightarrow C^{n-1})$, hence induces a map $\operatorname{coker}(\delta : C^{n-2} \rightarrow C^{n-1}) \rightarrow D^n$. By acyclicity and the injectivity of $D^n$, this extends to $\varphi^n : C^n \rightarrow D^n$ with $\varphi^n \delta = \delta \varphi^{n-1}$.

**Uniqueness up to homotopy.** If $\varphi, \psi : C \rightarrow D$ both induce $\bar{\varphi}$, construct a cochain homotopy $\Sigma^n : C^{n+1} \rightarrow D^n$ (a morphism of degree $-1$) inductively, using the injectivity of $D^n$ to lift the difference $\varphi^n - \psi^n$ through $\delta : D^{n-1} \rightarrow D^n$, in a manner dual to the construction in Theorem 4.1.

The verification that $\varphi - \psi = \delta \Sigma + \Sigma \delta$ follows by the same algebraic identities as in Theorem 4.1, with all arrows reversed. $\square$

**Remark.** This theorem is the dual counterpart of the comparison theorem; together they justify the definition of right derived functors via injective resolutions, guaranteeing independence from the choice of resolution.
