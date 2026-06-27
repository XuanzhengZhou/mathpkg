---
role: proof
locale: en
of_concept: kleisli-category-of-a-monad
source_book: gtm005
source_chapter: "VI"
source_section: "5. Free Algebras for a Monad"
---

**Proof.** The construction proceeds in several steps.

**Category axioms.** Define the composite of $f^\flat : x_T \to y_T$ with $g^\flat : y_T \to z_T$ (where $f : x \to Ty$ and $g : y \to Tz$ in $X$) by

$$g^\flat \circ f^\flat = (\mu_z \circ Tg \circ f)^\flat : x_T \to z_T.$$

Associativity follows from a large diagram chase using the associativity of the monad multiplication $\mu$ and the naturality of $\mu$. The arrow $(\eta_x)^\flat : x_T \to x_T$ serves as the identity: for any $f^\flat : x_T \to y_T$, we have

$$f^\flat \circ (\eta_x)^\flat = (\mu_y \circ Tf \circ \eta_x)^\flat = (\mu_y \circ \eta_{Ty} \circ f)^\flat = f^\flat$$

by the unit law of the monad, and similarly $(\eta_y)^\flat \circ f^\flat = f^\flat$.

**Functors.** Define $F_T : X \to X_T$ on objects by $F_T x = x_T$ and on arrows $h : x \to y$ by $F_T h = (\eta_y \circ h)^\flat$. Then $F_T(g \circ h) = (\eta_z \circ g \circ h)^\flat = (\eta_z \circ g)^\flat \circ (\eta_y \circ h)^\flat$ using the definition of composition, verifying functoriality. Define $G_T : X_T \to X$ on objects by $G_T(x_T) = Tx$ and on arrows $f^\flat : x_T \to y_T$ by $G_T(f^\flat) = \mu_y \circ Tf : Tx \to Ty$. The functoriality of $G_T$ follows from the associativity law of $\mu$.

**Adjunction.** The bijection

$$\varphi_T : X_T(F_T x, y_T) = X_T(x_T, y_T) \cong X(x, Ty) = X(x, G_T y_T)$$

sends $f^\flat$ to $f$, which is clearly a bijection by construction. It is natural in $x$ and $y_T$. The unit is $\eta_x = \varphi_T(1_{F_T x}) = \varphi_T((\eta_x)^\flat)$, and the counit $\varepsilon_T$ is given by $(\varepsilon_T)_{y_T} = \varphi_T^{-1}(1_{G_T y_T}) = (1_{Ty})^\flat : (Ty)_T \to y_T$.

**Recovery of the monad.** The multiplication of the monad induced by the adjunction is $G_T \varepsilon_T F_T$. Evaluating on $x \in X$:

$$G_T(\varepsilon_T)_{F_T x} = G_T((\varepsilon_T)_{x_T}) = G_T((1_{Tx})^\flat) = \mu_x \circ T(1_{Tx}) = \mu_x,$$

which is exactly the original multiplication $\mu$. Therefore the adjunction $\langle F_T, G_T, \varphi_T \rangle$ defines the given monad $\langle T, \eta, \mu \rangle$. $\square$
