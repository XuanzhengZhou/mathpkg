---
role: proof
locale: en
of_concept: csa-characterization
source_book: gtm009
source_chapter: "15"
source_section: "15.3"
---

**($\Leftarrow$)** Suppose that $H = L_0(\operatorname{ad} z)$ is an Engel subalgebra of $L$. By Lemma B of (15.2), $H$ is self-normalizing. If in addition $H$ properly contains no other Engel subalgebra, then the hypotheses of Lemma A of (15.2) are satisfied (with $H = K$), forcing

$$H = L_0(\operatorname{ad} z) \subset L_0(\operatorname{ad} x)$$

for all $x \in H$. In particular, $\operatorname{ad}_H x$ is nilpotent for all $x \in H$. By Engel's Theorem, $H$ is nilpotent. Thus $H$ is both nilpotent and self-normalizing, hence a CSA.

**($\Rightarrow$)** Conversely, let $H$ be a CSA of $L$. Since $H$ is nilpotent, $H \subset L_0(\operatorname{ad} x)$ for all $x \in H$. We want equality to hold for at least one $x$. Suppose, on the contrary, that this never happens. Take $L_0(\operatorname{ad} z)$, $z \in H$, to be as small as possible.

Then $H$ is properly contained in $L_0(\operatorname{ad} z)$. Apply Lemma A of (15.2) with $K = H$: this forces $L_0(\operatorname{ad} z) \subset L_0(\operatorname{ad} x)$ for all $x \in H$. By the minimal choice of $z$, we deduce $L_0(\operatorname{ad} z) = L_0(\operatorname{ad} x)$ for all $x \in H$ for which $L_0(\operatorname{ad} x)$ is minimal.

Now consider the action of $\operatorname{ad}_H z$ on the quotient space $L_0(\operatorname{ad} z)/H$. Since $\operatorname{ad}_H z$ is nilpotent (as $H$ is nilpotent), if $L_0(\operatorname{ad} z) \neq H$, there exists $y \in L_0(\operatorname{ad} z) \setminus H$ such that $[z, y] \in H$. But then for any $h \in H$, one can show $[h, y] \in H$ using the nilpotence of $\operatorname{ad}_H h$, implying $y$ normalizes $H$, contradicting $N_L(H) = H$. Therefore $H = L_0(\operatorname{ad} z)$, so $H$ is indeed an Engel subalgebra. Minimality follows from Lemma A.
