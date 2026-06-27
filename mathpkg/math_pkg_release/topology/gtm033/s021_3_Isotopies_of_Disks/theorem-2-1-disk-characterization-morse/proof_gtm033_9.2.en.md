---
role: proof
locale: en
of_concept: theorem-2-1-disk-characterization-morse
source_book: gtm033
source_chapter: "9"
source_section: "2"
---

# Proof of Theorem 2.1 (Disk Characterization via Morse Function)

Let $f: M \to \mathbb{R}$ be an admissible Morse function on a compact connected surface $M$. Suppose $f$ has exactly $3$ critical points, and these are of type $0, 0, 1$ (two minima and one saddle). Then $M \approx D^2$.

**Strategy of proof.** First we find another function $g: N \to \mathbb{R}$ of the same kind, on a surface $N$ which we know is diffeomorphic to $D^2$. Then we construct a homeomorphism from $M$ to $N$ using level curves and gradient lines of the two Morse functions. This homeomorphism is then smoothed to a diffeomorphism.

**Step 1: The model function.** Define the model function

$$g: \mathbb{R}^2 \to \mathbb{R}, \quad g(x,y) = \frac{x^4}{4} - \frac{x^3}{3} - x^2 + y^2 = \int_0^x t(t+1)(t-2)\,dt + y^2.$$

The critical points of $g$ are at $(0,0)$ (type $1$, a saddle), $(-1,0)$ (type $0$, a minimum), and $(2,0)$ (type $0$, a minimum). The three critical values are distinct. Let $N = g^{-1}(-\infty, \xi]$ for some regular value $\xi > 0$; then $N \approx D^2$.

**Step 2: Normalization.** Let $a, b, c \in M$ be the three critical points of $f$, with $a$ and $c$ local minima and $b$ a saddle. By slightly perturbing $f$ near $a$ and $c$ if necessary, we can assume $f(b) > f(a) > f(c)$. Let $\lambda: \mathbb{R} \to \mathbb{R}$ be a diffeomorphism matching the critical values of $f$ to those of $g$:

$$\lambda(f(a)) = g(-1,0), \quad \lambda(f(b)) = g(0,0), \quad \lambda(f(c)) = g(2,0).$$

After replacing $f$ by $\lambda \circ f$, we may assume the critical values coincide. Set $\xi = f(\partial M) = g(\partial N) > 0$, the maximum value.

**Step 3: Connectedness of the boundary.** First prove $\partial M$ is connected. By the regular interval theorem, it suffices to show $f^{-1}(\varepsilon)$ is connected for some small $\varepsilon > 0$. Give $M$ a Riemannian metric induced by Morse charts near critical points. Let $F_t$ be the flow of $-\operatorname{grad} f$, defined for all $t \geqslant 0$. For each $x \in M$, the limit $\bar{x} = \lim_{t \to \infty} F_t(x)$ exists and is a critical point of $f$. The set of points flowing to a given minimum forms an open disk.

**Step 4: Gradient-line homeomorphism.** Using a method of extending diffeomorphisms along gradient lines (Theorem 2.1 of the section, for open subsets of level surfaces), construct a homeomorphism $G$ between $M$ and $N$ that preserves level curves and gradient lines. The map is defined piecewise:

- On the descending disks $D \cup D'$ of the two minima, use a local model matching
- On a neighborhood $P_\varepsilon$ of the saddle, use a chart-based identification
- Elsewhere, extend along gradient lines

Verify that the piecewise definitions agree on overlaps (they preserve level curves and gradients), yielding a well-defined, bijective, continuous map $K: N \to M$.

**Step 5: Smoothing.** The map $K$ is a homeomorphism that is a diffeomorphism on the descending disks and on the complement of their interiors. By the smoothing theorem (Theorem 8.1.9), $K$ can be approximated by a diffeomorphism. Hence $M \approx N \approx D^2$. $\square$

**Remark.** The proof generalizes immediately to higher dimensions: if $f: M \to \mathbb{R}$ is an admissible Morse function on a compact connected $n$-manifold with exactly $3$ critical points of types $0, 0, 1$, then $M \approx D^n$ (Theorem 2.4).
