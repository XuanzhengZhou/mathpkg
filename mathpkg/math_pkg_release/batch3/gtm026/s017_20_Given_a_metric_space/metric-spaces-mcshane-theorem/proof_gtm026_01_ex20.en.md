---
role: proof
locale: en
of_concept: metric-spaces-mcshane-theorem
source_book: gtm026
source_chapter: "1"
source_section: "Exercise 20"
---

Following the hint in Manes, define the extension $g: X \to \mathbb{R}$ by
$$g(x) = \sup\{\, f(a) - d(x, a) : a \in A \,\}.$$

**Step 1: $g$ extends $f$.** Let $x \in A$. For $a = x$ we have $f(x) - d(x, x) = f(x)$, so $g(x) \geq f(x)$. Conversely, for any $a \in A$, since $f$ is distance decreasing,
$$f(a) - f(x) \leq |f(a) - f(x)| \leq d(a, x) = d(x, a),$$
hence $f(a) - d(x, a) \leq f(x)$. Taking the supremum over $a \in A$ yields $g(x) \leq f(x)$. Therefore $g(x) = f(x)$ for all $x \in A$.

**Step 2: $g$ is distance decreasing.** Let $x, y \in X$. For any $a \in A$, the triangle inequality gives
$$f(a) - d(x, a) \leq f(a) - d(y, a) + d(x, y).$$
Taking the supremum over $a \in A$ on the left-hand side yields
$$g(x) \leq g(y) + d(x, y).$$
Thus $g(x) - g(y) \leq d(x, y)$. By symmetry in $x$ and $y$, we also have $g(y) - g(x) \leq d(x, y)$. Combining these gives
$$|g(x) - g(y)| \leq d(x, y).$$

Therefore $g$ is a distance-decreasing extension of $f$ to the whole space $X$, proving that $\mathbb{R}$ is injective in the category of metric spaces.
