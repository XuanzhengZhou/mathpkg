---
role: proof
locale: en
of_concept: lemma-1-27
source_book: gtm040
source_chapter: "1"
source_section: "27"
---

**Proof:** Since $A \supset (A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_k)$, we have, by Lemma 1-20, $\mu(A) \geq \mu(A_1 \cup A_2 \cup \cdots \cup A_k)$, and by Lemma 1-26 the right side equals $\sum_{n=1}^k \mu(A_n)$ for each $k$. Hence

$$\mu(A) \geq \

Since the last expression on the right is the tail of a convergent series, we have $B_n \rightarrow A$. Since $B_n \in \mathcal{F}^*$, we can find $L_n$ in $\mathcal{F}$ such that $d(L_n, B_n) \leq 1/n$. Then $d(L_n, A) \leq 1/n + d(B_n, A)$, and hence $L_n \rightarrow A$. Thus $A$ is in $\mathcal{F}^*$.

Remark: If $A \in \mathcal{G}^*$ with $\mu(A)$ finite, then $A$ is in $\mathcal{F}^*$; hence for every $\epsilon > 0$ there is a $B$ in $\mathcal{F}$ such that $\mu(A \oplus B) \leq \epsilon$. Conversely, if there exists such a $B_\epsilon$ for any $\epsilon$, then $B_{1/n} \rightarrow A$ so that $A \in \mathcal{F}^*$ and, a fortiori, $A \in \mathcal{G}^*$. These observations give a characterization of the sets $A$ in $\mathcal{G}^*$ for which $\mu(A)$ is finite.

Lemma 1-29: $\mu$ is completely additive on $\mathcal{G}^*$, and $\mathcal{G}^*$ is a Borel field.

Proof: Suppose

$$A = \bigcup_n A_n$$

is the union of disjoint sets $\{A_n\}$ in $\mathcal{G}^*$. Then $\mu(A) \geq \mu(A_n)$ for every $n$ by Lemma 1-20, so that we may assume $\mu(A_n) < \infty$ for every $n$. The complete additivity of $\mu$ now follows from Lemmas 1-28 and 1-27. For the proof that $\mathcal{G}^*$ is a Borel field, we see clearly that $\mathcal{G}^*$ is closed under denumerable unions. It remains to be proved that $\mathcal{G}^*$ is closed under complementation. Since $\nu$ is sigma-finite, let

$$X = \bigcup_n A_n$$

with $A_n$ in $\mathcal{

Lemma 1-29, $G^*$ is a Borel field containing $\mathcal{F}$, $G^*$ contains $\mathcal{G}$. The extended measure restricted to sets of $\mathcal{G}$ has the desired properties. For uniqueness, suppose $\mu'$ is another measure on $\mathcal{G}$ that agrees with $\nu$ on $\mathcal{F}$. Since, by sigma-finiteness, $X$ is the union of sets $A_n$ in $\mathcal{F}$ of finite $\nu$-measure, we may assume that $X$ is a disjoint union of sets of finite measure by letting $B_n = A_n - \bigcup_{k < n} A_k$. Let $C$ be any set in $\mathcal{G}$; we want to show $\mu'(C) = \mu(C)$. By definition,

$$\mu(C) = \inf \left\{ \sum_n \nu(C_n) \right\}$$

with the infimum taken over covers $\{C_n\}$, where $C_n$ is in $\mathcal{F}$. For any fixed cover $\{C_n\}$, we have

$$\mu'(C) \leq \mu' \left( \bigcup_n C_n \right) \leq \sum_n \mu'(C_n) = \sum_n \nu(C_n).$$

Therefore

$$\mu'(C) \leq \inf \left\{ \sum_n \nu(C_n) \right\} = \mu(C).$$

Writing

$$\mu'(C) = \sum_n \mu'(C \cap B_n),$$

we see that it is sufficient to show that

$$\mu'(C \cap B_n) \geq \mu(C \cap B_n).$$

But

$$\mu'(C \cap B_n) + \mu'(\tilde{C} \cap B_n) = \nu(B_n) = \mu(C \cap B_n) + \mu(\tilde{C} \cap B_n).$$

Now we know that $\mu'$ is dominated by $\mu$:

$$\mu'(\tilde{C} \cap B_n) \leq \mu(\tilde{C} \cap B_n) \leq \mu(B_n) < \infty.$$

If

The content of the next proposition is that the property $f(x) < c$ may be replaced by any of the conditions $f(x) \leq c$, $f(x) > c$, or $f(x) \geq c$. Therefore, if $f$ is a measurable function, then the set

$$\{x \mid c \leq f(x) \leq d\}$$

is measurable; either or both of the signs $\leq$ may be replaced by $<$, and the set is still measurable.
