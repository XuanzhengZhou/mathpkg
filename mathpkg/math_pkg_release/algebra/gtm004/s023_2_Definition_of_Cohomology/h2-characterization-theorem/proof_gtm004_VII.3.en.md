---
role: proof
locale: en
of_concept: h2-characterization-theorem
source_book: gtm004
source_chapter: "VII"
source_section: "3. H^2 and Extensions"
---

# Proof of Characterization of $H^2$ via Equivalence Classes of Extensions

**Theorem 3.3.** There is a one-to-one correspondence between $M(\mathfrak{h}, A)$ (the set of equivalence classes of extensions of $\mathfrak{h}$ by the $\mathfrak{h}$-module $A$) and $H^2(\mathfrak{h}, A)$.

---

## Proof

The proof proceeds formally just as for groups (Section VI.10). We construct mutually inverse maps between (equivalence classes of) extensions and 2-cocycles (modulo 2-coboundaries).

### Step 1: From an extension to a 2-cocycle

Let $A \overset{i}{\hookrightarrow} \mathfrak{g} \overset{p}{\twoheadrightarrow} \mathfrak{h}$ be an extension of $\mathfrak{h}$ by the $\mathfrak{h}$-module $A$. Choose a $K$-linear section $s: \mathfrak{h} \to \mathfrak{g}$ (i.e. $p \circ s = 1_{\mathfrak{h}}$) with $s(0) = 0$. For $x, y \in \mathfrak{h}$, the element
$$s([x, y]) - [s(x), s(y)] \in \ker(p) = i(A).$$
Define $f: \mathfrak{h} \times \mathfrak{h} \to A$ by
$$i(f(x, y)) = s([x, y]) - [s(x), s(y)], \qquad x, y \in \mathfrak{h}.$$

One verifies that $f$ is a 2-cocycle, meaning it satisfies:
\begin{align}
&f(x, y) + f(y, x) = 0, \tag{skew-symmetry} \\
&f([x, y], z) + f([y, z], x) + f([z, x], y) \notag \\
&\qquad = x \circ f(y, z) + y \circ f(z, x) + z \circ f(x, y). \tag{2-cocycle condition}
\end{align}

The skew-symmetry follows because $s([x,y]) - [s(x), s(y)] = -(s([y,x]) - [s(y), s(x)])$ (since $[x,y] = -[y,x]$ and $[s(x), s(y)] = -[s(y), s(x)]$). The 2-cocycle condition follows from the Jacobi identity in $\mathfrak{g}$ expressed in terms of the section $s$, using the fact that $s([x,y]) - [s(x), s(y)]$ lies in the abelian kernel.

If a different section $s'$ is chosen, then $s'(x) - s(x) \in i(A)$, say $s'(x) - s(x) = i(g(x))$ for some $K$-linear map $g: \mathfrak{h} \to A$. The corresponding 2-cocycles differ by the 2-coboundary $\delta g$:
$$f'(x, y) - f(x, y) = g([x, y]) - x \circ g(y) + y \circ g(x),$$
which is precisely the coboundary of $g$. Moreover, equivalent extensions yield cohomologous 2-cocycles. Hence the construction gives a well-defined map
$$\Phi: M(\mathfrak{h}, A) \to H^2(\mathfrak{h}, A).$$

### Step 2: From a 2-cocycle to an extension

Let $f: \mathfrak{h} \times \mathfrak{h} \to A$ be a 2-cocycle. Define a Lie algebra structure on the $K$-vector space $A \oplus \mathfrak{h}$ by
$$[(a, x), (b, y)] = (x \circ b - y \circ a + f(x, y), \; [x, y]),$$
where $a, b \in A$ and $x, y \in \mathfrak{h}$. The skew-symmetry of $f$ ensures that this bracket is alternating:
$$[(a, x), (a, x)] = (x \circ a - x \circ a + f(x, x), \; [x, x]) = (0, 0).$$

The Jacobi identity for this bracket follows from the 2-cocycle condition on $f$ together with the Jacobi identity in $\mathfrak{h}$ and the $\mathfrak{h}$-module structure on $A$. A direct computation verifies:
\begin{align*}
&[(a,x), [(b,y), (c,z)]] + [(b,y), [(c,z), (a,x)]] + [(c,z), [(a,x), (b,y)]] \\
&\quad = \bigl(x \circ (y \circ c - z \circ b + f(y,z)) - [y,z] \circ a + f(x, [y,z]) \\
&\qquad + \text{cyclic permutations}, \; [x, [y,z]] + [y, [z,x]] + [z, [x,y]] \bigr) = (0, 0).
\end{align*}
The third component vanishes by the Jacobi identity in $\mathfrak{h}$, and the first component vanishes by the 2-cocycle condition on $f$.

Denote this Lie algebra by $\mathfrak{g}_f$. The obvious maps
$$A \overset{i}{\hookrightarrow} \mathfrak{g}_f, \quad a \mapsto (a, 0); \qquad \mathfrak{g}_f \overset{p}{\twoheadrightarrow} \mathfrak{h}, \quad (a, x) \mapsto x,$$
constitute an extension of $\mathfrak{h}$ by $A$. The $\mathfrak{h}$-module structure induced by this extension (using the canonical section $s(x) = (0, x)$) agrees with the given $\mathfrak{h}$-module structure on $A$:
$$[s(x), i(a)] = [(0, x), (a, 0)] = (x \circ a, 0) = i(x \circ a).$$

If $f$ is replaced by a cohomologous 2-cocycle $f' = f + \delta g$, the map $\varphi: \mathfrak{g}_f \to \mathfrak{g}_{f'}$ defined by $\varphi(a, x) = (a + g(x), x)$ is an equivalence of extensions. Hence we obtain a well-defined map
$$\Psi: H^2(\mathfrak{h}, A) \to M(\mathfrak{h}, A).$$

### Step 3: $\Phi$ and $\Psi$ are mutually inverse

Given an extension, construct its 2-cocycle $f$ via a section $s$, then construct $\mathfrak{g}_f$: the map $(a, x) \mapsto i(a) + s(x)$ is an isomorphism $\mathfrak{g}_f \to \mathfrak{g}$ commuting with the extension structure, showing $\Psi(\Phi([\mathfrak{g}])) = [\mathfrak{g}]$.

Conversely, given a 2-cocycle $f$, construct $\mathfrak{g}_f$ and take the canonical section $s(x) = (0, x)$; the resulting 2-cocycle is exactly $f$, showing $\Phi(\Psi([f])) = [f]$.

Thus $M(\mathfrak{h}, A)$ is in bijection with $H^2(\mathfrak{h}, A)$. Under this correspondence, the class of the split extension $A \rtimes \mathfrak{h}$ corresponds to the zero element $0 \in H^2(\mathfrak{h}, A)$. $\square$
