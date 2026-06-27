---
role: proof
locale: en
of_concept: thm-suppose-that-is-the-transition-function
source_book: gtm034
source_chapter: "7"
source_section: "017"
---

Proof: Let $Q(x,y) = P(x,y)$ when $x,y$ are in $R - A$, and let $Q_n(x,y)$ be the iterates of the transient kernel $Q$ defined on the set $S = R - A$. (Q is a transient kernel if, as we may assume, the set $A$ is nonempty, since the original random walk is recurrent.) Observe that $f(x)$ is excessive, relative to $Q$ on $S$, because

(1) $f(x) - \sum_{y \in S} Q(x,y)f(y) \geq \sum_{t \in A} P(x,t)f(t) = w(x) \geq 0, \quad x \in S.$

Proceeding as in the proof of the Riesz decomposition theorem, as one may since $Pf - f \leq 0$ on $S$, one iterates the application of $Q$ to (1)

Here $H_A(x,t)$ is of course the hitting probability measure of the set $A$, for the random walk given by $P(x,y)$ on $R$. Now it follows from (2) that

$$f(x) \geq \sum_{t \in A} H_A(x,t)f(t)$$

$$\geq \left[ \inf_{t \in A} f(t) \right] \sum_{t \in A} H_A(x,t) = \inf_{t \in A} f(t), \quad x \in S.$$

That proves T2. We shall actually use only the very special case when the set $A$ is a single point. Nevertheless the full strength of T2 is indispensable in developing further the logarithmic type potential theory which was sketched at the end of the last section.

Letting $A = \{0\}$ in T2 the following extension of T1 is immediate
