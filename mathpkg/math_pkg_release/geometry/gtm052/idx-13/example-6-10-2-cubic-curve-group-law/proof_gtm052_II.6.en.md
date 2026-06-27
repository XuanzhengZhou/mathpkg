---
role: proof
locale: en
of_concept: example-6-10-2-cubic-curve-group-law
source_book: gtm052
source_chapter: "II"
source_section: "6"
---
Let $P_0 = (0,1,0)$ be the inflection point on $X$, with tangent line $z=0$ giving divisor $3P_0$. For any line $L$ meeting $X$ in three points $P,Q,R$, we have $P+Q+R \sim 3P_0$ since $L \sim z=0$ on $\mathbf{P}^2$.

The map $P \mapsto P - P_0 \in \text{Cl}^0 X$ is injective: if $P-P_0 \sim Q-P_0$, then $P \sim Q$, which would imply $X$ is rational (previous example), impossible. 

For surjectivity, let $D = \sum n_i P_i \in \text{Cl}^0 X$ with $\sum n_i = 0$. Write $D = \sum n_i (P_i - P_0)$. Using the relation $P+Q+R \sim 3P_0$, if $P_0+R+T \sim 3P_0$, then $(P-P_0)+(Q-P_0) \sim (T-P_0)$. By induction on $\sum |n_i|$, one reduces $D$ to $P-P_0$ for some $P$, showing surjectivity.

The addition law defines a morphism $X \times X \to X$ and the inverse a morphism $X \to X$, making $X$ a group variety.
