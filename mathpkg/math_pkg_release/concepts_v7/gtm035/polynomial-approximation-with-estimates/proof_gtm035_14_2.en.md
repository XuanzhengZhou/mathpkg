---
role: proof
locale: en
of_concept: polynomial-approximation-with-estimates
source_book: gtm035
source_chapter: "14"
source_section: "14.2"
---
# Proof of Polynomial Approximation with Estimates

Let $P_n$ be as in Lemma 14.1 (the polynomial that approximates $1/(w + 1/n)$ on the closed semidisk $S$). Then

$$
|w P_n(w)|
= |w| \left| P_n(w) - \frac{1}{w + \frac{1}{n}} + \frac{1}{w + \frac{1}{n}} \right|
\leq |w| \left| P_n(w) - \frac{1}{w + \frac{1}{n}} \right|
+ \left| \frac{w}{w + \frac{1}{n}} \right|
\leq \frac{|w|}{n} + 1
\leq C, \quad w \in S,
$$

where $C = r_0 + 1$, since $|w| < |w + 1/n|$ for $\operatorname{Re}(w) > 0$, and the semidisk $S$ lies in the right half-plane.

This follows from Lemma 14.1 which guarantees $\left|P_n(w) - \frac{1}{w+1/n}\right| \leq \frac{1}{n}$ on $S$. Hence

$$
|P_n(w)| \leq \frac{C}{|w|}, \quad w \in S \setminus \{0\}, \; n = 1, 2, \dots.
$$

Also, for each fixed $w \in S \setminus \{0\}$,

$$
P_n(w) - \frac{1}{w} \to 0 \quad \text{as} \quad n \to \infty,
$$

since $P_n(w)$ approximates $1/(w + 1/n)$ and $1/(w + 1/n) \to 1/w$.

Thus the sequence $\{P_n\}$ satisfies both required properties:
1. $P_n(w) \to 1/w$ for all $w \in S \setminus \{0\}$, and
2. $|P_n(w)| \leq C/|w|$ for all $w \in S \setminus \{0\}$ and all $n$.

$\square$
