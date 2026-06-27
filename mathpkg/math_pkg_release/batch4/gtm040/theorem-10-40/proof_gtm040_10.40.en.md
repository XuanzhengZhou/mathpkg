---
role: proof
locale: en
of_concept: theorem-10-40
source_book: gtm040
source_chapter: "10"
source_section: "40"
---

**Proof:** By Lemma 10-39,

$$\mu^h(C \cap \bar{S}) = \Pr^h[x_v \in C \cap \bar{S}] = \int_S \Pr^{K(\cdot,x)}[x_v \in C \cap \bar{S}] d\nu(x).$$

But by Proposition 10-35,

$$\Pr^{K(\cdot,x)}[x_v \in C \cap \bar{S}] = \mu^K(\cdot,x)(C \cap \bar{S}) = \chi_{C \cap S}(x).$$

Hence for all Borel sets $C \cap \bar{S}$

$$\mu^h(C \cap \bar{S}) = \int_S \chi_{C \cap S}(x) d\nu(x) = \nu(C \cap \bar{S}).$$

Since $\nu(\bar{S}) = 1$, we must have $\mu^h(\bar{S}) = 1$ and hence $\mu^h(C) = \nu(C)$ for all Borel sets $C$ in $S^*$.

We have not yet proved that the representation in Theorem 10-40 does hold for the measure $\mu^h$, but this fact is a consequence of

r regular arises by decomposing the integral over $\bar{S}$ into a part over $S$ and a part over $B_e$. If $h$ is normalized, then the measure that corresponds to $h$ is $\mu^h$.

Proof: By Fubini's Theorem any function of the form

$$h_i = \int_S K(i, x) d\nu(x)$$

with $\nu$ finite is non-negative superregular and has $\pi h = \nu(\bar{S})$.

Conversely, let $h$ be given. If $\pi h = 0$, then the superregularity of $h$ implies that

$$0 = \pi h \geq \pi P^n h \geq 0$$

for all $n$ and hence $\pi P^n h = 0$ for all $n$. Thus $(\pi N)h = 0$. Since $\pi N$ is everywhere positive, $h = 0$. Thus existence and uniqueness of $\nu$ follow if $\pi h = 0$. Next, let $\pi h$ be positive. Since $h$ and $\nu$ must be related by $\pi h = \nu(\bar{S})$, we may, for both existence and uniqueness, divide $h$ by an appropriate positive constant to obtain $\pi h = 1$. Uniqueness of $\nu$ and the fact that $\nu = \mu^h$ then follow from Theorem 10-40. Existence of $\nu$ follows from Theorem 10-26 provided we can show that $\mu^h(S^* - \bar{S}) = 0$. By Lemma 10-32,

$$\bar{S}^h \subset S^{h*} \cap \bar{S}.$$

Hence

$$\mu^h(\bar{S}) = \mu^h(S^{h*} \cap \bar{S}) \geq \mu^h(\bar{S}^h).$$

But the right side equals one by Proposition 10-38. Thus $\mu^h(\bar{S}) = 1$ and $\mu^h(S^* - \bar{S}) = 0$.

Finally we have $\bar{S} = S \cup B_e$ disjointly

then Fatou's Theorem asserts that for almost every $x$ [m] on the circle, $h(re^{i\theta}) \rightarrow f(x)$ whenever $re^{i\theta}$ converges to $x$ nontangentially. In this section we shall prove a Markov chain analog of this theorem in terms of the Martin boundary and the measures given by Theorem 10-41. As expected, harmonic measure $\mu$ will play the role of Lebesgue measure.

Our procedure will be first to derive an almost everywhere statement in terms of the measure on the probability space and then to translate this statement into a result in terms of harmonic measure. As a preliminary to the first step, we consider a special case in the lemma below.

We shall be dealing with expressions of the form $\lim_{n \to \infty} h(x_n(\omega))$ in this section, where $h$ is non-negative and $P$-regular, and we shall adopt the convention that $h(x_n(\omega)) = 0$ if $n > v$. This definition is motivated by the following consideration: If $\bar{P}$ is the enlarged chain for $P$, then a $P$-regular function $h$ extends to be regular for $\bar{P}$ if $h$ is defined to be zero at the absorbing state; consequently if $\pi h$ is finite, $\{h(x_n)\}$ is a martingale with $M[h(x_0)] = \pi h$.
