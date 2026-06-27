---
role: proof
locale: en
of_concept: epimorphism-iff-surjective-for-modules
source_book: gtm004
source_chapter: "I. Modules"
source_section: "6. Dualization, Injective Modules"
---

# Proof: In Module Categories, Epimorphisms Coincide with Surjective Homomorphisms

**($\Leftarrow$)** Suppose $\varepsilon : B \to C$ is surjective, and let $\alpha_1, \alpha_2 : C \to M$ be homomorphisms such that $\alpha_1 \varepsilon = \alpha_2 \varepsilon$. For any $c \in C$, surjectivity of $\varepsilon$ gives $b \in B$ with $\varepsilon(b) = c$. Then

$$\alpha_1(c) = \alpha_1(\varepsilon(b)) = (\alpha_1 \varepsilon)(b) = (\alpha_2 \varepsilon)(b) = \alpha_2(\varepsilon(b)) = \alpha_2(c).$$

Hence $\alpha_1 = \alpha_2$, so $\varepsilon$ is an epimorphism.

**($\Rightarrow$)** Suppose $\varepsilon : B \to C$ is epimorphic. Consider the canonical projection $\pi : C \to C/\varepsilon(B)$ and the zero map $0 : C \to C/\varepsilon(B)$. For all $b \in B$,

$$0(\varepsilon(b)) = 0, \qquad \pi(\varepsilon(b)) = 0 \text{ (since } \varepsilon(b) \in \varepsilon(B)\text{)}.$$

Thus $0 \circ \varepsilon = \pi \circ \varepsilon$. Since $\varepsilon$ is epimorphic, this implies $0 = \pi$, so $C/\varepsilon(B) = 0$ and therefore $C = \varepsilon(B)$. Thus $\varepsilon$ is surjective.
