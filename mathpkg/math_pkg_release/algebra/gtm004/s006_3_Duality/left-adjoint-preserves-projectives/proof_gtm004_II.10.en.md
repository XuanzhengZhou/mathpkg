---
role: proof
locale: en
of_concept: left-adjoint-preserves-projectives
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Left Adjoint Preserves Projectives

Let $F: \mathfrak{C} \to \mathfrak{D}$ and $F \dashv G$ with adjugant $\eta: \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, GY)$. Assume $G$ maps epimorphisms to epimorphisms.

Let $P \in \mathfrak{C}$ be projective. We show $FP \in \mathfrak{D}$ is projective. Consider a diagram in $\mathfrak{D}$:

$$\begin{array}{ccc}
FP & \xrightarrow{\varphi} & B \\
& & \downarrow{\scriptstyle \varepsilon} \\
A & \xrightarrow{\varepsilon} & B
\end{array}$$

with $\varepsilon$ epimorphic. Apply the adjugant $\eta = \eta_{P, -}$ to the morphism $\varphi: FP \to B$ to obtain

$$\eta(\varphi): P \to GB.$$

By hypothesis, $G\varepsilon: GA \to GB$ is epimorphic in $\mathfrak{C}$. We now have a diagram in $\mathfrak{C}$:

$$\begin{array}{ccc}
P & \xrightarrow{\eta(\varphi)} & GB \\
& & \downarrow{\scriptstyle G\varepsilon} \\
GA & \xrightarrow{G\varepsilon} & GB
\end{array}$$

Since $P$ is projective in $\mathfrak{C}$, there exists $\psi': P \to GA$ such that $G\varepsilon \circ \psi' = \eta(\varphi)$.

Now apply the inverse adjugant $\xi = \eta^{-1}$ to $\psi'$ to obtain $\psi = \xi(\psi'): FP \to A$. By the naturality of the adjugant (equation 7.1),

$$\eta(\varepsilon \circ \psi) = G\varepsilon \circ \eta(\psi) = G\varepsilon \circ \psi' = \eta(\varphi).$$

Since $\eta$ is bijective, $\varepsilon \circ \psi = \varphi$. Thus $FP$ is projective. $\square$
