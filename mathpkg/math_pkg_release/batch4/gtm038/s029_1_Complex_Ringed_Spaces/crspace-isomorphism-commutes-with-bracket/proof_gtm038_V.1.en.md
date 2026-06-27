---
role: proof
locale: en
of_concept: crspace-isomorphism-commutes-with-bracket
source_book: gtm038
source_chapter: "V"
source_section: "1"
---

Let $s \in \Gamma(V, \mathcal{H}_2)$ and let $x \in \tilde{\varphi}^{-1}(V)$. Then $\tilde{\varphi}(x) \in V$. By definition, the bracket is given by evaluation at the residue field:
$$[s](\tilde{\varphi}(x)) = \pi_{\tilde{\varphi}(x)}(s_{\tilde{\varphi}(x)}),$$
where $s_{\tilde{\varphi}(x)}$ is the germ of $s$ at $\tilde{\varphi}(x)$ and $\pi_y: (\mathcal{H}_2)_y \to (\mathcal{H}_2)_y/\mathfrak{m}_y \simeq \mathbb{C}$ is the canonical projection.

Since $\varphi_*$ is stalk-preserving with respect to $\tilde{\varphi}$, we have
$$(\varphi_*(s))_x = \varphi_{*,x}^{-1}(s_{\tilde{\varphi}(x)}),$$
where $\varphi_{*,x}: (\mathcal{H}_1)_x \to (\mathcal{H}_2)_{\tilde{\varphi}(x)}$ is the $\mathbb{C}$-algebra isomorphism on stalks. Then
$$[\varphi_*(s)](x) = \pi_x((\varphi_*(s))_x) = \pi_x(\varphi_{*,x}^{-1}(s_{\tilde{\varphi}(x)})).$$

By Lemma 2, the isomorphism $\varphi_{*,x}^{-1}$ maps the maximal ideal onto the maximal ideal, so it induces an isomorphism of the residue fields. Since both residue fields are canonically $\mathbb{C}$, this induced map is the identity on $\mathbb{C}$. Hence
$$\pi_x \circ \varphi_{*,x}^{-1} = \pi_{\tilde{\varphi}(x)}.$$

Therefore
$$[\varphi_*(s)](x) = \pi_{\tilde{\varphi}(x)}(s_{\tilde{\varphi}(x)}) = [s](\tilde{\varphi}(x)) = ([s] \circ \tilde{\varphi})(x) = \varphi^*([s])(x).$$

Since $x$ was arbitrary, $[\varphi_*(s)] = \varphi^*([s])$. The second statement follows by applying the first to the inverse isomorphism $\varphi^{-1}$.
