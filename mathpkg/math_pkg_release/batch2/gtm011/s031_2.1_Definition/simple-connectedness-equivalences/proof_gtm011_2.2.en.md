---
role: proof
locale: en
of_concept: simple-connectedness-equivalences
source_book: gtm011
source_chapter: "VIII"
source_section: "2.2"
---

**Proof.** The implications are proved in the following order.

**(a) \(\Rightarrow\) (b):** If \(\gamma\) is a closed rectifiable curve in \(G\) and \(a\) is a point in the complement of \(G\), then \(n(\gamma; a) = \frac{1}{2\pi i} \int_\gamma (z-a)^{-1}\,dz\). The function \((z-a)^{-1}\) is analytic in \(G\), and part (b) follows by Cauchy's Theorem.

**(b) \(\Rightarrow\) (c):** Suppose \(\mathbb{C}_{\infty} - G\) is not connected; then \(\mathbb{C}_{\infty} - G = A \cup B\) where \(A\) and \(B\) are disjoint, non-empty, closed subsets of \(\mathbb{C}_{\infty}\). Since \(\infty\) must be either in \(A\) or in \(B\), suppose that \(\infty\) is in \(B\); thus, \(A\) must be a compact subset of \(\mathbb{C}\) (\(A\) is compact in \(\mathbb{C}_{\infty}\) and does not contain \(\infty\)). But then \(G_1 = G \cup A = \mathbb{C}_{\infty} - B\) is an open set in \(\mathbb{C}\) and contains \(A\). According to Proposition 1.1 there are a finite number of polygons \(\gamma_1, \ldots, \gamma_m\) in \(G_1 - A = G\) such that for every analytic function \(f\) on \(G_1\),

\[
f(z) = \sum_{k=1}^{m} \frac{1}{2\pi i} \int_{\gamma_k} \frac{f(w)}{w-z}\,dw
\]

for all \(z\) in \(A\). In particular, if \(f(z) \equiv 1\) then

\[
1 = \sum_{k=1}^{m} n(\gamma_k; z)
\]

for all \(z\) in \(A\). Thus for any \(z\) in \(A\) there is at least one polygon \(\gamma_k\) in \(G\) such that \(n(\gamma_k; z) \neq 0\). This contradicts (b).

**(c) \(\Rightarrow\) (d):** See Corollary 1.15.

**(d) \(\Rightarrow\) (e):** Let \(\gamma\) be a closed rectifiable curve in \(G\), let \(f\) be an analytic function on \(G\), and let \(\{p_n\}\) be a sequence of polynomials such that \(f\) is approximated uniformly on compact sets. Then the restriction of this approximation to \(\{\gamma\}\) yields the desired uniform approximation.

**(e) \(\Rightarrow\) (f):** This follows by applying (e) to the function \((z-a)^{-1}\) for \(a \notin G\) along closed rectifiable curves.

**(f) \(\Rightarrow\) (g):** Standard argument using the fact that homology to zero gives path-independence for integrals of analytic functions, allowing construction of a primitive for \(f'/f\).

**(g) \(\Rightarrow\) (h):** If \(f\) never vanishes and has an analytic logarithm \(g\) (so that \(f = \exp(g)\)), then \(\exp(g/2)\) is an analytic square root of \(f\).

**(h) \(\Rightarrow\) (i):** See Theorem III.2.30 and the argument below.

**(i) \(\Rightarrow\) (j):** Since Theorem III.2.30 also applies to \(\mathbb{C}\), (j) follows from (h) together with the construction of a harmonic conjugate producing a homeomorphism onto \(D\).

**(j) \(\Rightarrow\) (g):** Suppose \(f: G \to \mathbb{C}\) is analytic and never vanishes, and let \(u = \operatorname{Re} f\), \(v = \operatorname{Im} f\). If \(U: G \to \mathbb{R}\) is defined by

\[
U(x, y) = \log |f(x + iy)| = \log\left[ u(x,y)^2 + v(x,y)^2 \right]^{\frac{1}{2}}
\]

then a computation shows that \(U\) is harmonic. Let \(V\) be a harmonic function on \(G\) such that \(g = U + iV\) is analytic on \(G\) and let \(h(z) = \exp g(z)\). Then \(h\) is analytic, never vanishes, and

\[
\left| \frac{f(z)}{h(z)} \right| = 1
\]

for all \(z\) in \(G\). That is, \(f/h\) is an analytic function whose range is not open. It follows that there is a constant \(c\) such that

\[
f(z) = c\,h(z) = c \exp g(z) = \exp[g(z) + c_1].
\]

Thus, \(g(z) + c_1\) is a branch of \(\log f(z)\).

**(j) \(\Rightarrow\) (i):** Let \(h: G \to D\) be a homeomorphism (where \(D\) is the open unit disk). If \(u: G \to \mathbb{R}\) is harmonic then \(u_1 = u \circ h^{-1}\) is a harmonic function on \(D\). By Theorem III.2.30 there is a harmonic function \(v_1: D \to \mathbb{R}\) such that \(f_1 = u_1 + i v_1\) is analytic on \(D\). Let \(f = f_1 \circ h\). Then \(f\) is analytic on \(G\) and \(u\) is the real part of \(f\). Thus \(v = \operatorname{Im} f = v_1 \circ h\) is the sought-after harmonic conjugate. Since Theorem III.2.30 also applies to \(\mathbb{C}\), (j) follows from (h).

This completes the proof of the theorem. This theorem constitutes an aesthetic peak in Mathematics. Notice that it says that a topological condition (simple connectedness) is equivalent to analytical conditions (e.g., the existence of harmonic conjugates and analytic logarithms).
