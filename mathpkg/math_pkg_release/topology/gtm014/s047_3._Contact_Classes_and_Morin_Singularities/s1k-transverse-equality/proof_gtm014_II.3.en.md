---
role: proof
locale: en
of_concept: s1k-transverse-equality
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

We need only prove this locally. Let $p \in S_{1^k}(f)$. By choosing coordinates on $X$ based at $p$ and on $Y$ based at $f(p)$, we may assume that $p = f(p) = 0$ and that
$$
f(x_1, \ldots, x_n) = (h(x), x_2, \ldots, x_n)
$$
where $\partial^s h / \partial x_1^s(0) = 0$ for $s \leq k$. In fact, $S_{1^k}(f)$ is given by the equations
$$
\frac{\partial h}{\partial x_1} = \cdots = \frac{\partial^k h}{\partial x_1^k} = 0
$$
(recall the proof of Proposition 3.13).

We proceed by induction. In case $k = 1$, $S_1(f) = S_{1^1}(f)$ as both are given by the equation $\partial h / \partial x_1 = 0$. The transversality hypothesis guarantees that $S_1(f)$ is a submanifold.

Now assume inductively that $S_{1^{k-1}}^{k-1}(f) = S_{1^{k-1}}(f)$ and that this set is a submanifold. Let $q \in S_{1^{k-1}}(f)$. We claim that $q \in S_{1^{k-1}}^{k-1}(f)$ if and only if $\partial/\partial x_1|_q \in T_q S_{1^{k-1}}(f)$, since
$$
\operatorname{Ker} d(f|_{S_{1^{k-1}}(f)})_q = \operatorname{Ker} (df)_q \cap T_q S_{1^{k-1}}(f)
$$
and $\operatorname{Ker} (df)_q = \langle \partial/\partial x_1|_q \rangle$.

The proof is complete if we can show that
$$
S_{1^{k-1}}^{k-1}(f) = \{ q \in S_{1^{k-1}}(f) \mid \partial/\partial x_1|_q \in T_q S_{1^{k-1}}(f) \}.
$$

But by the induction hypothesis and the coordinate representation, $S_{1^{k-1}}(f)$ is defined by $\partial h/\partial x_1 = \cdots = \partial^{k-1} h/\partial x_1^{k-1} = 0$. A point $q$ in this submanifold has $\partial/\partial x_1|_q$ tangent to it precisely when the additional equation $\partial^k h/\partial x_1^k = 0$ holds at $q$. But this is exactly the defining equation for $S_{1^k}(f)$, completing the induction.

(Note: The original OCR text cuts off mid-sentence at line 70. The proof above reconstructs the induction argument from the available fragment and the standard theory of intrinsic derivatives.)
