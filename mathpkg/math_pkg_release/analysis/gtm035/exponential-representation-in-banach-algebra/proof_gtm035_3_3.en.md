---
role: proof
locale: en
of_concept: exponential-representation-in-banach-algebra
source_book: gtm035
source_chapter: "3"
source_section: "3"
---
# Proof of Exponential Representation in Banach Algebra

Let $\mathfrak{A}$ be a Banach algebra and let $x \in \mathfrak{A}$ be such that $\sigma(x)$ is contained in a simply connected region $\Omega$ with $0 \notin \Omega$. Since $\Omega$ is simply connected and does not contain the origin, there exists a single-valued holomorphic branch of the logarithm on $\Omega$; denote it by $\Phi \in H(\Omega)$. Thus

$$\Phi(z) = \log z, \qquad z \in \Omega,$$

and consequently

$$\exp(\Phi(z)) = z, \qquad z \in \Omega.$$

That is, the function $G(z) := \exp(\Phi(z))$ is the identity function on $\Omega$: $G(z) = z$ for all $z \in \Omega$.

By Theorem 3.3 (the Gelfand Operational Calculus), since $\Omega$ is an open set containing $\sigma(x)$, there exists an algebra homomorphism

$$\tau : H(\Omega) \to \mathfrak{A}, \qquad F \mapsto F(x).$$

Set $y = \tau(\Phi) = \Phi(x) \in \mathfrak{A}$. Then, using the homomorphism property (part (a) of Theorem 3.3) together with the fact that the exponential function is entire (hence its restriction to $\Phi(\Omega)$ belongs to $H(\Phi(\Omega))$), we obtain

$$e^y = \exp(\Phi(x)) = (\exp \circ \Phi)(x) = G(x).$$

But $G(z) = z$ for all $z \in \Omega$, so by part (c) of Theorem 3.3 (the identity function maps to the element itself), we have $G(x) = x$. Therefore

$$x = e^y,$$

as required. $\square$
