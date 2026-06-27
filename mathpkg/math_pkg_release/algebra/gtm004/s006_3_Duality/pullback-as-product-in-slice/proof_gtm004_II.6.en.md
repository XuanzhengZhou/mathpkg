---
role: proof
locale: en
of_concept: pullback-as-product-in-slice
source_book: gtm004
source_chapter: "II"
source_section: "6"
---

# Proof that the Pull-back is a Product in the Slice Category

Let $\Delta = \varphi \alpha = \psi \beta$ be the diagonal of the pull-back square

$$\begin{array}{ccc}
Y & \xrightarrow{\beta} & B \\
{\scriptstyle \alpha}\downarrow & & \downarrow{\scriptstyle \psi} \\
A & \xrightarrow{\varphi} & X
\end{array}$$

In the slice category $\mathfrak{C}/X$, objects are morphisms with codomain $X$. We regard $\varphi : A \to X$ and $\psi : B \to X$ as objects of $\mathfrak{C}/X$, and $\Delta = \varphi \alpha = \psi \beta : Y \to X$ as another object of $\mathfrak{C}/X$.

A morphism in $\mathfrak{C}/X$ from an object $\gamma : Z \to X$ to $\varphi : A \to X$ is a morphism $\zeta : Z \to A$ in $\mathfrak{C}$ such that $\varphi \zeta = \gamma$. With this interpretation:

- $\alpha : Y \to A$ satisfies $\varphi \alpha = \Delta$, so $\alpha$ is a morphism $\Delta \to \varphi$ in $\mathfrak{C}/X$.
- $\beta : Y \to B$ satisfies $\psi \beta = \Delta$, so $\beta$ is a morphism $\Delta \to \psi$ in $\mathfrak{C}/X$.

The universal property of the pull-back states: given any $\gamma : Z \to A$ and $\delta : Z \to B$ with $\varphi \gamma = \psi \delta = \kappa$, there exists a unique $\zeta : Z \to Y$ such that $\alpha \zeta = \gamma$ and $\beta \zeta = \delta$. This is precisely the universal property of the product of $\varphi$ and $\psi$ in $\mathfrak{C}/X$, with projections $\alpha$ and $\beta$.

Hence $(\Delta; \alpha, \beta)$ is the product of $\varphi$ and $\psi$ in $\mathfrak{C}/X$.
