---
role: proof
locale: en
of_concept: proposition-14-15
source_book: gtm055
source_chapter: "15"
source_section: "Section 16_Section_16"
---

Proof. Let $V$ be a convex open neighborhood of $x_0$ that does not meet $C$. Then, as was seen in the proof of Proposition 14.14, there exists a continuous nonzero real linear functional $f$ on $\mathcal{E}$ such that $f(u) \leq f(v)$ whenever $u \in C$ and $v \in V$. If we set $c = \sup\{f(u) : u \in C\}$, and if $g$ is the complex linear functional on $\mathcal{E}$ such that $\text{Re } g = f$ (see the proof of Theorem 14.3), then $g$ is continuous along with $f$, and the inequality $\text{Re } g(x) \leq c$ holds for all vectors $x$ in $C$. To complete the proof we note that $f(V)$ is an open set in $\mathbb{R}$. (This can be seen in many ways. The simplest way is to fix a vector $z_0$ such that $f(z_0) \neq 0$, and to choose for each vector $v$ in $V$ a positive number $\delta = \delta_v$ such that $v + tz_0 \in V$ for all $-\delta < t < +\delta$. Then $f(V)$ contains the interval $\{f(v) + tf(z_0) : -\delta < t < +\delta\}$ about $f(v)$.) Hence if $V$ contained any vector $v$ such that $f(v) = c$, then $V$ would also have to contain vectors $v

Example N. If $0 < p < 1$ the linear space $(\ell_p)$ (Ex. 11D) is not (in any natural way) a normed space (cf. Example 11C), but

$$|x| = \sum_{n=0}^{\infty} |\xi_n|^p, \quad x = \{\xi_n\}_{n=0}^{\infty} \in (\ell_p),$$

(18)

defines a useful quasinorm on $(\ell_p)$ (see Problem U). If $\varepsilon$ is a positive number, then the ball $(\ell_p)_\varepsilon = \{x \in (\ell_p) : |x| \leq \varepsilon\}$ contains all of the vectors $\varepsilon e_m$, $m \in \mathbb{N}_0$ (where $e_m$ denotes the sequence $\{\delta_{mn}\}_{n=0}^{\infty}$ as usual; cf. Example 11H). Since $x_n = \varepsilon(e_0 + \cdots + e_{n-1})/n$ is a convex combination of the vectors $\varepsilon e_0, \ldots, \varepsilon e_{n-1}$, and since $|x_n| = \varepsilon^p/n^{p-1}$ for each nonnegative integer $n$, we see that the convex hull of $(\ell_p)_\varepsilon$ is not contained in any ball $(\ell_p)_r, r > 0$. Hence no bounded neighborhood of the origin 0 in $(\ell_p)$ contains a convex neighborhood of 0, so the space $(\ell_p)$ equipped with the quasinorm (18) is certainly not locally convex. Nevertheless the linear functionals $\{\xi_n\}_{n=0}^{\infty} \to \xi_m$ are all continuous on $(\ell_p)$ with respect to the quasinorm (18), and this family of linear functionals is separating on $(\ell_p)$. Thus the collection $\mathcal{E}^*$ of continuous linear functionals on a topological linear space $\mathcal{E}$ may be separating even when $\mathcal{E}$ is not locally convex.

Problems

A. Let $M$ denote the linear submanifold of $\mathbb{C}^

of the full algebraic direct sum of the family $\mathcal{E}_{\gamma}$ such that $\sum_{\gamma} \| x_{\gamma} \|^p < +\infty$, equipped with the norm

$$\| \{x_{\gamma}\} \|_p = \left[ \sum_{\gamma} \| x_{\gamma} \|^p \right]^{1/p}$$

(see Problem 11T). Find the dual space $\mathcal{K}_p^*$.

E. Prove the converse of Proposition 12.2 by showing that if $\mathcal{E}$ and $\mathcal{F}$ are normed spaces with $\mathcal{E} \neq (0)$, and if $\mathcal{L}(\mathcal{E}, \mathcal{F})$ is complete, then $\mathcal{F}$ is also complete.

F. Let $[a, b]$ be a real interval, $a \leq b$, and let $\mathcal{V} = \mathcal{V}([a, b])$ denote the collection of all complex-valued functions $\alpha$ of bounded variation on $[a, b]$. Then $\mathcal{V}$ is a linear space and $V(\alpha) = V(\alpha; a, b)$ (the total variation of $\alpha$ over $[a, b]$) defines a pseudo-norm on $\mathcal{V}$. Show that the zero space $\mathcal{Z}$ of $V$ is the one-dimensional space consisting of the constant functions, and verify that the associated space $\dot{\mathcal{V}}$ is complete in the norm obtained by factoring out $\mathcal{Z}$ (Prop. 11.17). (Thus the elements of the Banach space $\dot{\mathcal{V}}$ are really equivalence classes of functions differing by additive constants. Nevertheless it is customary to refer to them as functions, to write $\mathcal{V}([a, b])$ for $\dot{\mathcal{V}}$, and also to refer to $V$ as the total variation norm on $\mathcal{V}$. It should be noted that the ambiguity thus introduced places on the reader the rather trivial burden of determining, in some situations, just which meaning to assign to the symbol $\mathcal{V}$.) Show also that the mapping that assigns to each $\alpha$ in $\dot{\mathcal

H. Suppose $x = \{\xi_n\}_{n=0}^{\infty}$ is an ultimately periodic sequence of complex numbers, i.e., suppose there exist complex numbers $\alpha_1, \ldots, \alpha_p$ and a positive integer $N$ such that $\xi_n = \alpha_i$ whenever $n$ is congruent to $i$ modulo $p$ and $n > N$, and let $\varphi$ be an arbitrary Banach generalized limit (Ex. E). Show that $\varphi(x) = (\alpha_1 + \cdots + \alpha_p)/p$.

I. For an arbitrary infinite sequence $x = \{\xi_n\}_{n=0}^{\infty}$ of complex numbers let us write $Cx = \{\eta_n\}_{n=0}^{\infty}$, where

$$\eta_n = \frac{\xi_0 + \cdots + \xi_n}{n+1}, \quad n \in \mathbb{N}_0.$$

The sequence $x$ is said to be limitable (in the sense of) Cesàro to $\lambda_0$ (notation: $C$-lim $x = \lambda_0$) if the sequence $Cx$ is convergent and lim $Cx = \lambda_0$. Show that the collection $\mathcal{L}$ of all bounded sequences $x$ that are limitable Cesàro forms a subspace of $(\ell_\infty)$, and that $\varphi(x) = C$-lim $x$ is a bounded linear functional on $\mathcal{L}$. Show also that $\varphi$ may be extended to a Banach generalized limit on $(\ell_\infty)$. (Hint: Show first that $C$ acts as a contraction on $(\ell_\infty)$, and hence that $\varphi$ has norm one. Verify that if $x = \{\xi_n\}$ is limitable Cesàro, and if $x_m$ denotes the tail $\{\xi_m, \xi_{m+1}, \ldots\}$ of $x$, then $C$-lim $x_m = C$-lim $x$. Conclude that $(c) \subset \mathcal{L}$, that $\varphi$ extends the functional lim on $(c)$, and that $\varphi$ has norm one with respect to the pseudonorm $\sigma$ introduced in Example E.)

K. (i) Let $\varphi$ be an arbitrary linear functional on $(\ell_\infty)$ that takes the value one at the constant sequence $e = \{1, 1, \ldots\}$. Show that $\varphi$ is a positive linear functional when and only when $\|\varphi\| = 1$. (Hint: Show that if $\|\varphi\| = 1$ and if $x$ is a sequence in $(\ell_\infty)$ all of whose terms lie in some closed disc $D^-$ in $\mathbb{C}$, then $\varphi(x) \in D^-$; use this fact to conclude that $\text{Re} \varphi(x) \geq 0$ whenever $\text{Re} x \geq 0$.) (ii) Let $\varphi$ be a Banach generalized limit on $(\ell_\infty)$ as defined in Example E. Show that $\varphi$ is the complexification of its restriction to $(\ell_\infty)_{\mathbb{R}}$ (Ex. 2M), and that if $\varphi_0$ denotes the restriction of $\varphi$ to $(\ell_\infty)_{\mathbb{R}}$, then $\varphi_0$ satisfies condition (13). Show conversely that if $\varphi_0$ is any linear functional on $(\ell_\infty)_{\mathbb{R}}$ satisfying (13), then the complexification of $\varphi_0$ has norm one with respect to the pseudonorm $\sigma$ of Example E, and is therefore a Banach generalized limit. (In other words, the real generalized limits generated by the procedure set forth in Problem J are precisely the restrictions to $(\ell_\infty)_{\mathbb{R}}$ of the Banach generalized limits of Example E.)

L. The function $p_0$ introduced in Problem J has a number of interesting properties.

(i) Verify first that if $x = \{\xi_n\}$, then

$$-p_0(-x) = \sup \inf_{n} \left\{ \frac{1}{M} \sum_{i=1}^{M} \xi_{m_i+n} \right\} = \sup \liminf_{n} \left\{ \frac{1}{M} \sum_{i=1}^{M} \xi_{m_i+n} \right\},$$

where the supremum

M. Show that there exist linear functionals $\varphi$ on the real Banach space $\mathcal{B}_{\mathbb{R}}([0, +\infty))$ of all bounded real functions on the half-line $[0, +\infty)$ satisfying the following conditions for every $f$ in $\mathcal{B}_{\mathbb{R}}([0, +\infty))$:

(i) If $\lim f(t)$ exists, then $\varphi(f) = \lim f(t)$,
(ii) If $f \geq 0$, then $\varphi(f) \geq 0$,
(iii) If we write $f_s(t) = f(s + t)$, then $\varphi(f_s) = \varphi(f)$ for all $s \geq 0$.

Show also that if $\varphi$ is any such functional, then

(iv) $\lim \inf f(t) \leq \varphi(f) \leq \lim \sup f(t)$ for every $f$ in $\mathcal{B}_{\mathbb{R}}([0, +\infty))$, and
(v) $\|\varphi\| = 1$.

N. (i) Show that if a subset $A$ of a topological linear space $\mathcal{E}$ is [absolutely] convex, then $A^-$ and $A^+$ are also [absolutely] convex. (Hint: If $x, y \in \mathcal{E}$ and $V$ is a neighborhood of 0, and if $0 \leq t \leq 1$, then $t(x + V) + (1 - t)(y + V) = (tx + (1 - t)y) + (tV + (1 - t)V)$; recall Problem 11M.) Show also that a subset $A$ of $\mathcal{E}$ is absolutely convex if and only if $x, y \in A$ and $|\alpha| + |\beta| \leq 1$ imply that $\alpha x + \beta y \in A$. (It is this characterization that led to the term "absolutely convex".) Verify that an arbitrary subset $M$ of $\mathcal{E}$ is contained in a smallest absolutely convex set $A$, and that this set, known as the absolutely convex hull of $M$, consists of the collection of all linear combinations

Q. Let $\Delta$ be a domain in the complex plane, and let $A$ denote the space of all analytic functions on $\Delta$. Show that $A$ is a Frechét space in the topology of uniform convergence on compact subsets of $\Delta$. (Hint: See Problem 11U.)

R. Show that if $\mathcal{E}$ is a normed space such that $\mathcal{E}^*$ is separable, then $\mathcal{E}$ itself is separable. (Hint: Let $\{f_n\}$ be a countable dense subset of $\mathcal{E}^*$ and for each $n$ let $x_n$ be a unit vector in $\mathcal{E}$ such that $f_n(x_n) > \|f_n\|/2$. Use Proposition 14.10 to show that the countable set $\{x_n\}$ spans $\mathcal{E}$; then use Problem 11K.) Show by an example that the separability of $\mathcal{E}$ does not imply that of $\mathcal{E}^*$.

S. Let $C$ be a convex subset of a real linear space $\mathcal{E}$. A subset $D$ of $C$ is called an extreme subset of $C$ if, for every line segment $\sigma$ in $C$ such that $\sigma \cap D \neq \emptyset$, either $\sigma \subset D$ or else $\sigma \cap D$ is a singleton consisting of an endpoint of $\sigma$. A point $x_0$ such that the singleton $\{x_0\}$ is an extreme subset of $C$ is called an extreme point of $C$.

(i) Let $C$ be a convex set in a real linear space $\mathcal{E}$, let $f$ be a (real) linear functional on $\mathcal{E}$, and suppose $f$ is bounded above on $C$. Show that the set

$$D = \left\{x \in C : f(x) = \sup_{y \in C} f(y)\right\}$$

is an extreme subset of $C$.

(ii) Show that an extreme subset $D$ of a convex set $C$ has the property that both $D$ and $C \setminus D$ are convex sets. Show also that if

sequences (Ex. 11H) is dense in $(\ell_p)$ with respect to this quasinorm, and use this fact to verify that every continuous linear functional on $(\ell_p)$, $0 < p < 1$, is of the form

$$f_a(x) = \sum_{n=0}^{\infty} \alpha_n \xi_n, \quad x = \{\xi_n\}_{n=0}^{\infty} \in (\ell_p),$$

where $a = \{\alpha_n\}_{n=0}^{\infty}$ is a bounded sequence of complex numbers. Show, finally, in the converse direction, that if $\{\alpha_n\} \in (\ell_\infty)$, then $f(x) = \sum_{n=0}^{\infty} \alpha_n \xi_n$ defines a continuous linear functional on $(\ell_p)$, $0 < p < 1$. (Hint: If $|x|_p \leq 1$, then $\|x\|_1 \leq |x|_p$.)

The following two problems are concerned with yet another version of the Hahn–Banach theorem, valid in the context of partially ordered linear spaces.

V. If $\mathcal{E}$ is a real linear space that is equipped with a partial ordering $\leq$, then $\mathcal{E}$ is said to be a partially ordered linear space if the following conditions are satisfied: (1) if $x \leq y$ in $\mathcal{E}$ then $x + z \leq y + z$ for every $z$ in $\mathcal{E}$, and (2) if $x \leq y$ and if $t$ is a nonnegative real number, then $tx \leq ty$.

(i) Show that if $\mathcal{E}$ is a partially ordered linear space, then the set $P$ of positive elements of $\mathcal{E}$, that is, elements $x$ of $\mathcal{E}$ such that $x \geq 0$, is a convex subset of $\mathcal{E}$ with the property that if $x \in P$ and $t$ is a nonnegative real number then $tx \in P$. (Such a convex set is called a convex cone.) Show conversely that if $P$ is a convex cone in an arbitrary real linear space $\mathcal{E}$, and if we

Local convexity and weak topologies 15

Along with its norm topology every normed space possesses a second topology of great importance known as its weak topology.
