---
role: proof
locale: en
of_concept: borel-cantelli-lemma
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Borel--Cantelli Lemma

**Borel--Cantelli Lemma.** Let $A_1, A_2, \ldots$ be a sequence of events in $\mathcal{F}$. Let $\{A_n \text{ i.o.}\}$ denote the event $\limsup A_n$ that consists in the realization of infinitely many of $A_1, A_2, \ldots$.

(a) If $\sum_{n=1}^{\infty} P(A_n) < \infty$, then $P(A_n \text{ i.o.}) = 0$.

(b) If the events $A_1, A_2, \ldots$ are independent and $\sum_{n=1}^{\infty} P(A_n) = \infty$, then $P(A_n \text{ i.o.}) = 1$.

*Proof.* (a) By definition $A_n \text{ i.o.} = \limsup A_n = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k$. For every $n$,

$$P(A_n \text{ i.o.}) \leq P\left(\bigcup_{k=n}^{\infty} A_k\right) \leq \sum_{k=n}^{\infty} P(A_k).$$

But $\sum_{k=1}^{\infty} P(A_k) < \infty$ implies $\sum_{k=n}^{\infty} P(A_k) \to 0$ as $n \to \infty$. Therefore $P(A_n \text{ i.o.}) = 0$.

(b) Since $P(\bigcap_{k=n}^{\infty} \bar{A}_k) = \prod_{k=n}^{\infty} P(\bar{A}_k)$ by independence, and $\log(1-x) \leq -x$ for $0 \leq x < 1$,

$$\log \prod_{k=n}^{\infty} [1 - P(A_k)] = \sum_{k=n}^{\infty} \log[1 - P(A_k)] \leq -\sum_{k=n}^{\infty} P(A_k) = -\infty.$$

Consequently $P(\bigcap_{k=n}^{\infty} \bar{A}_k) = 0$ for all $n$, and therefore

$$P(A_n \text{ i.o.}) = 1 - \lim_{n \to \infty} P\left(\bigcap_{k=n}^{\infty} \bar{A}_k\right) = 1.$$

This completes the proof of the lemma. $\square$
