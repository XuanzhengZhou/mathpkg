---
role: proof
locale: en
of_concept: ordinal-product-not-normal
source_book: gtm027
source_chapter: "4"
source_section: "E. Problems (Ordinal Space Properties)"
---

# Proof: The Product $\Omega_0 \times \Omega'$ is Not Normal

**Statement (e)**: The product $\Omega_0 \times \Omega'$ is not normal. (Here $\Omega_0 = [0, \Omega)$ with the order topology, and $\Omega' = [0, \Omega]$.)

**Proof** (following Kelley's hint):

Define two subsets of $\Omega_0 \times \Omega'$:
- $A = \{(x, x) : x \in \Omega_0\}$, the diagonal (restricted to $\Omega_0$).
- $B = \Omega_0 \times \{\Omega\}$, the "top edge" of the product.

Both $A$ and $B$ are closed in $\Omega_0 \times \Omega'$:
- $A$ is the graph of the identity function on $\Omega_0$, which is continuous, hence its graph is closed (in a Hausdorff space).
- $B = \Omega_0 \times \{\Omega\}$ is closed because $\{\Omega\}$ is closed in $\Omega'$ (it is the maximum point) and the product of closed sets in a product of $T_1$ spaces is closed.

Moreover, $A \cap B = \varnothing$, since $(x, x)$ for $x \in \Omega_0$ has second coordinate $x < \Omega$, while points of $B$ have second coordinate $\Omega$.

We prove that $A$ and $B$ cannot be separated by disjoint open sets. Suppose, for contradiction, that $U$ is an open neighborhood of $A$.

For each $x \in \Omega_0$, since $(x, x) \in A \subset U$, there exist neighborhoods: an open interval $I_x$ in $\Omega_0$ containing $x$ and an open interval $J_x$ in $\Omega'$ containing $x$, such that $I_x \times J_x \subset U$.

Define a function $f: \Omega_0 \to \Omega_0$ as follows: for each $x \in \Omega_0$, let $f(x)$ be the smallest ordinal larger than $x$ such that $(x, f(x)) \notin U$. (Such an ordinal exists because otherwise $(x, y) \in U$ for all $y > x$, including $y = \Omega$, which would put $(x, \Omega) \in B \cap U$, contradicting that $U$ should separate $A$ from $B$.)

By construction, $f(x) \geq x$ for all $x \in \Omega_0$. Then by part (d), there exists $\xi \in \Omega_0$ such that $(\xi, \xi)$ is an accumulation point of the graph of $f$.

Now consider the definition of $f(\xi)$. Since $(\xi, \xi) \in A \subset U$, and $U$ is open, there is a basic open neighborhood $W \times V$ of $(\xi, \xi)$ contained in $U$. Because $(\xi, \xi)$ is an accumulation point of the graph of $f$, there exist $x$ arbitrarily close to $\xi$ such that $(x, f(x))$ is in $W \times V$.

But by definition of $f(x)$, the point $(x, f(x))$ is not in $U$. Since $W \times V \subset U$, this is a contradiction.

Thus no open set $U$ containing $A$ can avoid intersecting every open set containing $B$ (in fact, any $U$ containing $A$ must intersect $B$ at limit points). Hence $\Omega_0 \times \Omega'$ is not normal.
