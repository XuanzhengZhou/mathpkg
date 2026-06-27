---
role: proof
locale: en
of_concept: separating-transcendence-basis-theorem
source_book: gtm028
source_chapter: "V"
source_section: "§4. Finiteness theorems"
---

If $n = d$, we take $y_j = x_j$ and there is nothing to prove. We proceed by induction on $n$, for $n > d$. Owing to the transitivity of integral dependence (§1, Theorem 2) and of separability (II, §5, Theorem 9) we have only to prove the following result (where, for simplicity of notation, $n$ has been changed into $n + 1$): if $k[x_1, \cdots, x_n, x_{n+1}]$ is a finite integral domain, of transcendence degree $d \leq n$, then there exist $n$ linear combinations $z_1, \cdots, z_n$ of the $x_i$ such that $k[x]$ is integral over $k[z]$ (and such that $k(x)$ is separable over $k(z)$ if $k(x)$ is separably generated over $k$). After eventual renumbering of the $x_i$ we may suppose that a transcendence basis of $k(x)$ over $k$ may be found among $\{x_1, \cdots, x_n\}$ (II, §12, Theorem 23, Corollary 2) and that this basis is a separating transcendence basis in the separable case (II, §13, Theorem 30). We then write $u = x_{n+1}$ and denote by $P(U, x_1, \cdots, x_n)$ the minimal polynomial of $u$ over $k(x_1, \cdots, x_n)$. We assume that the coefficients of $P(U, x_1, \cdots, x_n)$ are in $k[x_1, \cdots, x_n]$, so that $P(U, x_1, \cdots, x_n)$ is a polynomial in $U, x_1, \cdots, x_n$. By choosing suitable linear combinations $z_i = x_i + c_i u$ with generic constants $c_i \in k$ (requiring $k$ to be infinite, or passing to a transcendental extension), one ensures that after the change of variables, the ring becomes integral over a polynomial ring in $n$ variables. The induction hypothesis then applies.
