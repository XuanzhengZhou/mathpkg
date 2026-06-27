---
role: proof
locale: en
of_concept: markovian-function-condition
source_book: gtm017
source_chapter: "III"
source_section: "d"
---
Let $Y(m) = f(X(m))$ with state sets $S_\alpha$. If $Y(m)$ is Markovian, the joint probabilities factor:
$$P[Y(1)=\alpha, Y(2)=\beta, Y(3)=\gamma] = P[Y(1)=\alpha]P[Y(2)=\beta|Y(1)=\alpha]P[Y(3)=\gamma|Y(2)=\beta].$$

Writing both sides in terms of $X(m)$ probabilities and letting all but two initial weights tend to zero yields the condition $p_{i, S_\beta} = C_{S_\alpha, S_\beta}$ for $i \in S_\alpha$.

Sufficiency is verified by induction on joint probabilities, showing Markovian factorization holds.

For reversible chains with $DP = PD$, the matrix formulation $(I - BA)PB = 0$ (where $B_{i,j} = 1$ if $i \in S_j$) captures the condition. $D(I-BA)$ is positive definite, so factoring $D(I-BA) = RR$ gives $RPB=0 \implies RRPB = D(I-BA)PB = 0 \implies (I-BA)PB = 0$.
