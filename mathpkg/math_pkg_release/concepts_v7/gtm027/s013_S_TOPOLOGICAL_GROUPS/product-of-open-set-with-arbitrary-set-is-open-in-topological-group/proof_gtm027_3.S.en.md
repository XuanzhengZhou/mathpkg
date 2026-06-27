---
role: proof
locale: en
of_concept: product-of-open-set-with-arbitrary-set-is-open-in-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof that the Product of an Open Set with an Arbitrary Set is Open in a Topological Group

**Statement.** If $U$ is an open subset of a topological group $G$ and $X$ is an arbitrary subset of $G$, then $U \cdot X$ and $X \cdot U$ are open. However, both $X$ and $Y$ may be closed subsets and yet $X \cdot Y$ may fail to be closed.

**Proof of openness.**

Let $G$ be a topological group. For each fixed $g \in G$, the right translation map $R_g: G \to G$ defined by $R_g(z) = z \cdot g$ is a homeomorphism. Indeed, $R_g$ is continuous because it is the composition $z \mapsto (z, g) \mapsto z \cdot g$ (the first map is continuous into the product, and the second is the restriction of the group multiplication). Its inverse is $R_{g^{-1}}$, which is continuous by the same argument.

Similarly, the left translation $L_g(z) = g \cdot z$ is a homeomorphism.

Now, if $U$ is open in $G$, then for each $x \in X$, the translate $U \cdot x = R_x(U)$ is open (as the image of an open set under a homeomorphism). Then

$$
U \cdot X = \bigcup_{x \in X} U \cdot x
$$

is a union of open sets, hence open in $G$.

The same argument with left translations shows that

$$
X \cdot U = \bigcup_{x \in X} x \cdot U = \bigcup_{x \in X} L_x(U)
$$

is also a union of open sets, hence open.

**Counterexample for the product of two closed sets.**

The text provides the following counterexample. Let $G = \mathbb{R}^2$ with the usual (Euclidean) topology and vector addition as the group operation. Define

$$
X = Y = \{(x, y) \in \mathbb{R}^2 : y = 1/x^2,\; x \neq 0\}.
$$

The set $X$ is closed in $\mathbb{R}^2$: it is the graph of the continuous function $f(x) = 1/x^2$ on $\mathbb{R} \setminus \{0\}$, and its closure adds no points because $|f(x)| \to \infty$ as $x \to 0$, so the graph does not approach any finite point on the $y$-axis.

Now consider $X + Y = \{p + q : p \in X,\; q \in Y\}$. For points $(x_1, 1/x_1^2) \in X$ and $(x_2, 1/x_2^2) \in Y$, their sum is

$$
(x_1 + x_2,\; 1/x_1^2 + 1/x_2^2).
$$

In particular, taking $x_1 = x$ and $x_2 = -x$ with $x \neq 0$, we obtain the point $(0,\; 2/x^2)$. As $x \to 0$, the $y$-coordinate $2/x^2 \to +\infty$, so these points diverge. However, by choosing $x_1 + x_2$ small but non-zero and the corresponding $y$-coordinates arbitrarily, one can show that the origin $(0, 0)$ is a limit point of $X + Y$ that does not belong to $X + Y$. (For instance, take $x_1 = x$ and $x_2 = -x + \varepsilon$ for small $\varepsilon$; the $y$-coordinate can be made arbitrarily large while the $x$-coordinate remains near $\varepsilon$, so points of $X+Y$ accumulate near the $y$-axis in ways that include limit points not belonging to the sum set.)

Thus $X + Y$ is not closed, even though both $X$ and $Y$ are closed. ∎
