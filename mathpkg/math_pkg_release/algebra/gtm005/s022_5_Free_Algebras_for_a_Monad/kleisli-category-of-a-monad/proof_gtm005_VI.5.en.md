---
role: proof
locale: en
of_concept: kleisli-category-of-a-monad
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "5. Free Algebras for a Monad"
---

The construction is verified by checking the category axioms, functoriality, and adjunction conditions.

**Associativity of composition.** For arrows $f^\flat : x_T \to y_T$, $g^\flat : y_T \to z_T$, and $h^\flat : z_T \to w_T$, the composition defined by $g^\flat \circ f^\flat = (\mu_z \circ T g \circ f)^\flat$ is associative because $(h^\flat \circ g^\flat) \circ f^\flat = (\mu_w \circ T(h^\flat \circ g^\flat) \circ f)^\flat$. Expanding $h^\flat \circ g^\flat = (\mu_w \circ T h \circ g)^\flat$ and using naturality of $\mu$, one obtains $h^\flat \circ (g^\flat \circ f^\flat)$ by a large commutative diagram.

**Identity laws.** The arrow $(\eta_x)^\flat : x_T \to x_T$ is a two-sided identity: for any $f^\flat : x_T \to y_T$, we have $f^\flat \circ (\eta_x)^\flat = (\mu_y \circ T f \circ \eta_x)^\flat = (\mu_y \circ \eta_{T y} \circ f)^\flat = (1_{T y} \circ f)^\flat = f^\flat$, using the unit law $\mu_y \circ \eta_{T y} = 1_{T y}$. Similarly $(\eta_y)^\flat \circ f^\flat = (\mu_y \circ T \eta_y \circ f)^\flat = f^\flat$ by the other unit law $\mu_y \circ T \eta_y = 1_{T y}$.

**Functoriality of $F_T$.** $F_T$ preserves composition: $F_T(g \circ f) = (\eta_z \circ g \circ f)^\flat = (\mu_z \circ T \eta_z \circ g \circ f)^\flat$. Meanwhile $F_T g \circ F_T f = (\eta_z \circ g)^\flat \circ (\eta_y \circ f)^\flat = (\mu_z \circ T(\eta_z \circ g) \circ \eta_y \circ f)^\flat = (\mu_z \circ T \eta_z \circ T g \circ \eta_y \circ f)^\flat = (\mu_z \circ \eta_{T z} \circ g \circ f)^\flat = (g \circ f)^\flat$? Wait, this needs the definition: $F_T(f) = (\eta_y \circ f)^\flat$. For $f: x \to y$ and $g: y \to z$, $F_T(g \circ f) = (\eta_z \circ g \circ f)^\flat$. And $F_T g \circ F_T f = (\eta_z \circ g)^\flat \circ (\eta_y \circ f)^\flat = (\mu_z \circ T(\eta_z \circ g) \circ \eta_y \circ f)^\flat = (\mu_z \circ T \eta_z \circ T g \circ \eta_y \circ f)^\flat$. By naturality of $\eta$, $T g \circ \eta_y = \eta_{T z} \circ g$. Applying $\mu_z \circ T \eta_z = 1_{T z}$, one obtains $(\eta_z \circ g \circ f)^\flat = F_T(g \circ f)$, confirming functoriality.

**Functoriality of $G_T$.** For $f^\flat : x_T \to y_T$ and $g^\flat : y_T \to z_T$, we have $G_T(g^\flat \circ f^\flat) = G_T((\mu_z \circ T g \circ f)^\flat) = \mu_z \circ T(\mu_z \circ T g \circ f) = \mu_z \circ T \mu_z \circ T^2 g \circ T f$. Meanwhile $G_T(g^\flat) \circ G_T(f^\flat) = (\mu_z \circ T g) \circ (\mu_y \circ T f) = \mu_z \circ T g \circ \mu_y \circ T f = \mu_z \circ \mu_{T z} \circ T^2 g \circ T f$ by naturality of $\mu$. These are equal by the associativity law $\mu_z \circ T \mu_z = \mu_z \circ \mu_{T z}$.

**The adjunction $F_T \dashv G_T$.** By construction, $X_T(F_T x, y_T) = X_T(x_T, y_T) = \{f^\flat : x_T \to y_T \mid f : x \to T y\} \cong X(x, T y) = X(x, G_T y_T)$. The bijection $f^\flat \mapsto f$ is natural in $x$: for $h : x' \to x$, $(f^\flat \circ F_T h) \mapsto f \circ h$; and natural in $y_T$: for $k^\flat : y_T \to y'_T$, $(G_T k^\flat \circ f) \mapsto k^\flat \circ f^\flat$. The unit is $\eta$ and the counit $\varepsilon_T$ defined by $(\varepsilon_T)_{y_T} = (1_{T y})^\flat$ satisfies the triangular identities by construction. The monad of this adjunction is $G_T \varepsilon_T F_T = \mu$, which is precisely the original monad $\langle T, \eta, \mu \rangle$.
