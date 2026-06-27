---
role: proof
locale: en
of_concept: homomorphism-preserves-lattice-structure
source_book: gtm043
source_chapter: "1"
source_section: "1.6"
---

Let $t : C(Y) \to C(X)$ (or $t : C^*(Y) \to C(X)$) be a ring homomorphism.

**Step 1: $t$ is order-preserving.** If $g \geq 0$, then $g = l^2$ for some $l$ in the domain (since the domain consists of real-valued functions and nonnegative functions are squares). Then $tg = t(l^2) = (tl)^2$, so $tg$ is a square, hence $tg \geq 0$. Thus $t$ sends nonnegative functions to nonnegative functions. If $g \geq h$, then $g - h \geq 0$, so $tg - th = t(g - h) \geq 0$, i.e., $tg \geq th$. Hence $t$ is order-preserving.

**Step 2: $t$ preserves absolute values.** We have
$$(t|g|)^2 = t(|g|^2) = t(g^2) = (tg)^2.$$
Since $|g| \geq 0$, we have $t|g| \geq 0$ by Step 1. The function $|tg|$ is also nonnegative and satisfies $(|tg|)^2 = (tg)^2$. Since nonnegative square roots in $C(X)$ are unique, we conclude $t|g| = |tg|$.

**Step 3: $t$ preserves the join.** Using the identity
$$(g \vee h) + (g \vee h) = g + h + |g - h|,$$
we apply $t$ to both sides:
\begin{align*}
t(g \vee h) + t(g \vee h) &= t(g) + t(h) + t|g - h| \\
&= tg + th + |tg - th| && \text{(by Step 2)} \\
&= (tg \vee th) + (tg \vee th).
\end{align*}
Since $t(g \vee h)$ and $tg \vee th$ are real-valued functions on $X$, the equality $2 \cdot t(g \vee h) = 2 \cdot (tg \vee th)$ implies $t(g \vee h) = tg \vee th$.

**Step 4: $t$ preserves the meet.** Dually, $g \wedge h = -((-g) \vee (-h))$, so $t(g \wedge h) = tg \wedge th$ follows from the join-preservation.
