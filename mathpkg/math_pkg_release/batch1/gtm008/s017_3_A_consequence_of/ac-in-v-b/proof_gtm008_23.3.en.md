---
role: proof
locale: en
of_concept: ac-in-v-b
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

In most cases $B$ satisfies the additional requirement that $V^{(B)}$ is a model of $ZF$. In this case we can prove the $AC$ in $V^{(B)}$ by a forcing argument just as in Theorem 14.25 with suitable modifications as in the proof of Theorem 23.24 below. However, since we shall give an example of a Boolean algebra $B$ such that $V^{(B)}$ does not satisfy the Axiom of Powers, we indicate a direct proof of Theorem 23.23 in the general case. We take the Axiom of Choice in the following form:

$(\forall u)(\exists v)(\forall x \in u)[(\exists y \in x)(\exists! x' \in u)[y \in x'] \rightarrow (\exists! y \in x)[y \in v]]$.

Let $\phi(x, y)$ be $y \in x \wedge (\exists! x' \in u)[y \in x']$, $u \in V^{(B)}$. Since $\bigcup_{x \in \mathcal{D}(u)} \mathcal{D}(x)$ is a set, let $\{y_\xi \mid \xi < \alpha\}$ be an enumeration of this set (using the $AC$ in $V$). Then define $v \in V^{(B)}$ by

$$\mathcal{D}(v) = \bigcup_{x \in \mathcal{D}(u)} \mathcal{D}(x) = \{y_\xi \mid \xi < \alpha\},$$

$(\forall y \in \mathcal{D}(v)) \left[ v(y) = \sum_{x \in \mathcal{D}(u)} \sum_{\xi < \alpha} ([y = y_\xi \wedge \phi(x, y_\xi)] \cdot \prod_{\eta < \xi} [\neg \phi(x, y_\eta)]) \right]$.

Note that $v(y) \in B$, since we have only sup's and inf's over sets. Now one can show that $v$ is the required choice function.
