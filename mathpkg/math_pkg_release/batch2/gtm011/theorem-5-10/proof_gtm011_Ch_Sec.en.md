---
role: proof
locale: en
of_concept: theorem-5-10
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Suppose that $\sigma: [0, 1] \rightarrow \mathcal{S}(G)$ is a path with $\sigma(0) = (a, [f]_a), \sigma(

$C = \{(b, [g]_b) : [g]_b$ is the continuation of $[f]_a$ along some curve in $G$.

Proof. Suppose $C$ is a component of $S(G)$; by Corollary 5.9 $C$ is an open arcwise connected subset of $S(G)$. So by the preceding theorem, for each point $(b, [g]_b)$ in $C$, $[g]_b$ is the continuation of $[f]_a$ along some curve in $G$. Conversely, if $[g]_b$ is the continuation of $[f]_a$ along some curve in $G$ then $(b, [g]_b)$ belongs to the component of $S(G)$ which contains $(a, [f]_a)$; that is, $(b, [g]_b) \in C$.

Now suppose that $C$ consists of all points $(b, [g]_b)$ such that $[g]_b$ is a continuation of $[f]_a$. Then $C$ is arcwise connected and hence is connected. If $C_1$ is the component of $S(G)$ containing $C$ then by the first half of this proof it follows that $C = C_1$.

Notice that the point $(a, [f]_a)$ in the statement of the preceding theorem has a transitory role; any point in the component will do.

Fix a function element $(f, D)$ and recall that the complete analytic function $F$ associated with $(f, D)$ is the collection of all germs $[g]_z$ which are analytic continuations of $[f]_a$ for any $a$ in $D$ (see Definition 2.7). Let

5.12 $G = \{z : \text{there is a germ } [g]_z \text{ in } F\}$;

it follows that $G$ is open. In fact, if $z \in G$ then there is a germ $[g]_z$ in $F$ and a disk $B$ about $z$ on which $g$ is defined. Clearly $B \subset G$ so that $G$ is open.

some extra points—the branch points. These branch points correspond to singularities and permit a deeper analysis of the complete analytic function.

Exercises

1. Define $F: \mathcal{S}(\mathbb{C}) \to \mathbb{C}$ by $F(z, [f]_z) = f(z)$ and show that $F$ is continuous.
2. Let $\mathcal{F}$ be the complete analytic function obtained from the principal branch of the logarithm and let $G = \mathbb{C} - \{0\}$. If $D$ is an open subset of $G$ and $f: D \to \mathbb{C}$ is a branch of the logarithm show that $[f]_a \in \mathcal{F}$ for all $a$ in $D$. Conversely, if $(f, D)$ is a function element such that $[f]_a \in \mathcal{F}$ for some $a$ in $D$, show that $f: D \to \mathbb{C}$ is a branch of the logarithm. (Hint: Use Exercise 2.8.)
3. Let $G = \mathbb{C} - \{0\}$, let $\mathcal{F}$ be the complete analytic function obtained from the principal branch of the logarithm, and let $(\mathcal{R}, \rho)$ be the Riemann surface of $\mathcal{F}$ (so that $G$ is the base of $\mathcal{R}$). Show that $\mathcal{R}$ is homeomorphic to the graph $\Gamma = \{(z, e^z): z \in G\}$ considered as a subset of $\mathbb{C} \times \mathbb{C}$. (Use the map $h: \mathcal{R} \to \Gamma$ defined by $h(z, [f]_z) = (f(z), z)$ and use Exercise 2.) State and prove an analogous result for branches of $z^{1/n}$.
4. Consider the sheaf $\mathcal{S}(\mathbb{C})$, let $B = \{z: |z-1| < 1\}$, let $\ell$ be the principal branch of the logarithm defined on $B$, and let $\ell_1(z) = \ell(z) + 2\pi i
