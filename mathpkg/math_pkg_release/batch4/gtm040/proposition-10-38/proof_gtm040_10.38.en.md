---
role: proof
locale: en
of_concept: proposition-10-38
source_book: gtm040
source_chapter: "10"
source_section: "38"
---

**Proof:** Applying Lemma 10-37 to the statement $x_v \in D$, where $D$ is a Borel set of $S^*$, we have for any Borel subset $C$ of $S_N$

$$\Pr[x_v \in D \land x_v \in C] = \int_C \Pr^{K(\cdot, x)}[x_v \in D] d\mu(x) = \int_C \mu^{K(\cdot, x)}(D) d\mu(x).$$

But by definition

$$\Pr[x_v \in D \land x_v \in C] = \mu(D \cap C) = \int_C \chi_D(x) d\mu(x).$$

The set on which two Borel meas

Remembering that $S_N$ is a Borel set of harmonic measure one, we see that $T$ is the denumerable intersection of Borel sets of measure one and is therefore a Borel set with $\mu(T) = 1$. We show $T = \bar{S}$.

First let $x \in T$. Choose $s_n$ in $S$ with $d(x, s_n) < 1/n$, and let $D_n$ be the intersection with $S_N$ of the ball with center $s_n$ and radius $1/n$. By assumption

$$\mu^{K(\cdot, x)}(D_n) = \chi_{D_n}(x) = 1$$

for all $n$. Hence

$$\mu^{K(\cdot, x)}(\{x\}) = \mu^{K(\cdot, x)}(\cap D_n) = 1.$$

Therefore $x \in \bar{S}$ by Proposition 10-35.

Conversely, if $x \in \bar{S}$, then

$$\mu^{K(\cdot, x)}(\{x\}) = 1$$

by Proposition 10-35, and so

$$\mu^{K(\cdot, x)}(D) = \chi_D(x)$$

for all Borel sets $D$ in $S_N$. Therefore $x \in T$, and $T = \bar{S}$.
