---
role: proof
locale: en
of_concept: kochen-specker-nonembeddability
source_book: gtm053
source_chapter: "12"
source_section: "12.9"
---

**Proof.** We choose a real Euclidean space $E^3 \subset \mathcal{H}$ and show that even $B(E^3)$ cannot be embedded in a Boolean algebra. Otherwise there would exist a homomorphism of the partial Boolean algebra $B(E^3)$ onto the two-element Boolean algebra $\{0, 1\}$, since for any pair of elements in any Boolean algebra, there exists a homomorphism onto $\{0, 1\}$ that separates them.

Let $h$ be such a homomorphism. If $a_1, a_2, a_3 \in E^3$ are pairwise orthogonal lines, then $h(a_i \wedge a_j) = h(a_i) \wedge h(a_j) = 0$ for $i \neq j$. Hence, in any pair of orthogonal lines, at least one of the pair must go to $0$ under $h$.

Then the images of $a_3$ and $a_4$ are determined up to a sign by the property of being orthogonal to $(a_1, a_5)$ and $(a_2, a_6)$, and we choose

$$a_3 \mapsto \frac{\xi \bar{y} - \bar{z}}{\sqrt{1 + \xi^2}}, \quad a_4 \mapsto \frac{\eta \bar{x} - \bar{y}}{\sqrt{1 + \eta^2}}.$$

We similarly set

$$a_0 \mapsto \frac{\xi \eta \bar{x} - \xi \bar{y} + \bar{z}}{\sqrt{1 + \xi^2 + \xi^2 \eta^2}}, \quad a_7 \mapsto \frac{\bar{x} + \eta \bar{y} + \xi \eta \bar{z}}{\sqrt{1 + \eta^2 + \xi^2 \eta^2}},$$

and finally, $a_8$ and $a_9$ are determined up to sign. The sine of the angle between $a_0$ and $a_9$ is easy to compute: it equals

$$\xi \eta / \sqrt{(1 + \xi^2 + \xi^2 \eta^2)(1 + \eta^2 + \xi^2 \eta^2)}.$$

As $\xi$ and $\eta$ vary, this expression takes on all values in $[0, \frac{1}{3}]$.

Now consider the graph $\Gamma_2$ from Lemma 12.14, which is realized on $S^2$. Let $k$ be the composition of the embedding of $B(E^3)$ into a Boolean algebra with the homomorphism onto $\{0, 1\}$. We must have $k(p_1) = k(a_9) = 1$. In fact, if we had $k(a_9) = 0$, then we would also have $k(a_7) = 1$, and then $k(a_1) = k(a_2) = k(a_3) = k(a_4) = 0$, and $k(a_5) = k(a_6) = 1$, which is a contradiction.

We now return to $\Gamma_2$. Since $k(p_0) = k(p_1) = 1$, we similarly find that $k(p_2) = 1$, and then $k(p_3) = k(p_4) = k(q_0) = 1$. But $k(q_0) = 1$ contradicts the fact that $k(p_0) = 1$. This completes the proof. $\square$
