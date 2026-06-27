---
role: proof
locale: en
of_concept: causal-character-via-orthogonal-complement
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

**Proof of (a).** Suppose $W$ is timelike. Then $W$ contains a timelike vector $w$. There exists an orthonormal basis $\{e_1, \ldots, e_{N-1}, w\}$ with $g(e_i, e_i) > 0$ and $g(w, w) < 0$. Since $W^\perp \subset \operatorname{span}\{e_i \mid i = 1, \ldots, N-1\}$ and $g$ is positive definite on this span, $W^\perp$ is spacelike.

Conversely, suppose $W^\perp$ is spacelike. Then $V = W \oplus W^\perp$ (since $W^\perp$ is spacelike, it has trivial intersection with $W$ and $g$ is non-degenerate). Let $v \in V$ be timelike; then $v = w + \hat{w}$ for some $w \in W$, $\hat{w} \in W^\perp$. We have
$$g(w, w) = g(v, v) - g(\hat{w}, \hat{w}) < 0$$
since $g(v, v) < 0$ and $g(\hat{w}, \hat{w}) \geq 0$. Thus $w$ is timelike and hence $W$ is timelike.

The dual statement ($W$ spacelike iff $W^\perp$ timelike) follows from $W^{\perp\perp} = W$.

**Proof of (b).** Suppose $W$ is lightlike. Then $W$ contains a lightlike vector $w_0$, but no timelike vector. For all $a \in \mathbb{R}$ and all $w \in W$,
$$g(w + a w_0, w + a w_0) = g(w, w) + 2a\,g(w, w_0) \geq 0.$$
Since $a$ was arbitrary, we must have $g(w, w_0) = 0$ for all $w \in W$. Hence $w_0 \in W^\perp$, so $W \cap W^\perp \neq \{0\}$, and $W$ contains no timelike vector by definition of lightlike.

Conversely, suppose $0 \neq w_0 \in W \cap W^\perp$ and $W$ contains no timelike vector. Then $g(w_0, w_0) = 0$, so $w_0$ is lightlike. Since $W$ cannot contain a timelike vector by hypothesis and contains the lightlike vector $w_0$, $W$ is lightlike by the definition and Example 1.1.2(b).

The dual statement ($W$ lightlike iff $W^\perp$ lightlike) follows from $W^{\perp\perp} = W$.
