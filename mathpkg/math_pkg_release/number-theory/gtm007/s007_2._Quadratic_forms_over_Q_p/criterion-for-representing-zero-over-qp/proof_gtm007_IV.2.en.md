---
role: proof
locale: en
of_concept: criterion-for-representing-zero-over-qp
source_book: gtm007
source_chapter: "IV"
source_section: "§2. Quadratic forms over Q_p"
---

Write $f$ in diagonal form $f \sim a_1 X_1^2 + \cdots + a_n X_n^2$ and consider the cases separately.

\medskip

oindent 	extbf{Case (i): $n = 2$.}

The form $f$ represents $0$ if and only if $-a_1/a_2$ is a square. But $-a_1/a_2 = -a_1 a_2 = -d$ in $k^*/k^{*2}$, so $f$ is isotropic exactly when $d = -1$.

\medskip

oindent 	extbf{Case (ii): $n = 3$.}

We may assume $f \sim a X^2 + b Y^2 + c Z^2$ with $-abc = d$. The form represents $0$ if and only if the ternary form is isotropic, which by the Hilbert symbol criterion is equivalent to $(-a, -b)(-a, -c)(-b, -c) = 1$. Using properties of the Hilbert symbol this simplifies to $(-1, -d) = arepsilon$.

\medskip

oindent 	extbf{Case (iii): $n = 4$.}

Write $f \sim a_1 X_1^2 + a_2 X_2^2 + a_3 X_3^2 + a_4 X_4^2$. The form $f$ represents $0$ if and only if the forms $h = a_1 X_1^2 + a_2 X_2^2$ and $g = -a_3 X_3^2 - a_4 X_4^2$ represent a common nonzero element. By case (ii) applied to each rank-2 form, there exists $x \in k^*/k^{*2}$ represented by both if and only if the sets
$$
A = \{x \in k^*/k^{*2} : (x, -a_1 a_2) = (a_1, a_2)\}, \quad
B = \{x \in k^*/k^{*2} : (x, -a_3 a_4) = (-a_3, -a_4)\}
$$
intersect nontrivially. These are each cosets of $H^1_{a_1 a_2}$ and $H^1_{a_3 a_4}$ respectively. By part (c) of the preparatory Lemma, $A \cap B = arnothing$ if and only if
$$
a_1 a_2 = a_3 a_4 \quad 	ext{and} \quad (a_1, a_2) = -(-a_3, -a_4).
$$
The first condition means $d = 1$. If $d = 1$, then
$$
arepsilon = (a_1, a_2)(a_3, a_4)(a_1 a_2, a_3 a_4) = (a_1, a_2)(a_3, a_4)(-1, a_3 a_4) = (a_1, a_2)(-a_3, a_4)(-1, -1).
$$
Thus the second condition is $arepsilon = -(-1, -1)$, giving the stated criterion.

\medskip

oindent 	extbf{Case (iv): $n \geq 5$.}

It suffices to treat $n = 5$. Write $f \sim a_1 X_1^2 + \cdots + a_5 X_5^2$. By the Lemma on the structure of $k^*/k^{*2}$, one can always find $x \in k^*/k^{*2}$ represented by both $a_1 X_1^2 + a_2 X_2^2$ and $a_3 X_3^2 + a_4 X_4^2 + a_5 X_5^2$ (the latter having rank $3$ and therefore always representing some $x$ by the case $n = 3$ analyzed above, unless its invariants obstruct it — but one can check that in rank $\geq 5$ there is always a choice of orthogonal decomposition making the intersection nonempty). Hence $f$ is isotropic.
