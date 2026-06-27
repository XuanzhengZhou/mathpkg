---
role: proof
locale: en
of_concept: lem-2
source_book: gtm095
source_chapter: "Chapter 1"
source_section: "§3. Random walk, arcsine law, ruin problem"
---

# Proof of Lemma 2

**Statement.** Let $u_0 = 1$ and $0 \leq k \leq n$. Then

$$P_{2k, 2n} = u_{2k} \cdot u_{2n-2k},$$

where $P_{2k, 2n}$ is the probability that during the interval $[0, 2n]$ the particle spends $2k$ units of time on the positive side, and $u_{2k} = P(S_{2k} = 0)$.

**Proof.** The proof proceeds in two steps. First we establish the identity

$$u_{2k} = \sum_{l=1}^{k} P\{S_{2(k-l)} = 0\} \, P\{\sigma_{2n} = 2l\}, \tag{13}$$

where $\sigma_{2n}$ is the first time the walk reaches zero.

Since $\{S_{2k} = 0\} \subseteq \{\sigma_{2n} \leq 2k\}$, we have the disjoint decomposition

$$\{S_{2k} = 0\} = \{S_{2k} = 0\} \cap \{\sigma_{2n} \leq 2k\} = \bigcup_{1 \leq l \leq k} \bigl(\{S_{2k} = 0\} \cap \{\sigma_{2n} = 2l\}\bigr).$$

Consequently,

$$u_{2k} = P(S_{2k} = 0) = \sum_{1 \leq l \leq k} P(S_{2k} = 0, \sigma_{2n} = 2l)$$

$$= \sum_{1 \leq l \leq k} P(S_{2k} = 0 \mid \sigma_{2n} = 2l) \; P(\sigma_{2n} = 2l).$$

We now simplify the conditional probability. By the definition of $\sigma_{2n}$,

$$P(S_{2k} = 0 \mid \sigma_{2n} = 2l) = P(S_{2k} = 0 \mid S_1 \neq 0, \ldots, S_{2l-1} \neq 0, S_{2l} = 0)$$

$$= P\bigl(S_{2l} + (\xi_{2l+1} + \cdots + \xi_{2k}) = 0 \mid S_1 \neq 0, \ldots, S_{2l-1} \neq 0, S_{2l} = 0\bigr).$$

Since the increments $\xi_{2l+1}, \ldots, \xi_{2k}$ are independent of the event $\{S_1 \neq 0, \ldots, S_{2l} = 0\}$, the conditioning reduces to conditioning on $S_{2l} = 0$ alone:

$$P\bigl(S_{2l} + (\xi_{2l+1} + \cdots + \xi_{2k}) = 0 \mid S_{2l} = 0\bigr) = P(\xi_{2l+1} + \cdots + \xi_{2k} = 0) = P(S_{2(k-l)} = 0).$$

Hence

$$u_{2k} = \sum_{1 \leq l \leq k} P\{S_{2(k-l)} = 0\} \; P\{\sigma_{2n} = 2l\},$$

which establishes (13).

Now, to prove the lemma, we use induction on $n$ together with the recurrence relation

$$P_{2k, 2n} = \frac{1}{2} \sum_{r=1}^{k} f_{2r} \, P_{2k-2r, 2n-2r} + \frac{1}{2} \sum_{r=1}^{n-k} f_{2r} \, P_{2k, 2n-2r}, \tag{14}$$

where $f_{2r} = P(\sigma_{2n} = 2r)$. Assume that $P_{2k, 2m} = u_{2k} \cdot u_{2m-2k}$ holds for all $m = 1, \ldots, n-1$. Applying the induction hypothesis in (14) yields

$$P_{2k, 2n} = \frac{1}{2} u_{2n-2k} \sum_{r=1}^{k} f_{2r} \, u_{2k-2r} + \frac{1}{2} u_{2k} \sum_{r=1}^{n-k} f_{2r} \, u_{2n-2r-2k}.$$

By formula (13), each inner sum evaluates to the corresponding $u$-term:

$$\sum_{r=1}^{k} f_{2r} \, u_{2k-2r} = u_{2k}, \qquad \sum_{r=1}^{n-k} f_{2r} \, u_{2n-2r-2k} = u_{2n-2k}.$$

Therefore

$$P_{2k, 2n} = \frac{1}{2} u_{2n-2k} \, u_{2k} + \frac{1}{2} u_{2k} \, u_{2n-2k} = u_{2k} \, u_{2n-2k}.$$

This completes the proof of the lemma. ∎
