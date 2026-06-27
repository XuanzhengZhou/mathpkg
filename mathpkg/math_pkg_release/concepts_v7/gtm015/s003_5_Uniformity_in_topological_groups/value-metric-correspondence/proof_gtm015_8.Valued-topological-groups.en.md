---
role: proof
locale: en
of_concept: value-metric-correspondence
source_book: gtm015
source_chapter: "8"
source_section: "Valued topological groups"
---

# Proof of One-to-one correspondence between values and left-invariant metrics

Let $(G, |\cdot|)$ be a valued group, and define $d(x, y) = |x^{-1}y|$ for all $x, y \in G$. We verify that $d$ is a left-invariant metric on $G$.

**Positivity:** If $x \neq y$, then $x^{-1}y \neq e$, so $d(x, y) = |x^{-1}y| > 0$ by axiom (ii) of a value. For any $x$, $d(x, x) = |x^{-1}x| = |e| = 0$ by axiom (i).

**Symmetry:** $d(y, x) = |y^{-1}x| = |(y^{-1}x)^{-1}| = |x^{-1}y| = d(x, y)$, using axiom (iii) of a value.

**Triangle inequality:**
$$d(x, y) = |x^{-1}y| = |(x^{-1}z)(z^{-1}y)| \leq |x^{-1}z| + |z^{-1}y| = d(x, z) + d(z, y),$$
using axiom (iv) of a value.

**Left-invariance:**
$$d(ax, ay) = |(ax)^{-1}(ay)| = |x^{-1}a^{-1}ay| = |x^{-1}y| = d(x, y).$$

Thus $d$ is a left-invariant metric. Conversely, the value is recovered from the metric by $|x| = d(e, x)$, since $d(e, x) = |e^{-1}x| = |x|$.

This establishes a one-to-one correspondence: given a left-invariant metric $d$, defining $|x| = d(e, x)$ yields a value, and given a value $|\cdot|$, defining $d(x, y) = |x^{-1}y|$ yields a left-invariant metric; the two constructions are mutually inverse.
