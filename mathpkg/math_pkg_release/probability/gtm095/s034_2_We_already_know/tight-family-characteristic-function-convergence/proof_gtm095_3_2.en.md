---
role: proof
locale: en
of_concept: tight-family-characteristic-function-convergence
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of Characteristic Function Criterion for Tight Families

Let $\{P_n\}$ be a tight family of probability measures on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

**Sufficiency ($\Leftarrow$).** Suppose that for each $t \in \mathbb{R}$ the limit $\lim_n \varphi_n(t)$ exists, where

$$\varphi_n(t) = \int_{\mathbb{R}} e^{itx} \, P_n(dx).$$

Since $\{P_n\}$ is tight, by Prohorov's theorem there exists a subsequence $\{P_{n'}\}$ and a probability measure $P$ such that

$$P_{n'} \xrightarrow{w} P.$$

Suppose, for contradiction, that the whole sequence $\{P_n\}$ does not converge weakly to $P$. Then, by Lemma 1, there exists a subsequence $\{P_{n''}\}$ and a probability measure $Q$ such that $P_{n''} \xrightarrow{w} Q$ and $P \neq Q$.

Now we use the existence of $\lim_n \varphi_n(t)$ for each $t \in \mathbb{R}$. Since both $\{P_{n'}\}$ and $\{P_{n''}\}$ are subsequences of $\{P_n\}$, we have

$$\lim_{n'} \int_{\mathbb{R}} e^{itx} \, P_{n'}(dx) = \lim_{n''} \int_{\mathbb{R}} e^{itx} \, P_{n''}(dx) = \lim_n \varphi_n(t).$$

On the other hand, by the definition of weak convergence applied to the bounded continuous functions $x \mapsto \cos tx$ and $x \mapsto \sin tx$, we obtain

$$\lim_{n'} \int_{\mathbb{R}} e^{itx} \, P_{n'}(dx) = \int_{\mathbb{R}} e^{itx} \, P(dx),$$
$$\lim_{n''} \int_{\mathbb{R}} e^{itx} \, P_{n''}(dx) = \int_{\mathbb{R}} e^{itx} \, Q(dx).$$

Therefore

$$\int_{\mathbb{R}} e^{itx} \, P(dx) = \int_{\mathbb{R}} e^{itx} \, Q(dx), \quad t \in \mathbb{R}.$$

But the characteristic function determines the distribution uniquely (Theorem 2, Sect. 12, Chap. 2). Hence $P = Q$, which contradicts the assumption that $P \neq Q$. Therefore $P_n \xrightarrow{w} P$.

**Necessity ($\Rightarrow$).** If $P_n \xrightarrow{w} P$, then by the definition of weak convergence, for each $t \in \mathbb{R}$,

$$\lim_n \varphi_n(t) = \lim_n \int_{\mathbb{R}} e^{itx} \, P_n(dx) = \int_{\mathbb{R}} e^{itx} \, P(dx),$$

since $x \mapsto e^{itx} = \cos tx + i \sin tx$ is a bounded continuous function. Thus $\lim_n \varphi_n(t)$ exists for all $t \in \mathbb{R}$. $\square$
