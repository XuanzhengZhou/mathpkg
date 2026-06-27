---
role: proof
locale: en
of_concept: morse-cw-homotopy
source_book: gtm033
source_chapter: "6"
source_section: "6.4"
---

# Proof: Manifold Has Homotopy Type of a CW-Complex via Morse Theory

One can show that $M$ and $M - \partial M$ are homotopy equivalent (for example, by the collaring theorem, Theorem 2.1 of Chapter 6). Hence we can assume $\partial M = \varnothing$.

Choose a proper Morse function $f: M \to \mathbb{R}_+$, for example an approximation to the square of a proper embedding $M \hookrightarrow \mathbb{R}^N$. Assume $f$ separates the critical points $z_1, z_2, \ldots$, which are ordered so that $f(z_{i+1}) > f(z_i)$. Choose regular values $a_i$ so that

$$0 = a_0 < f(z_1) < a_1 < f(z_2) < a_2 < \cdots.$$

Note that $f(z_i) \to \infty$ since $f$ is proper and the $z_i$ are isolated; therefore $a_i \to \infty$ as well.

For each interval $[a_{k-1}, a_k]$, the restriction $f|_{f^{-1}[a_{k-1}, a_k]}$ is an admissible Morse function with a finite number of critical points all having a single critical value (after a small perturbation to separate them, as in Theorem 3.3). By Theorem 4.2 (which is a relative version of Theorem 3.3 adapted for CW-complexes), for each integer $k \geqslant 1$ there exist:

- A finite CW-complex $X_k$ of dimension at most $n$,
- Disjoint subcomplexes $Y_k, Z_k \subset X_k$,
- A homotopy equivalence

$$u_k: f^{-1}[a_{k-1}, a_k] \to X_k$$

taking $f^{-1}(a_{k-1})$ to $Y_k$ and $f^{-1}(a_k)$ to $Z_k$ by homotopy equivalences.

Let $v_k: Z_k \to f^{-1}(a_k)$ be a homotopy inverse to the restriction $u_k|_{f^{-1}(a_k)}: f^{-1}(a_k) \to Z_k$. The composition

$$Z_k \xrightarrow{v_k} f^{-1}(a_k) \xrightarrow{u_{k+1}|_{f^{-1}(a_k)}} Y_{k+1}$$

is a map between CW-complexes. By the cellular approximation theorem, this map is homotopic to a cellular map

$$w_k: Z_k \to Y_{k+1}.$$

A CW-complex $X$ homotopy equivalent to $M$ is obtained from the disjoint union of the $X_k$ (for all $k \geqslant 1$) under the identification of each $x \in Z_k$ with $w_k(x) \in X_{k+1}$. More precisely, $X$ is the mapping telescope (or infinite mapping cylinder) of the sequence

$$X_1 \supset Z_1 \xrightarrow{w_1} Y_2 \subset X_2 \supset Z_2 \xrightarrow{w_2} Y_3 \subset X_3 \supset \cdots$$

which is a CW-complex by construction. The homotopy equivalence $M \simeq X$ follows from the fact that each $u_k$ is a homotopy equivalence and the attaching maps $w_k$ are homotopic to the true identifications in $M$.

Since each $X_k$ has finitely many cells (namely, one $k$-cell for each critical point of index $k$ in $f^{-1}[a_{k-1}, a_k]$), and $M$ is compact, only finitely many $X_k$ are nonempty, so $X$ is a finite CW-complex.
