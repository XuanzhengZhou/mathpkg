---
role: proof
locale: en
of_concept: triviality-of-normal-bundle-of-boundary
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Theorem 4.2 (Triviality of the Normal Bundle of the Boundary)

Let $M$ be an $n$-dimensional manifold with boundary $\partial M$, and let $\nu$ be the algebraic normal bundle of $\partial M$ in $M$. Recall that for $x \in \partial M$,

$$\nu_x = T_x M / T_x (\partial M),$$

a $1$-dimensional real vector space. The bundle $\nu$ is a $1$-plane bundle over $\partial M$.

**Step 1: Local description at the boundary.** Let $n = \dim M$. Set

$$\mathbb{R}_+^n = \{x \in \mathbb{R}^n : x_1 \geq 0\}, \quad \partial \mathbb{R}_+^n = \{x \in \mathbb{R}^n : x_1 = 0\} \cong \mathbb{R}^{n-1}.$$

Let $\pi: \mathbb{R}^n \to \mathbb{R}$ be the projection onto the first coordinate, $\pi(x_1, \ldots, x_n) = x_1$.

Choose a family of charts $\{\varphi_i: U_i \to \mathbb{R}_+^n\}$ of $M$ whose domains cover $\partial M$. Each $\varphi_i$ maps $U_i \cap \partial M$ into $\partial \mathbb{R}_+^n$.

**Step 2: Local trivialization of $\nu$.** For $x \in U_i \cap \partial M$, the derivative

$$T_x \varphi_i: T_x M \to \mathbb{R}^n$$

maps $T_x(\partial M)$ onto $\partial \mathbb{R}_+^n = \{0\} \times \mathbb{R}^{n-1}$ and therefore induces an isomorphism on the quotient:

$$\overline{T_x \varphi_i}: \nu_x = T_x M / T_x(\partial M) \xrightarrow{\cong} \mathbb{R}^n / (\{0\} \times \mathbb{R}^{n-1}) \cong \mathbb{R}.$$

Composing with $\pi$, we obtain a linear isomorphism

$$h_i(x) := \pi \circ \overline{T_x \varphi_i}: \nu_x \xrightarrow{\cong} \mathbb{R}.$$

Thus over $U_i \cap \partial M$ the bundle $\nu$ is trivialized by the map

$$(x, v) \mapsto (x, h_i(x)(v)) \in (U_i \cap \partial M) \times \mathbb{R}.$$

**Step 3: Compatibility of trivializations.** Suppose $x \in U_i \cap U_j \cap \partial M$. The transition map

$$\psi = \varphi_j \circ \varphi_i^{-1}: \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j)$$

is a $C^r$ diffeomorphism between open subsets of $\mathbb{R}_+^n$ that preserves the boundary $\partial \mathbb{R}_+^n$. Hence for $y = \varphi_i(x) \in \partial \mathbb{R}_+^n$, the derivative $D\psi(y): \mathbb{R}^n \to \mathbb{R}^n$ maps the subspace $\partial \mathbb{R}_+^n$ to itself and maps the inward half-space to the inward half-space. Consequently, $D\psi(y)(e_1)$ has a positive first coordinate:

$$D\psi(y)(e_1) = \lambda e_1 + w, \quad \lambda > 0, \quad w \in \partial \mathbb{R}_+^n.$$

It follows that the two trivializations $h_i(x)$ and $h_j(x)$ of $\nu_x$ are related by

$$h_j(x) = \lambda_{ij}(x) \cdot h_i(x)$$

where $\lambda_{ij}(x) > 0$ is the $(1,1)$-entry of the Jacobian matrix of $\psi$ at $\varphi_i(x)$. Thus the transition functions $g_{ij}(x) = \lambda_{ij}(x)$ take values in the multiplicative group $\mathbb{R}_+ = (0, \infty)$.

**Step 4: Global trivialization.** The cocycle $\{g_{ij}\}$ defines $\nu$ as a line bundle with structure group $\mathbb{R}_+$. Since $\mathbb{R}_+$ is contractible (it is diffeomorphic to $\mathbb{R}$ via the logarithm), every $\mathbb{R}_+$-bundle is trivial. Explicitly, one can construct a global nonvanishing section of $\nu$ as follows. Equip $M$ with a Riemannian metric (using a partition of unity). Then $T(\partial M)$ has an orthogonal complement in $TM|_{\partial M}$, which is isomorphic to $\nu$. For each boundary chart $\varphi_i$, the vector field

$$v_i(x) := (T_x \varphi_i)^{-1}(e_1)$$

points inward (into $M$) and is orthogonal to $T_x(\partial M)$ if we use the pullback metric. In the overlap $U_i \cap U_j$, $v_i$ and $v_j$ are positive scalar multiples of each other. Using a partition of unity $\{\rho_i\}$ subordinate to $\{U_i\}$, define

$$v(x) := \sum_i \rho_i(x) v_i(x), \quad x \in \partial M.$$

Each $v_i(x)$ lies in the same $1$-dimensional space $\nu_x$ and are positive multiples of one another; the convex combination with $\rho_i(x) \geq 0$ (not all zero) therefore yields a nonvanishing section $v$ of $\nu$. A nonvanishing global section of a $1$-dimensional vector bundle provides a trivialization $\nu \cong \partial M \times \mathbb{R}$ via $(x, t) \mapsto t \cdot v(x)$.

**Conclusion.** The normal bundle $\nu$ of $\partial M$ in $M$ is trivial, and consequently orientable (every trivial bundle admits an obvious orientation).

QED
