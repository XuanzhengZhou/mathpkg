---
role: proof
locale: en
of_concept: integral-representation-of-superregular-functions
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
By Fubini's theorem, any function of the form

$$h_i = \int_{S} K(i, x) \, d\nu(x)$$

with $\nu$ finite is nonnegative superregular and has $\pi h = \nu(\bar{S})$.

Conversely, let $h$ be given. If $\pi h = 0$, then the superregularity of $h$ implies that

$$0 = \pi h \geq \pi P^n h \geq 0$$

for all $n$, and hence $\pi P^n h = 0$ for all $n$. Thus $(\pi N) h = 0$. Since $\pi N$ is everywhere positive, $h = 0$. Hence existence and uniqueness of $\nu$ follow trivially if $\pi h = 0$.

Next, let $\pi h > 0$. Since $h$ and $\nu$ must be related by $\pi h = \nu(\bar{S})$, we may, for both existence and uniqueness, divide $h$ by an appropriate positive constant to obtain $\pi h = 1$. Uniqueness of $\nu$ and the fact that $\nu = \mu^h$ then follow from Theorem 10-40.

Existence of $\nu$ follows from Theorem 10-26 provided we can show that $\mu^h(S^* \setminus \bar{S}) = 0$. By Lemma 10-32,

$$\bar{S}^h \subset S^{h*} \cap \bar{S}.$$

Hence

$$\mu^h(\bar{S}) = \mu^h(S^{h*} \cap \bar{S}) \geq \mu^h(\bar{S}^h).$$

But the right side equals one by Proposition 10-38. Thus $\mu^h(\bar{S}) = 1$ and $\mu^h(S^* \setminus \bar{S}) = 0$.

Finally, we have $\bar{S} = S \cup B_e$ disjointly, where $S$ is the original state space and $B_e$ is the set of extreme points in the Martin boundary.
