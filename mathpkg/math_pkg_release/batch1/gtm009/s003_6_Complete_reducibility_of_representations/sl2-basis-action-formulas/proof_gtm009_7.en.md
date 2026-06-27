---
role: proof
locale: en
of_concept: sl2-basis-action-formulas
source_book: gtm009
source_chapter: "II"
source_section: "7"
---

(a) Follows by repeated application of Lemma 7.1, since $y$ lowers weight by 2 each time.

(b) This is precisely the definition of $v_{i+1}$.

(c) Use induction on $i$. The case $i = 0$ holds since $v_{-1} = 0$ by convention and $x.v_0 = 0$ because $v_0$ is a maximal vector. Assume true for $i-1$:
\begin{align*}
i x.v_i &= x.y.v_{i-1} &&\text{(by definition)}\\
&= [x, y].v_{i-1} + y.x.v_{i-1} \\
&= h.v_{i-1} + y.x.v_{i-1} \\
&= (\lambda - 2(i-1))v_{i-1} + (\lambda - (i-1) + 1)y.v_{i-2} &&\text{(by (a) and induction)}\\
&= \ldots = i(\lambda - i + 1)v_{i-1}.
\end{align*}
Dividing by $i$ yields the result.
