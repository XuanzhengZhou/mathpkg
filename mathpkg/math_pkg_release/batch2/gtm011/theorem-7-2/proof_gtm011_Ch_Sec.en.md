---
role: proof
locale: en
of_concept: theorem-7-2
source_book: gtm011
source_chapter: "Runge's Theorem"
source_section: ""
---

Proof. If $U \subset G$ is open, then we will have shown that $f(U)$ is open if we can show that for each $a$ in $U$ there is a $\delta > 0$ such that $B(\alpha; \delta) \subset f(U)$, where $\alpha = f(a)$. But only part of the strength of the

4. Suppose that $f: G \rightarrow \mathbb{C}$ is analytic and one-one; show that $f'(z) \neq 0$ for any $z$ in $G$.

5. Let $X$ and $\Omega$ be metric spaces and suppose that $f: X \rightarrow \Omega$ is one-one and onto. Show that $f$ is an open map iff $f$ is a closed map. (A function $f$ is a closed map if it takes closed sets onto closed sets.)

6. Let $P: \mathbb{C} \rightarrow \mathbb{R}$ be defined by $P(z) = \text{Re } z$; show that $P$ is an open map but is not a closed map. (Hint: Consider the set $F = \{z: \text{Im } z = (\text{Re } z)^{-1} \text{ and Re } z \neq 0\}$.)

7. Use Theorem 7.2 to give another proof of the Fundamental Theorem of Algebra.

§8. Goursat’s Theorem

Most modern books define an analytic function as one which is differentiable on an open set (not assuming the continuity of the derivative). In this section it is shown that this definition is the same as ours.

Goursat’s Theorem. Let $G$ be an open set and let $f: G \rightarrow \mathbb{C}$ be a differentiable function; then $f$ is analytic on $G$.

Proof. We need only show that $f'$ is continuous on each open disk contained in $G$; so, we may assume that $G$ is itself an open disk. It will be shown that $f$ is analytic by an application of Morera’s Theorem (5.10). That is, we must show that $\int_T f = 0$ for each triangular path $T$ in $G$.

Let $T = [a, b, c, a]$ and let $\Delta$ be the closed set formed by $T$ and its inside. Notice that $T = \partial \Delta$. Now using the midpoints of the sides of $\Delta$ form four triangles $\Delta_1, \Delta_2, \Delta_3, \Delta_4$ inside

Now perform the same process on $T^{(1)}$, getting a triangle $T^{(2)}$ with the analogous properties. By induction we get a sequence $\{T^{(n)}\}$ of closed triangular paths such that if $\Delta^{(n)}$ is the inside of $T^{(n)}$ along with $T^{(n)}$ then;

8.2 $\Delta^{(1)} \supset \Delta^{(2)} \supset \ldots$;

8.3 $\left| \int_{T^{(n)}} f \right| \leq 4 \left| \int_{T^{(n+1)}} f \right|$;

8.4 $\ell(T^{(n+1)}) = \frac{1}{2} \ell(T^{(n)})$;

8.5 diam $\Delta^{(n+1)} = \frac{1}{2}$ diam $\Delta^{(n)}$.

These equations imply:

8.6 $\left| \int_{T} f \right| \leq 4^n \left| \int_{T^{(n)}} f \right|$;

8.7 $\ell(T^{(n)}) = (\frac{1}{2})^n \ell$ where $\ell = \ell(T)$;

8.8 diam $\Delta^{(n)} = (\frac{1}{2})^n d$ where $d = \text{diam} \Delta$.

Since each $\Delta^{(n)}$ is closed, (8.2) and (8.8) allow us to apply Cantor's Theorem (II.3.7), and get that $\bigcap_{n=1}^{\infty} \Delta^{(n)}$ consists of a single point $z_0$.

Let $\epsilon > 0$; since $f$ has a derivative at $z_0$ we can find a $\delta > 0$ such that $B(z_0; \delta) \subset G$ and

$$\left| \frac{f(z) - f(z_0)}{z - z_0} - f'(z_0) \right| < \epsilon$$

whenever $0 < |z - z_0| < \delta$. Alternately,

8.9 $|f(z) - f(z_0) - f'(z_0)(z - z_0)| \

But using (8.6) this gives

$$\left| \int_T f \right| \leq 4^n \epsilon d\ell \left( \frac{1}{4} \right)^n = \epsilon d\ell.$$

Since $\epsilon$ was arbitrary and $d$ and $\ell$ are fixed, $\int_T f = 0$.

Chapter V

Singularities

In this chapter functions which are analytic in a punctured disk (an open disk with the center removed) are examined. From information about the behavior of the function near the center of the disk, a number of interesting and useful results will be derived. In particular, we will use these results to evaluate certain definite integrals over the real line which cannot be evaluated by the methods of calculus.

§1. Classification of singularities

This section begins by studying the best behaved singularity—the removable kind.
