---
role: proof
locale: en
of_concept: isomorphism-of-varieties-iff-coordinate-rings-isomorphic
source_book: gtm044
source_chapter: "8"
source_section: "Isomorphic varieties"
---

# Proof of Isomorphism of Varieties iff Coordinate Rings are C-Isomorphic

**Theorem 8.7.** Two irreducible affine varieties $V \subset \mathbb{C}_{X_1, \ldots, X_n}$ and $W \subset \mathbb{C}_{Y_1, \ldots, Y_m}$ are isomorphic iff their coordinate rings are $\mathbb{C}$-isomorphic.

*Proof.*

$\Leftarrow$: Suppose we are given a $\mathbb{C}$-algebra isomorphism

$$\varphi: \mathbb{C}[x] = \mathbb{C}[x_1, \ldots, x_n] \xrightarrow{\sim} \mathbb{C}[y_1, \ldots, y_m] = \mathbb{C}[y],$$

where $\mathbb{C}[x] = \mathbb{C}[X_1, \ldots, X_n]/\mathfrak{p}$ and $\mathbb{C}[y] = \mathbb{C}[Y_1, \ldots, Y_m]/\mathfrak{q}$ are the coordinate rings of $V = V(\mathfrak{p})$ and $W = V(\mathfrak{q})$, with $x_i = X_i + \mathfrak{p}$ and $y_j = Y_j + \mathfrak{q}$.

Since $\varphi$ is surjective, each generator $y_i \in \mathbb{C}[y]$ corresponds under $\varphi$ to some element of $\mathbb{C}[x]$; that is, there exists a polynomial $p_i^*(X) \in \mathbb{C}[X_1, \ldots, X_n]$ such that

$$y_i = \varphi^{-1}(p_i^*(x_1, \ldots, x_n)).$$

Equivalently, $\varphi(p_i^*(x)) = y_i$. Similarly, since $\varphi^{-1}$ is also surjective, for each $x_j$ there exists a polynomial $q_j^*(Y) \in \mathbb{C}[Y_1, \ldots, Y_m]$ such that

$$x_j = \varphi(q_j^*(y_1, \ldots, y_m)).$$

(Note that the polynomials $p_i^*$ and $q_j^*$ are not necessarily uniquely determined — they are lifts of the images to the polynomial ring.)

Write $(X_1, \ldots, X_n) = (X)$ and $(Y_1, \ldots, Y_m) = (Y)$, and define the polynomial maps

$$p^*: \mathbb{C}_X^n \to \mathbb{C}_Y^m, \quad p^*(X) = (p_1^*(X), \ldots, p_m^*(X)),$$
$$q^*: \mathbb{C}_Y^m \to \mathbb{C}_X^n, \quad q^*(Y) = (q_1^*(Y), \ldots, q_n^*(Y)). \tag{14}$$

We now show that $p^*|_V = (q^*|_W)^{-1}$, which means there is a bijective polynomial map from $V$ to $W$ whose inverse also has a polynomial extension to the ambient affine spaces.

Let $(a) = (a_1, \ldots, a_n)$ be any point of $V$. Then $(a)$ has the associated maximal ideal

$$\mathfrak{m} = (x_1 - a_1, \ldots, x_n - a_n) \subset \mathbb{C}[x].$$

Under the ring isomorphism $\varphi$, the maximal ideal $\mathfrak{m}$ corresponds to a maximal ideal $\varphi(\mathfrak{m})$ of $\mathbb{C}[y]$. By the Nullstellensatz correspondence, $\varphi(\mathfrak{m})$ is of the form $(y_1 - b_1, \ldots, y_m - b_m)$ for a unique point $(b) = (b_1, \ldots, b_m) \in W$. Now, in $\mathbb{C}[y]/\varphi(\mathfrak{m}) \cong \mathbb{C}$, the image of each $y_i$ is $b_i$. On the other hand, $y_i = \varphi(p_i^*(x))$, so the image of $\varphi(p_i^*(x))$ in the residue field is $p_i^*(a)$ (since $x_j \mapsto a_j$ modulo $\mathfrak{m}$). Therefore $b_i = p_i^*(a)$, which means $p^*(a) = (b) \in W$. Hence $p^*|_V$ maps $V$ into $W$.

A symmetric argument shows that $q^*|_W$ maps $W$ into $V$. Moreover, the composition $q^* \circ p^*|_V$ corresponds, at the level of coordinate functions, to substituting the $p_i^*$ into the $q_j^*$, and the ring isomorphism condition $\varphi^{-1} \circ \varphi = \mathrm{id}$ forces this composition to induce the identity on $\mathbb{C}[x]$, hence the identity map on $V$. Thus $p^*|_V: V \to W$ is a polynomial isomorphism with inverse $q^*|_W: W \to V$, so $V$ and $W$ are isomorphic varieties.

$\Rightarrow$: Conversely, suppose $V$ and $W$ are isomorphic as varieties. Let $p: V \to W$ be a polynomial isomorphism, with polynomial extensions

$$p^*: \mathbb{C}_X^n \to \mathbb{C}_Y^m, \quad q^*: \mathbb{C}_Y^m \to \mathbb{C}_X^n$$

such that $p^*|_V = p$ and $q^*|_W = p^{-1}$ (as in Definition 8.6, equation (13)).

Let $R_V = \mathbb{C}[X]/\mathfrak{p}$ and $R_W = \mathbb{C}[Y]/\mathfrak{q}$ be the coordinate rings of $V$ and $W$. Define a map

$$\Phi: \mathbb{C}[Y] \to \mathbb{C}[X]/\mathfrak{p}, \qquad \Phi(f) = f \circ p^* + \mathfrak{p}.$$

If $f \in \mathfrak{q} = I(W)$, then $f$ vanishes identically on $W$. Since $p^*(V) = W$, the composition $f \circ p^*$ vanishes on $V$, i.e., $f \circ p^* \in I(V) = \mathfrak{p}$. Hence $\Phi$ factors through the quotient, giving a well-defined $\mathbb{C}$-algebra homomorphism

$$\phi: R_W = \mathbb{C}[Y]/\mathfrak{q} \to \mathbb{C}[X]/\mathfrak{p} = R_V, \qquad \phi(f + \mathfrak{q}) = f \circ p^* + \mathfrak{p}.$$

Symmetrically, define

$$\psi: R_V \to R_W, \qquad \psi(g + \mathfrak{p}) = g \circ q^* + \mathfrak{q}.$$

Now for any $f + \mathfrak{q} \in R_W$,

$$\psi(\phi(f + \mathfrak{q})) = \psi(f \circ p^* + \mathfrak{p}) = (f \circ p^*) \circ q^* + \mathfrak{q} = f \circ (p^* \circ q^*) + \mathfrak{q}.$$

Since $p^* \circ q^*|_W = p \circ p^{-1} = \mathrm{id}_W$, the polynomial $f \circ (p^* \circ q^*) - f$ vanishes on $W$, hence belongs to $\mathfrak{q}$. Thus $\psi \circ \phi = \mathrm{id}_{R_W}$. Similarly $\phi \circ \psi = \mathrm{id}_{R_V}$. Therefore $\phi$ is a $\mathbb{C}$-algebra isomorphism between $R_V$ and $R_W$. $\square$
