---
role: proof
locale: en
of_concept: crspace-isomorphism-induces-section-isomorphism
source_book: gtm038
source_chapter: "V"
source_section: "1"
---

Since $\varphi$ is an isomorphism of complex ringed spaces, $\tilde{\varphi}: X_1 \to X_2$ is a homeomorphism and $\varphi_*$ is a sheaf isomorphism that is stalk-preserving with respect to $\tilde{\varphi}$, inducing $\mathbb{C}$-algebra isomorphisms $\varphi_{*,x}: (\mathcal{H}_1)_x \to (\mathcal{H}_2)_{\tilde{\varphi}(x)}$ on each stalk.

For any open set $V \subset X_2$, the preimage $U := \tilde{\varphi}^{-1}(V)$ is open in $X_1$. The sheaf isomorphism $\varphi_*$ provides, for each open subset, a $\mathbb{C}$-algebra isomorphism between the section algebras. Composing with the pullback by $\tilde{\varphi}$ yields the map
$$\tilde{\varphi}_V := \varphi_*^{-1} \circ \tilde{\varphi}^*: \Gamma(V, \mathcal{H}_2) \to \Gamma(U, \mathcal{H}_1),$$
where $\tilde{\varphi}^*(s) = s \circ \tilde{\varphi}$. Since both $\varphi_*^{-1}$ and $\tilde{\varphi}^*$ are $\mathbb{C}$-algebra homomorphisms (the latter because composition with a homeomorphism preserves the algebra structure), their composition $\tilde{\varphi}_V$ is a $\mathbb{C}$-algebra isomorphism. The inverse is given by $\varphi_* \circ (\tilde{\varphi}^{-1})^*$.
