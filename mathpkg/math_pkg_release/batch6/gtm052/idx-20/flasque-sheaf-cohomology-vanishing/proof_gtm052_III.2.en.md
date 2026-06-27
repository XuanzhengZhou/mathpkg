---
role: proof
locale: en
of_concept: flasque-sheaf-cohomology-vanishing
source_book: gtm052
source_chapter: "III"
source_section: "§2 Cohomology of Sheaves"
---

Embed $\mathcal{F}$ in an injective object $\mathcal{I}$ of $\mathfrak{Ab}(X)$ and let $\mathcal{G}$ be the quotient:

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{I} \rightarrow \mathcal{G} \rightarrow 0.$$

Then $\mathcal{F}$ is flasque by hypothesis, $\mathcal{I}$ is flasque by (2.4), and so $\mathcal{G}$ is flasque by (II, Ex. 1.16c). Now since $\mathcal{F}$ is flasque, we have an exact sequence (II, Ex. 1.16b)

$$0 \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{G}) \rightarrow 0.$$

On the other hand, since $\mathcal{I}$ is injective, we have $H^i(X, \mathcal{I}) = 0$ for $i > 0$ (1.1Ae). Thus from the long exact sequence of cohomology, we get $H^1(X, \mathcal{F}) = 0$ and $H^i(X, \mathcal{F}) \cong H^{i-1}(X, \mathcal{G})$ for each $i \geq 2$. But $\mathcal{G}$ is also flasque, so by induction on $i$ we get the result.
