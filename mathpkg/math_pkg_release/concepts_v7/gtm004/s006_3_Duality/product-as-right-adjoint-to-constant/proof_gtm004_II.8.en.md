---
role: proof
locale: en
of_concept: product-as-right-adjoint-to-constant
source_book: gtm004
source_chapter: "II"
source_section: "8"
---

# Proof of Product as Right Adjoint to the Constant Functor

Let $P \dashv G$ where $P: \mathfrak{C} \to \mathfrak{C}^I$ is the constant functor (sending $X$ to the constant family $\{X_i = X\}_{i \in I}$) and $G: \mathfrak{C}^I \to \mathfrak{C}$ is its right adjoint. Let $\eta$ be the adjugant and $\delta: PG \to 1$ the counit.

Given a family of objects $\{X_i\}_{i \in I}$ in $\mathfrak{C}$, let $X = G(\{X_i\})$ and let $\delta_{\{X_i\}}: P(X) \to \{X_i\}$ be the component of the counit at $\{X_i\}$. The counit is a natural transformation whose $i$-th component is a morphism $p_i = (\delta_{\{X_i\}})_i: X \to X_i$.

We claim $(X; p_i)$ is the product of $\{X_i\}$. Indeed, given $f_i: Y \to X_i$ for all $i \in I$, we have a morphism $f = \{f_i\}: P(Y) \to \{X_i\}$ in $\mathfrak{C}^I$. Apply the adjugant $\eta$ to obtain a morphism

$$\eta(f): Y \to G(\{X_i\}) = X$$

such that, by the adjunction relation (7.3),

$$\delta_{\{X_i\}} \circ P(\eta(f)) = f.$$

The $i$-th component of this equation is $p_i \circ \eta(f) = f_i$, exactly the universal property of the product. Moreover, if $g: Y \to X$ satisfies $p_i \circ g = f_i$ for all $i$, then $\delta \circ P(g) = f$, so $g = \eta(f)$ by the bijectivity of $\eta$.

Thus the product functor $\prod_i: \mathfrak{C}^I \to \mathfrak{C}$ is precisely a right adjoint to the constant functor $P$, and the projections are the components of the counit.
