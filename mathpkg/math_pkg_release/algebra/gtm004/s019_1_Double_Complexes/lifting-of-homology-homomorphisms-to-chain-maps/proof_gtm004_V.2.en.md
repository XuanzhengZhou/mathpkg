---
role: proof
locale: en
of_concept: lifting-of-homology-homomorphisms-to-chain-maps
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "2. The Künneth Theorem"
---

# Proof of Lifting of Homology Homomorphisms to Chain Maps

**Lemma 2.3.** Let $C$, $D$ be chain complexes over the principal ideal domain $\Lambda$ and let $C$ be free. Let $\psi: H(C) \to H(D)$ be a homomorphism of graded modules. Then there exists a chain map $\varphi: C \to D$ such that $\varphi_* = \psi$.

**Proof.** We use the notation $Z_p = Z_p(C)$, $B_p = B_p(C)$, and barred letters for $D$.

Since $\Lambda$ is a p.i.d. and $C$ is free, each $B_{p-1}$ is free (as a submodule of the free module $C_{p-1}$). Therefore the short exact sequence
$$0 \to Z_p \to C_p \xrightarrow{\partial_p} B_{p-1} \to 0$$
splits, and we may write
$$C_p = Z_p \oplus Y_p,$$
where $\partial_p|_{Y_p}: Y_p \xrightarrow{\sim} B_{p-1}$ is an isomorphism.

Now we construct $\varphi$ degreewise. For each $p$, consider the diagram induced by the homology homomorphism:
$$\begin{CD}
0 @>>> B_p @>>> Z_p @>>> H_p(C) @>>> 0 \\
@. @V{\theta_p}VV @VV{\varphi_p^1}V @VV{\psi_p}V \\
0 @>>> \bar{B}_p @>>> \bar{Z}_p @>>> \bar{H}_p(D) @>>> 0
\end{CD}$$

Since $Z_p$ is free (hence projective), we can lift $\psi_p: H_p(C) \to \bar{H}_p(D)$ to a map $\varphi_p^1: Z_p \to \bar{Z}_p$. This lifting automatically induces a map $\theta_p: B_p \to \bar{B}_p$ on the kernels.

Next, we must extend $\varphi_p^1$ to all of $C_p = Z_p \oplus Y_p$. Define $\varphi_p^2: Y_p \to D_p$ as follows: for $y \in Y_p$, we have $\partial y \in B_{p-1}$. Set
$$\varphi_p^2(y) = \bar{\partial}^{-1} \circ \theta_{p-1} \circ \partial(y),$$
where $\bar{\partial}^{-1}: \bar{B}_{p-1} \to \bar{Y}_{p-1}$ is the chosen splitting inverse for $\bar{\partial}$ (since $D_{p-1} = \bar{Z}_{p-1} \oplus \bar{Y}_{p-1}$ and $\bar{\partial}|_{\bar{Y}_{p-1}}$ is an isomorphism onto $\bar{B}_{p-2}$... actually $\bar{\partial}: \bar{Y}_p \to \bar{B}_{p-1}$).

Now define $\varphi_p = \langle \varphi_p^1, \varphi_p^2 \rangle: Z_p \oplus Y_p \to D_p$.

To verify that $\varphi$ is a chain map, we must show $\partial \varphi_p = \varphi_{p-1} \partial_p$. For $(z, y) \in Z_p \oplus Y_p = C_p$:
$$\partial_p(z, y) = \partial y \in B_{p-1} \subseteq Z_{p-1}.$$
On the other hand,
$$\varphi_p(z, y) = \varphi_p^1(z) + \varphi_p^2(y),$$
and applying $\partial$:
$$\partial \varphi_p(z, y) = \partial \varphi_p^1(z) + \partial \varphi_p^2(y) = \theta_{p-1}(\partial z) + \theta_{p-1}(\partial y),$$
since $\varphi_p^1(z) \in \bar{Z}_p$ so $\partial \varphi_p^1(z) = 0$, and $\partial \varphi_p^2(y) = \theta_{p-1}(\partial y)$ by construction of $\varphi_p^2$.

But $\partial z = 0$ (as $z \in Z_p$), so $\partial \varphi_p(z,y) = \theta_{p-1}(\partial y) = \varphi_{p-1}^1(\partial y) = \varphi_{p-1}\partial_p(z,y)$.

Thus $\varphi$ is a chain map, and by construction $\varphi_*$ induces $\psi$ on homology.
