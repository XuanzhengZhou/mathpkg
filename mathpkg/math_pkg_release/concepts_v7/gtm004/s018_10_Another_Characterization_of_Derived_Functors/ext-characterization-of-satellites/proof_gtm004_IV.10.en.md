---
role: proof
locale: en
of_concept: ext-characterization-of-satellites
source_book: gtm004
source_chapter: "IV"
source_section: "10. Another Characterization of Derived Functors"
---

# Proof of Natural Isomorphism Between Natural Transformations from Ext and Left Satellites

Let $R_q \xrightarrow{\mu} P_{q-1} \to P_{q-2} \to \dots \to P_0 \to A$ be an exact sequence with $P_0, P_1, \dots, P_{q-1}$ projective. For an additive covariant functor $T : \mathfrak{M}_\Lambda \to \mathfrak{Ab}$, the left satellite is defined by

$$\tilde{L}_q T A = \ker\left(T(\mu) : T(R_q) \to T(P_{q-1})\right).$$

We construct an isomorphism

$$\Gamma : [\operatorname{Ext}_\Lambda^q(A, -), T] \xrightarrow{\cong} \tilde{L}_q T A.$$

---

**Construction of $\Gamma$.** Let $\Phi : \operatorname{Ext}_\Lambda^q(A, -) \to T$ be a natural transformation. Since $\operatorname{Hom}_\Lambda(-, B)$ is left exact, we may apply Proposition 5.8 to obtain the following commutative diagram with exact rows:

$$\begin{CD}
\operatorname{Hom}_\Lambda(P_{q-1}, R_q) @>>> \operatorname{Hom}_\Lambda(R_q, R_q) @>>> \operatorname{Ext}_\Lambda^q(A, R_q) @>>> 0 \\
@V{\mu_*}VV @V{\mu_*}VV \\
\operatorname{Hom}_\Lambda(P_{q-1}, P_{q-1}) @>>> \operatorname{Hom}_\Lambda(R_q, P_{q-1}) @>>> \operatorname{Ext}_\Lambda^q(A, P_{q-1}) @>>> 0
\end{CD}$$

Let $\eta \in \operatorname{Ext}_\Lambda^q(A, R_q)$ be the image of $1_{R_q}$ under the connecting homomorphism $\operatorname{Hom}_\Lambda(R_q, R_q) \to \operatorname{Ext}_\Lambda^q(A, R_q)$. Since $\mu : R_q \to P_{q-1}$ factors through $P_{q-1}$, we have $\mu_*(\eta) = 0$ in $\operatorname{Ext}_\Lambda^q(A, P_{q-1})$.

Define

$$\Gamma(\Phi) = \Phi_{R_q}(\eta) \in T(R_q).$$

We must verify that $\Gamma(\Phi) \in \ker(T(\mu)) = \tilde{L}_q T A$. Consider the commutative square induced by the natural transformation $\Phi$:

$$\begin{CD}
\operatorname{Ext}_\Lambda^q(A, R_q) @>{\Phi_{R_q}}>> T(R_q) \\
@V{\mu_*}VV @V{T(\mu)}VV \\
\operatorname{Ext}_\Lambda^q(A, P_{q-1}) @>{\Phi_{P_{q-1}}}>> T(P_{q-1})
\end{CD}$$

Since $\mu_*(\eta) = 0$, we obtain

$$T(\mu)(\Phi_{R_q}(\eta)) = \Phi_{P_{q-1}}(\mu_*(\eta)) = \Phi_{P_{q-1}}(0) = 0.$$

Thus $\Gamma(\Phi) \in \ker(T(\mu)) = \tilde{L}_q T A$, as required.

---

**Construction of the inverse $\Gamma^{-1}$.** Given $\xi \in \tilde{L}_q T A = \ker(T(\mu))$, we define a natural transformation $\Phi : \operatorname{Ext}_\Lambda^q(A, -) \to T$ as follows.

For any $\Lambda$-module $M$ and any element $\varrho \in \operatorname{Ext}_\Lambda^q(A, M)$, the Yoneda description of $\operatorname{Ext}^q$ provides a homomorphism $\sigma : R_q \to M$ representing $\varrho$, meaning that $\varrho = \sigma_*(\eta)$. We then set

$$\Phi_M(\varrho) = T(\sigma)(\xi).$$

**Well-definedness.** Suppose $\sigma' : R_q \to M$ is another representative of $\varrho$. Then $\sigma - \sigma'$ factors through $P_{q-1}$, i.e., there exists $\nu : P_{q-1} \to M$ such that $\sigma - \sigma' = \nu \circ \mu$. Hence

$$T(\sigma - \sigma')(\xi) = T(\nu) \circ T(\mu)(\xi) = T(\nu)(0) = 0,$$

since $\xi \in \ker(T(\mu))$. Therefore $T(\sigma)(\xi) = T(\sigma')(\xi)$, and $\Phi_M(\varrho)$ is well-defined.

**Naturality.** Let $\varphi : M \to N$ be a homomorphism. Then $\varphi \circ \sigma : R_q \to N$ represents $\varphi_*(\varrho) \in \operatorname{Ext}_\Lambda^q(A, N)$. We have

$$\Phi_N(\varphi_*(\varrho)) = T(\varphi \circ \sigma)(\xi) = T(\varphi) \circ T(\sigma)(\xi) = T(\varphi)(\Phi_M(\varrho)).$$

Thus the diagram

$$\begin{CD}
\operatorname{Ext}_\Lambda^q(A, M) @>{\Phi_M}>> T(M) \\
@V{\varphi_*}VV @V{T(\varphi)}VV \\
\operatorname{Ext}_\Lambda^q(A, N) @>{\Phi_N}>> T(N)
\end{CD}$$

commutes, establishing naturality.

---

**The maps are mutually inverse.** Given $\xi \in \tilde{L}_q T A$, let $\Phi = \Gamma^{-1}(\xi)$. Then

$$\Gamma(\Phi) = \Phi_{R_q}(\eta) = T(1_{R_q})(\xi) = \xi.$$

Conversely, given $\Phi \in [\operatorname{Ext}_\Lambda^q(A, -), T]$, let $\xi = \Gamma(\Phi)$. For any $M$ and $\varrho = \sigma_*(\eta) \in \operatorname{Ext}_\Lambda^q(A, M)$, naturality of $\Phi$ gives

$$\Phi_M(\varrho) = \Phi_M(\sigma_*(\eta)) = T(\sigma)(\Phi_{R_q}(\eta)) = T(\sigma)(\xi),$$

which is precisely $\Gamma^{-1}(\xi)_M(\varrho)$. Hence $\Gamma^{-1} \circ \Gamma = 1$ and $\Gamma \circ \Gamma^{-1} = 1$.

---

**Remark.** For $q = 0$, the assertion of Theorem 10.1 reduces to the Yoneda lemma: $[\operatorname{Hom}_\Lambda(A, -), T] \cong T(A)$.

For the case $q = 1$, the isomorphism takes the concrete form: a natural transformation $\Phi : \operatorname{Ext}_\Lambda^1(A, -) \to T$ is uniquely determined by the element $\xi = \Phi_R(\eta) \in \tilde{L}_1 T A = \ker(T(R) \to T(P))$, where $R \to P \to A$ is a projective presentation.
