---
role: proof
locale: en
of_concept: chain-map-lifting-projective-over-acyclic
source_book: gtm004
source_chapter: "IV"
source_section: "4. Projective and Injective Resolutions"
---

# Proof of Lifting of Maps from Projective to Acyclic Complexes

**Theorem 4.1.** Let

$$C : \cdots \rightarrow C_n \xrightarrow{\partial} C_{n-1} \rightarrow \cdots \rightarrow C_0$$

be projective and let

$$D : \cdots \rightarrow D_n \xrightarrow{\partial} D_{n-1} \rightarrow \cdots \rightarrow D_0$$

be acyclic. Then there exists, to every homomorphism $\bar{\varphi} : H_0(C) \rightarrow H_0(D)$, a chain map $\varphi : C \rightarrow D$ inducing $\bar{\varphi}$. Moreover, two chain maps $\varphi, \psi : C \rightarrow D$ inducing the same homomorphism $\bar{\varphi}$ are homotopic.

*Proof.*

**Existence of the chain map.** The chain map $\varphi$ is constructed recursively.

*Base case.* Since $D$ is acyclic, the sequence $D_0 \rightarrow H_0(D) \rightarrow 0$ is exact. Consider the composition

$$C_0 \twoheadrightarrow H_0(C) \xrightarrow{\bar{\varphi}} H_0(D).$$

By the projectivity of $C_0$, there exists a lift $\varphi_0 : C_0 \rightarrow D_0$ such that the diagram

$$\begin{CD}
C_0 @>>> H_0(C) \\
@V{\varphi_0}VV @VV{\bar{\varphi}}V \\
D_0 @>>> H_0(D)
\end{CD}$$

commutes.

*Inductive step.* Suppose $n \geq 1$ and that $\varphi_0, \varphi_1, \ldots, \varphi_{n-1}$ have been defined satisfying the chain map condition

$$\partial \varphi_i = \varphi_{i-1} \partial, \qquad i = 1, \ldots, n-1.$$

Consider the morphism $\varphi_{n-1} \partial : C_n \rightarrow D_{n-1}$. Using the induction hypothesis,

$$\partial (\varphi_{n-1} \partial) = (\partial \varphi_{n-1}) \partial = (\varphi_{n-2} \partial) \partial = \varphi_{n-2} \partial^2 = 0.$$

Hence $\varphi_{n-1} \partial$ maps $C_n$ into $\ker(\partial : D_{n-1} \rightarrow D_{n-2})$. By acyclicity of $D$, $\ker(\partial : D_{n-1} \rightarrow D_{n-2}) = \operatorname{im}(\partial : D_n \rightarrow D_{n-1})$. Thus we have a factorization

$$C_n \xrightarrow{\varphi_{n-1} \partial} \operatorname{im}(\partial : D_n \rightarrow D_{n-1}) \hookrightarrow D_{n-1}.$$

Since $C_n$ is projective, the morphism $C_n \rightarrow \operatorname{im}(\partial : D_n \rightarrow D_{n-1})$ lifts through the epimorphism $D_n \twoheadrightarrow \operatorname{im}(\partial : D_n \rightarrow D_{n-1})$. That is, there exists $\varphi_n : C_n \rightarrow D_n$ such that

$$\partial \varphi_n = \varphi_{n-1} \partial.$$

This completes the recursive definition of $\varphi$.

**Uniqueness up to homotopy.** Let $\varphi, \psi : C \rightarrow D$ be two chain maps both inducing $\bar{\varphi} : H_0(C) \rightarrow H_0(D)$. We construct a homotopy $\Sigma : \varphi \simeq \psi$ recursively.

*Base case.* Since $\varphi_0$ and $\psi_0$ both induce $\bar{\varphi}$, the difference $\varphi_0 - \psi_0$ maps $C_0$ into

$$\ker(D_0 \rightarrow H_0(D)) = \operatorname{im}(\partial : D_1 \rightarrow D_0).$$

Since $C_0$ is projective, there exists a lift $\Sigma_0 : C_0 \rightarrow D_1$ such that

$$\varphi_0 - \psi_0 = \partial \Sigma_0.$$

*Inductive step.* Suppose $n \geq 1$ and that $\Sigma_0, \ldots, \Sigma_{n-1}$ have been defined satisfying

$$\varphi_r - \psi_r = \partial \Sigma_r + \Sigma_{r-1} \partial, \qquad r = 0, \ldots, n-1$$

(with $\Sigma_{-1} \partial$ understood to be zero). Consider the morphism

$$\varphi_n - \psi_n - \Sigma_{n-1} \partial : C_n \rightarrow D_n.$$

Applying $\partial$ and using the chain map condition yields

$$\begin{aligned}
\partial(\varphi_n - \psi_n - \Sigma_{n-1} \partial) &= \partial \varphi_n - \partial \psi_n - \partial \Sigma_{n-1} \partial \\
&= \varphi_{n-1} \partial - \psi_{n-1} \partial - \partial \Sigma_{n-1} \partial \\
&= (\varphi_{n-1} - \psi_{n-1} - \partial \Sigma_{n-1}) \partial.
\end{aligned}$$

By the induction hypothesis for $r = n-1$,

$$\varphi_{n-1} - \psi_{n-1} - \partial \Sigma_{n-1} = \Sigma_{n-2} \partial.$$

Substituting, we obtain

$$\partial(\varphi_n - \psi_n - \Sigma_{n-1} \partial) = \Sigma_{n-2} \partial \partial = 0.$$

Therefore $\varphi_n - \psi_n - \Sigma_{n-1} \partial$ maps $C_n$ into

$$\ker(\partial : D_n \rightarrow D_{n-1}) = \operatorname{im}(\partial : D_{n+1} \rightarrow D_n).$$

Since $C_n$ is projective, there exists a lift $\Sigma_n : C_n \rightarrow D_{n+1}$ such that

$$\varphi_n - \psi_n - \Sigma_{n-1} \partial = \partial \Sigma_n,$$

equivalently

$$\varphi_n - \psi_n = \partial \Sigma_n + \Sigma_{n-1} \partial.$$

This completes the recursive definition of $\Sigma$, proving that $\varphi \simeq \psi$. $\square$
