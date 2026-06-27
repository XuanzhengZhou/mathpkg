---
role: proof
locale: en
of_concept: prop-for-subject-to-i-and-ii
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: Remember first of all that

$a(x) = \lim_{n \to \infty} [G_n(0,0) - G

$-b$ which does not go through the origin. Being precise, it states that whenever

$$P(b, x_1)P(x_1, x_2) \cdots P(x_n, -b) > 0$$

then at least one of the points $x_1, x_2, \ldots, x_n$ is the origin. A simple combinatorial argument settles the matter. There is a path of positive probability from any point to any other. Therefore there is a positive product of the type above, such that not all of the differences

$$x_1 - b, x_2 - x_1, \ldots, -b - x_n$$ are multiples of $b$ (parallel to the vector $b$). Call these differences $y_1, y_2, \ldots, y_{n+1}$ and reorder them so that the arguments $\arg(y_k)$ are in nondecreasing order. We can do this so that, calling the newly ordered set $z_1, z_2, \ldots, z_{n+1}$, we have $\arg b \leq \arg z_1 \leq \arg z_2 \leq \ldots \leq \arg z_{n+1} \leq \arg b + 2\pi$. Then we clearly have a path with probability (see diagram)

$$P(b, b + z_1)P(b + z_1, b + z_1 + z_2) \cdots P(b + \cdots + z_n, -b) > 0$$

which goes from $b$ to $-b$ without going through 0. That proves P7 by contradiction.

We are nearing our goal of expressing $H_B$, $\Pi_B$, and $\mu_B$ in terms of the function $a(x)$, for arbitrary finite sets $B$. Since this is a trivial matter when $|B| = 1$, but one which requires annoying modifications in the analysis, we assume from now on that $|B| \geq 2$. The key to the necessary calculations is the inversion of the operator $A(x,y)$, with $x$ and $y$ restricted to $B$. We shall say that the operator $A(x,y)$ restricted

to the set $B$ has an inverse if there exists a function $K_B(x,y)$, with $x$ and $y$ in $B$, such that
