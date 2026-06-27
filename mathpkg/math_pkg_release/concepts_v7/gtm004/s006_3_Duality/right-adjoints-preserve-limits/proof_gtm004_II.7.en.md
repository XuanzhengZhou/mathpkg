---
role: proof
locale: en
of_concept: right-adjoints-preserve-limits
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Right Adjoints Preserve Limits (RAPL)

Let $F \dashv G$ with adjugant $\eta: \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, GY)$ and inverse $\xi$. Let

$$\begin{array}{ccc}
Y & \xrightarrow{\alpha} & A \\
{\scriptstyle \beta}\downarrow & & \downarrow{\scriptstyle \varphi} \\
B & \xrightarrow{\psi} & X
\end{array}$$

be a pull-back square in $\mathfrak{D}$. We claim that applying $G$ yields a pull-back square in $\mathfrak{C}$:

$$\begin{array}{ccc}
GY & \xrightarrow{G\alpha} & GA \\
{\scriptstyle G\beta}\downarrow & & \downarrow{\scriptstyle G\varphi} \\
GB & \xrightarrow{G\psi} & GX
\end{array}$$

Suppose given $\gamma: Z \to GA$, $\delta: Z \to GB$ in $\mathfrak{C}$ with $G\varphi \circ \gamma = G\psi \circ \delta$. Apply the inverse adjugant $\xi$ to $\gamma$ and $\delta$:

$$\xi(\gamma): FZ \to A, \qquad \xi(\delta): FZ \to B.$$

Since $\eta$ is natural, $G\varphi \circ \gamma = G\psi \circ \delta$ implies $\varphi \circ \xi(\gamma) = \psi \circ \xi(\delta)$. By the universal property of the pull-back in $\mathfrak{D}$, there exists a unique $\varrho: FZ \to Y$ such that

$$\alpha \circ \varrho = \xi(\gamma), \qquad \beta \circ \varrho = \xi(\delta).$$

Now apply $\eta$ to $\varrho$:

$$\eta(\varrho): Z \to GY,$$

and we have

$$G\alpha \circ \eta(\varrho) = \eta(\alpha \circ \varrho) = \eta(\xi(\gamma)) = \gamma,$$

$$G\beta \circ \eta(\varrho) = \eta(\beta \circ \varrho) = \eta(\xi(\delta)) = \delta.$$

Uniqueness of $\eta(\varrho)$ follows from the bijectivity of $\eta$ and the uniqueness of $\varrho$. Hence $G$ preserves pull-backs. The same argument, applied to the limit cone of any diagram, shows that $G$ preserves all (small) limits.

The preservation of kernels follows as a special case: the kernel of $\varphi: A \to B$ is the pull-back of $\varphi$ along the zero morphism $0 \to B$.
