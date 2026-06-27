---
role: proof
locale: en
of_concept: subspace-causal-character-properties
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

(a) Suppose $W$ is timelike. Then there exists a timelike vector $w \in W$. Choose an orthonormal basis $\{e_1, \ldots, e_{N-1}, w\}$ with $g(e_i, e_i) = 1$ and $g(w, w) = -1$. Since $W^\perp \subset \operatorname{span}\{e_i \mid i = 1, \ldots, N-1\}$ and $g$ is positive definite on this span, $W^\perp$ is spacelike.

Conversely, suppose $W^\perp$ is spacelike. Then $V = W \oplus W^\perp$ (since $W^\perp$ is nondegenerate). Let $v \in V$ be timelike; decompose $v = w + \hat{w}$ with $w \in W$, $\hat{w} \in W^\perp$. Then
$$g(w, w) = g(v, v) - g(\hat{w}, \hat{w}) < 0$$
since $g(v, v) < 0$ and $g(\hat{w}, \hat{w}) \geq 0$. Thus $w$ is timelike, so $W$ is timelike.

(b) Suppose $W$ is lightlike. Then $W$ contains a lightlike vector $w_0 \neq 0$ but no timelike vector. For any $a \in \mathbb{R}$ and $w \in W$,
$$g(w + a w_0, w + a w_0) = g(w, w) + 2a\, g(w, w_0) \geq 0.$$
Since $a$ is arbitrary, we must have $g(w, w_0) = 0$ for all $w \in W$. Hence $w_0 \in W^\perp$, which implies $W \cap W^\perp \neq \{0\}$.

Conversely, if $0 \neq w_0 \in W \cap W^\perp$, then $g(w_0, w_0) = 0$, so $w_0$ is lightlike. Since $W$ cannot contain a timelike vector by part (a) (otherwise $W^\perp$ would be spacelike, contradicting $w_0 \in W \cap W^\perp$ with $w_0 \neq 0$), $W$ is lightlike.
