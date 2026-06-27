---
role: proof
locale: en
of_concept: local-charts-on-jet-bundles
source_book: gtm014
source_chapter: "2"
source_section: "2. Jet Bundles"
---

We construct the chart $\tau_{U,V}$ and verify the smoothness of transition maps.

**Step 1: Definition of $\tau_{U,V}$.**

Given coordinate charts $\phi: U \to U' \subset \mathbf{R}^n$ and $\psi: V \to V' \subset \mathbf{R}^m$, let $\sigma \in J^k(U, V)$ have source $x_0$ and target $y_0$, represented by a smooth map $f: X \to Y$. Consider the coordinate representation $\psi \circ f \circ \phi^{-1}: U' \to \mathbf{R}^m$ with component functions $f_i$. Define

$$T_k(f_i)(x_0) = \sum_{1 \leq |\alpha| \leq k} \frac{\partial^{|\alpha|} f_i}{\partial x^\alpha}(x_0) (x - x_0)^\alpha \in A_n^k.$$

By Lemma 2.2, the partial derivatives $\partial^{|\alpha|} f_i / \partial x^\alpha(x_0)$ for $1 \leq |\alpha| \leq k$ depend only on the $k$-jet $\sigma$, so $T_k(f_i)(x_0)$ is well-defined. Set

$$\tau_{U,V}(\sigma) = (x_0, y_0, T_k(f_1)(x_0), \ldots, T_k(f_m)(x_0)) \in U \times V \times B_{n,m}^k.$$

Since two maps representing the same $k$-jet have identical Taylor polynomials of degree $k$, $\tau_{U,V}$ is injective. Given any $(x_0, y_0, P_1, \ldots, P_m) \in U \times V \times B_{n,m}^k$, the polynomial map $x \mapsto y_0 + (P_1(x - x_0), \ldots, P_m(x - x_0))$ defines a smooth map whose $k$-jet maps to this tuple, so $\tau_{U,V}$ is surjective.

**Step 2: Transition maps are smooth.**

Let $\phi_1, \psi_1, U_1, V_1$ be data for another chart $\tau_{U_1,V_1}$. The transition map is

$$\tau_{U_1,V_1} \circ \tau_{U,V}^{-1} = T_{U_1',V_1'} \circ (\phi_1^{-1})^* \circ (\psi_1)_* \circ (\psi_*)^{-1} \circ \phi^* \circ T_{U',V'}^{-1}$$

where $T_{U,V}$ denotes the natural identification of $J^k(U,V)$ with $U \times V \times B_{n,m}^k$. By the functoriality properties (Proposition 2.5), lower $*$ and upper $*$ commute, giving

$$\tau_{U_1,V_1} \circ \tau_{U,V}^{-1} = T_{U_1',V_1'} \circ (\phi_1^{-1} \circ \phi)^* \circ (\psi_1 \circ \psi^{-1})_* \circ T_{U',V'}^{-1}.$$

We need to show that for a smooth map $F: U' \to V'$ (here $F = \psi_1 \circ \psi^{-1} \circ f \circ \phi \circ \phi_1^{-1}$), the map

$$(x_0, y_0, D) \mapsto (g(x_0), h(y_0), T_k((h \circ f \circ g^{-1})_1)(g(x_0)), \ldots)$$

is smooth, where $g = \phi_1 \circ \phi^{-1}$ and $h = \psi_1 \circ \psi^{-1}$ are smooth transition functions. Here $D$ encodes the partial derivatives of $f$ up to order $k$.

The key computation: $T_k(\phi_i)(g(x_0)) = \sum_{1 \leq |\alpha| \leq k} \frac{\partial^{|\alpha|} \phi_i}{\partial x^\alpha}(g(x_0)) (x - g(x_0))^\alpha$, where $\phi = h \circ f \circ g^{-1}$. By the chain rule for higher derivatives (Faa di Bruno formula), each partial derivative $\partial^{|\alpha|} \phi_i / \partial x^\alpha(g(x_0))$ is a polynomial in the partial derivatives of $h$, $g^{-1}$ (which are fixed smooth functions) and the partial derivatives of $f$ up to order $|\alpha|$ at $x_0$ (which are encoded in $D$). Therefore the map $D \mapsto \partial^{|\alpha|} \phi_i / \partial x^\alpha(g(x_0))$ is smooth in $D$, and the transition map is smooth overall.

**Step 3: Source and target maps are submersions.**

In the local chart $\tau_{U,V}$, the source map $\alpha$ corresponds to projection onto the first factor $U \times V \times B_{n,m}^k \to U$, which is a submersion. Indeed, for $\sigma$ represented by $f$, we have

$$\phi \circ \alpha \circ \tau_{U,V}^{-1}(x_0, y_0, D) = \phi \circ \alpha \circ (\psi_*)^{-1} \circ \phi^* \circ T_{U',V'}^{-1}(x_0, y_0, D) = x_0,$$

since $\alpha \circ j^k g = \mathrm{id}_X$ for any map $g$. Similarly $\beta$ projects onto the second factor and is a submersion.
