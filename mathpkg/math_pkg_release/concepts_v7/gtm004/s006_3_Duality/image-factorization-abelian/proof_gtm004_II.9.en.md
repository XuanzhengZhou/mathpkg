---
role: proof
locale: en
of_concept: image-factorization-abelian
source_book: gtm004
source_chapter: "II"
source_section: "9"
---

# Proof of Image Factorization in an Abelian Category

Let $\varphi: A \to B$ be a morphism in the abelian category $\mathfrak{A}$.

**Step 1.** Let $\mu: K \to A$ be the kernel of $\varphi$ (exists by axiom (i)). Let $\eta: A \to I$ be the cokernel of $\mu$. Since $\varphi \circ \mu = 0$, the universal property of the cokernel yields a unique $\nu: I \to B$ such that $\varphi = \nu \circ \eta$.

**Lemma 9.7.** If $\mu = \ker \varphi$, then $\eta = \operatorname{coker} \mu$ has the property that $\mu = \ker \eta$, and consequently $\nu$ (where $\varphi = \nu \circ \eta$) is a monomorphism.

*Proof of Lemma 9.7.* By definition, $\mu = \ker \varphi$ and $\eta = \operatorname{coker} \mu$. In an abelian category, every monomorphism is the kernel of its cokernel (axiom (ii)); since kernels are always monomorphisms, $\mu$ is monic. Its cokernel $\eta$ is epimorphic. The universal property forces $\mu = \ker(\operatorname{coker} \mu) = \ker \eta$. Now suppose $\sigma: J \to I$ satisfies $\nu \circ \sigma = 0$. Then $\varphi \circ (\text{some lift}) = 0$, and by the kernel property of $\mu$, there exists $\tau$ with $\sigma \circ \eta = \mu \circ \tau$. Since $\mu = \ker \eta$, this yields $\sigma = 0$ after factoring through, establishing $\nu$ is monic. $\square$

**Step 2.** By Lemma 9.7, $\nu: I \to B$ is a monomorphism. Let $\varepsilon: B \to C$ be the cokernel of $\varphi$ (exists by axiom (i)). Since $\varepsilon \circ \varphi = 0$ and $\varphi = \nu \circ \eta$, we have $\varepsilon \circ \nu \circ \eta = 0$. Since $\eta$ is epimorphic, $\varepsilon \circ \nu = 0$. Since $\nu$ is monic and $\varepsilon$ is the cokernel of $\varphi$, the universal property forces $\nu = \ker \varepsilon$.

Thus we have constructed the sequence

$$S_{\varphi}: \quad K \xrightarrow{\mu} A \xrightarrow{\eta} I \xrightarrow{\nu} B \xrightarrow{\varepsilon} C,$$

where $\mu = \ker \varphi$, $\eta = \operatorname{coker} \mu$, $\nu = \ker \varepsilon$, $\varepsilon = \operatorname{coker} \varphi$, and $\varphi = \nu \circ \eta$. Here $\eta$ is epimorphic, $\nu$ is monomorphic, and this factorization is essentially unique: if $\varphi = \nu_1 \circ \eta_1$ with $\eta_1$ epic, $\nu_1$ monic, then $\ker \varphi = \ker \eta = \ker \eta_1$, so $\eta_1 = \omega \circ \eta$ for some isomorphism $\omega$, and consequently $\nu = \nu_1 \circ \omega$.

The object $I$ is called the **image** of $\varphi$, denoted $\operatorname{im} \varphi$.
