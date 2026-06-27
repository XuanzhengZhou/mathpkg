---
role: proof
locale: en
of_concept: stationary-chain-decomposition
source_book: gtm046
source_chapter: "XI"
source_section: "37"
---

The ergodic decomposition theorem for invariant probabilities states that every invariant probability measure \(\bar{P}\) can be uniquely decomposed into an integral of indecomposable (ergodic) invariant probabilities. When applied to a Markov chain with transition probability function \(P(x, S)\) and invariant distribution \(P_1\), this general theorem yields the decomposition of the stationary chain.

Specifically, let the stationary chain be determined by an invariant probability \(P_1\) and transition probability \(P(x, S)\). The joint distribution of the chain is a probability measure on the sequence space that is invariant under the shift transformation. By the ergodic decomposition theorem, this invariant measure decomposes as

$$
P = \int_{\mathcal{E}} P_\alpha \, \nu(d\alpha),
$$

where \(\mathcal{E}\) indexes the ergodic components, \(\nu\) is a probability measure on the index space, and each \(P_\alpha\) is an ergodic (indecomposable) invariant probability measure.

Each component measure \(P_\alpha\), when restricted to the one-dimensional distributions, yields a probability measure \(P_{1,\alpha}(S) = P_\alpha(X_1 \in S)\), and the transition probabilities \(P_\alpha(x, S)\) are obtained via conditioning. The chain \((P_{1,\alpha}, P_\alpha(x, S))\) is then stationary (since \(P_\alpha\) is invariant under the shift) and indecomposable (since \(P_\alpha\) is ergodic). Thus every component chain is stationary and indecomposable.

The indecomposability implies that the component chain has trivial tail \(\sigma\)-field and satisfies a zero-one law: every shift-invariant event has probability either 0 or 1 under \(P_\alpha\).
