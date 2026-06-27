---
role: proof
locale: en
of_concept: representation-proper-orthochroneous-lorentz
source_book: gtm023
source_chapter: "XI"
source_section: "§5. Application to Lorentz-transformations, 11.20"
---

Let $T: S \to S$ be a proper orthochroneous Lorentz transformation. We consider two cases.

**Case 1: $T \iota = \iota$.** Using the isomorphism $\Omega: Q \to S$ from sec. 11.17, define

$$T' = \Omega^{-1} \circ T \circ \Omega$$

on $Q$. Then $T'$ satisfies $\langle T'\varphi, T'\psi \rangle = \langle \varphi, \psi \rangle$ and $T' \iota = \iota$. By the properties of the space $Q$ (sec. 11.14), $T'$ corresponds to a transformation of the form $\varphi \mapsto \beta \circ \varphi \circ \beta^{-1}$ for some $\beta$ with $(\beta, \beta) = 1$. Reversing the isomorphism:

$$T \sigma = (\Omega \circ T' \circ \Omega^{-1}) \sigma = \Omega(\beta \circ \Omega^{-1} \sigma \circ \beta^{-1}) = \beta \circ \sigma \circ \beta^{-1}.$$

Since $\beta^{-1} = \tilde{\beta}$ (property of $Q$), this can be written as

$$T \sigma = \beta \circ \sigma \circ \tilde{\beta} = T_{\beta} \sigma,$$

and $\det \beta = (\beta, \beta) = 1$.

**Case 2: $T \iota \neq \iota$.** Since $T$ is proper orthochroneous, $T \iota$ and $\iota$ are linearly independent. Consider the plane $F = \operatorname{span}\{\iota, T\iota\}$. Choose a vector $\omega \in F$ such that

$$\langle \iota, \omega \rangle = 0 \quad \text{and} \quad \langle \omega, \omega \rangle = 1.$$

By (11.70) and (11.71), these conditions are equivalent to $\operatorname{tr} \omega = 0$ and $\det \omega = -1$, whence $\omega \circ \omega = \iota$.

Since $T$ preserves the fore-cone and past-cone, $T \iota$ can be expressed as (cf. sec. 9.26)

$$T \iota = \iota \cosh \theta + \omega \sinh \theta$$

for some $\theta \in \mathbb{R}$. Define the selfadjoint transformation

$$\alpha = \iota \cosh \frac{\theta}{2} + \omega \sinh \frac{\theta}{2}.$$

One verifies that $\det \alpha = 1$:

$$\det \alpha = -\langle \alpha, \alpha \rangle = -\langle \iota, \iota \rangle \cosh^2 \frac{\theta}{2} - \langle \omega, \omega \rangle \sinh^2 \frac{\theta}{2} = 1 \cdot \cosh^2 \frac{\theta}{2} - 1 \cdot \sinh^2 \frac{\theta}{2} = 1.$$

Now consider $T_{\alpha}^{-1} \circ T$. One checks that $(T_{\alpha}^{-1} \circ T) \iota = \iota$, reducing to Case 1. Thus $T_{\alpha}^{-1} \circ T = T_{\beta}$ for some $\beta$ with $\det \beta = 1$, and

$$T = T_{\alpha} \circ T_{\beta} = T_{\alpha \circ \beta}$$

with $\det(\alpha \circ \beta) = \det \alpha \cdot \det \beta = 1$.
