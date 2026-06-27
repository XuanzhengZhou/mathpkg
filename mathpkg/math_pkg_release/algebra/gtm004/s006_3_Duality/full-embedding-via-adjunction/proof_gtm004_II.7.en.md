---
role: proof
locale: en
of_concept: full-embedding-via-adjunction
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Full Embedding via Adjunction

Let $F \dashv G$ with unit $\varepsilon: 1 \to GF$ and counit $\delta: FG \to 1$. Assume the unit $\varepsilon$ is a natural equivalence (i.e., each component $\varepsilon_X: X \to GFX$ is an isomorphism). Then we claim $F$ is fully faithful.

For any $X, X' \in \mathfrak{C}$, consider the composition

$$\mathfrak{C}(X, X') \xrightarrow{F} \mathfrak{D}(FX, FX') \xrightarrow{\eta^{-1}} \mathfrak{C}(X, GFX'),$$

where $\eta^{-1}$ is the inverse of the adjugant equivalence $\eta: \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, GY)$ evaluated at $Y = FX'$. Explicitly, for $f: X \to X'$, we have

$$\eta^{-1}(Ff) = \delta_{FX'} \circ F(Ff) = \delta_{FX'} \circ F(GFf \circ \varepsilon_X).$$

But since $\varepsilon$ is a natural equivalence, $F$ is faithful: if $Ff = Fg$, then $\eta(Ff) = \eta(Fg)$, so $G(Ff) \circ \varepsilon_X = G(Fg) \circ \varepsilon_X$, hence $\varepsilon_{X'} \circ f = \varepsilon_{X'} \circ g$, and since $\varepsilon_{X'}$ is iso, $f = g$.

Moreover, $F$ is full: given any $h: FX \to FX'$ in $\mathfrak{D}$, apply $\eta$ to obtain $\psi = \eta(h) = Gh \circ \varepsilon_X: X \to GFX'$. Since $\varepsilon_{X'}$ is invertible, define $f = \varepsilon_{X'}^{-1} \circ \psi: X \to X'$. Then

$$Ff = F(\varepsilon_{X'}^{-1}) \circ F\psi = F(\varepsilon_{X'}^{-1}) \circ FGh \circ F\varepsilon_X.$$

Using naturality of $\delta$ and the triangular identities, one verifies $Ff = h$. Hence $F$ is fully faithful, i.e., a full embedding.

**Remark.** The condition $\varepsilon$ being an equivalence is equivalent to $F$ being fully faithful. This is a fundamental property: a left adjoint is fully faithful if and only if the unit of the adjunction is a natural isomorphism.
