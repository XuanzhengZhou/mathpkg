---
role: proof
locale: en
of_concept: left-exactness-of-hom-functor
source_book: gtm004
source_chapter: "I. Modules"
source_section: "2. The Group of Homomorphisms"
---

# Proof of Left Exactness of the Hom Functor (Theorem 2.1)

**Theorem 2.1.** Let $B' \xrightarrow{\mu} B \xrightarrow{\varepsilon} B''$ be an exact sequence of $\Lambda$-modules. For every $\Lambda$-module $A$ the induced sequence

$$0 \to \operatorname{Hom}_\Lambda(A, B') \xrightarrow{\mu_*} \operatorname{Hom}_\Lambda(A, B) \xrightarrow{\varepsilon_*} \operatorname{Hom}_\Lambda(A, B'')$$

is exact.

*Proof.* We must verify three things: (a) $\mu_*$ is injective, (b) $\operatorname{im} \mu_* \subset \ker \varepsilon_*$, and (c) $\ker \varepsilon_* \subset \operatorname{im} \mu_*$.

**(a) $\mu_*$ is injective.** Assume that $\mu_*(\varphi) = \mu \circ \varphi$ is the zero map in the diagram

$$\begin{array}{c}
A \\
\downarrow \scriptstyle{\varphi} \\
B' \xrightarrow{\mu} B \xrightarrow{\varepsilon} B''
\end{array}$$

Since $\mu \circ \varphi = 0$ and $\mu: B' \to B$ is injective (exactness at $B'$ gives $\ker \mu = 0$), it follows that $\varphi: A \to B'$ is the zero map. Hence $\ker \mu_* = 0$, so $\mu_*$ is injective.

**(b) $\operatorname{im} \mu_* \subset \ker \varepsilon_*$.** A map in $\operatorname{im} \mu_*$ is of the form $\mu \circ \varphi$ for some $\varphi \in \operatorname{Hom}_\Lambda(A, B')$. Then

$$\varepsilon_*(\mu \circ \varphi) = \varepsilon \circ (\mu \circ \varphi) = (\varepsilon \circ \mu) \circ \varphi = 0 \circ \varphi = 0,$$

since $\varepsilon \circ \mu = 0$ by exactness of the original sequence ($\operatorname{im} \mu \subset \ker \varepsilon$). Thus $\mu \circ \varphi \in \ker \varepsilon_*$, establishing the inclusion.

**(c) $\ker \varepsilon_* \subset \operatorname{im} \mu_*$.** Let $\psi \in \operatorname{Hom}_\Lambda(A, B)$ satisfy $\varepsilon_*(\psi) = \varepsilon \circ \psi = 0$. Consider the diagram

$$\begin{array}{c}
A \\
\downarrow \scriptstyle{\psi} \\
B' \xrightarrow{\mu} B \xrightarrow{\varepsilon} B''
\end{array}$$

The condition $\varepsilon \circ \psi = 0$ means that the image of $\psi$ is contained in $\ker \varepsilon$. By exactness, $\ker \varepsilon = \operatorname{im} \mu$. Since $\mu$ is injective, it is an isomorphism $B' \xrightarrow{\cong} \operatorname{im} \mu = \ker \varepsilon$. Therefore $\psi$ factors uniquely through $\mu$: there exists a (unique) $\Lambda$-module homomorphism $\varphi: A \to B'$ such that $\mu \circ \varphi = \psi$. Explicitly, for $a \in A$, $\psi(a) \in \ker \varepsilon = \operatorname{im} \mu$, so there is a unique $b' \in B'$ with $\mu(b') = \psi(a)$; define $\varphi(a) = b'$. Then $\psi = \mu_*(\varphi) \in \operatorname{im} \mu_*$.

Parts (a), (b), (c) together establish the exactness of the induced sequence. $\square$

**Remark.** Even if $\varepsilon$ is surjective, the induced map $\varepsilon_* = \operatorname{Hom}_\Lambda(A, \varepsilon)$ is not, in general, surjective (see Exercise 2.1). This is why the Hom functor is only *left* exact.
