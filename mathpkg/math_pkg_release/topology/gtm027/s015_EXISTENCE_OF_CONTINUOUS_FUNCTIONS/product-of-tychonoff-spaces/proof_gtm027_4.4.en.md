---
role: proof
locale: en
of_concept: product-of-tychonoff-spaces
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Product of Tychonoff Spaces is Tychonoff

**Theorem 6.** The product of Tychonoff spaces is a Tychonoff space.

*Proof.* A topological space is completely regular if for each point $x$ and each neighborhood $U$ of $x$ there is a continuous function $f$ to $[0,1]$ such that $f(x) = 0$ and $f$ is identically one on $X \sim U$. Equivalently, for each pair $(x, U)$ with $x \in U$, there exists a function $f$ such that $f(x) = 0$ and $f = 1$ on $X \sim U$.

Let $X = \prod \{X_a : a \in A\}$ be a product of Tychonoff spaces and let $x \in X$, $U$ a neighborhood of $x$. There exists a basic neighborhood $\bigcap_{i=1}^n P_{a_i}^{-1}[U_{a_i}] \subset U$ where each $U_{a_i}$ is a neighborhood of $x_{a_i}$ in $X_{a_i}$. Since each $X_{a_i}$ is completely regular, for each $i$ there is a continuous function $f_i : X_{a_i} \to [0,1]$ such that $f_i(x_{a_i}) = 0$ and $f_i = 1$ on $X_{a_i} \sim U_{a_i}$. Define $g(x) = \sup \{f_i \circ P_{a_i}(x) : i = 1, \ldots, n\}$. Then $g(x) = 0$, $g = 1$ on $X \sim \bigcap_i P_{a_i}^{-1}[U_{a_i}] \supset X \sim U$, and $g$ is continuous (as the supremum of finitely many continuous functions). Hence $X$ is completely regular.

Since the product of $T_1$-spaces is $T_1$, $X$ is a Tychonoff space.

