---
role: exercise
locale: en
chapter: "III"
section: "7"
exercise_number: 1
---

Let $X$ be a projective nonsingular variety of dimension $n$ over an algebraically closed field $k$. For a closed subscheme $Y \subseteq X$ of pure codimension $p$, define the cohomology class $\eta(Y) \in H^p(X, \Omega_X^p)$ as follows: Use the trace map $t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k$ and the isomorphism of (7.13) to obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$, which corresponds to $\eta(Y) \in H^p(X, \Omega_X^p)$.

(a) If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

(b) If $X = \mathbf{P}^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is its degree as a projective variety (I, \S7). [Hint: Cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case $Y$ is a finite set of points.]

(c) For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mathcal{O}_X^* \to \Omega_X$ by $d\log(f) = f^{-1}df$. Here $\mathcal{O}^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology $\operatorname{Pic} X = H^1(X, \mathcal{O}_X^*) \to H^1(X, \Omega_X)$ which we denote by $c$ — see (Ex. 4.5).

(d) Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mathcal{L}(Y))$, where $\mathcal{L}(Y)$ is the invertible sheaf corresponding to the divisor $Y$.

See Matsumura [1] for further discussion.
