---
role: proof
locale: en
of_concept: wedge-product-anticommutativity
source_book: gtm035
source_chapter: "4"
source_section: "4.5"
---

# Proof of Anticommutativity of Wedge Product

**Lemma 4.5.** If $\tau \in \wedge^k(V)$ and $\sigma \in \wedge^l(V)$, then

$$\tau \wedge \sigma = (-1)^{kl} \sigma \wedge \tau.$$

## Proof

Let $\tau \in \wedge^k(V)$ and $\sigma \in \wedge^l(V)$. By definition, for any $\xi_1, \ldots, \xi_{k+l} \in V$,
$$(\tau \wedge \sigma)(\xi_1, \ldots, \xi_{k+l}) = \frac{1}{k! \, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi) \, \tau(\xi_{\pi(1)}, \ldots, \xi_{\pi(k)}) \, \sigma(\xi_{\pi(k+1)}, \ldots, \xi_{\pi(k+l)}).$$

Now compute $(\sigma \wedge \tau)(\xi_1, \ldots, \xi_{k+l})$:
$$(\sigma \wedge \tau)(\xi_1, \ldots, \xi_{k+l}) = \frac{1}{l! \, k!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi) \, \sigma(\xi_{\pi(1)}, \ldots, \xi_{\pi(l)}) \, \tau(\xi_{\pi(l+1)}, \ldots, \xi_{\pi(l+k)}).$$

Consider the permutation $\rho \in S_{k+l}$ that interchanges the first $k$ and last $l$ positions: for $1 \leq i \leq l$, $\rho(i) = k+i$, and for $l+1 \leq i \leq l+k$, $\rho(i) = i-l$. This permutation has sign $\operatorname{sgn}(\rho) = (-1)^{kl}$, since it requires $kl$ transpositions to bring each of the $k$ elements past each of the $l$ elements.

Reindexing the summation in the definition of $\tau \wedge \sigma$ by composing with $\rho$, we obtain
$$(\tau \wedge \sigma)(\xi_1, \ldots, \xi_{k+l}) = \frac{1}{k! \, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi \circ \rho) \, \tau(\xi_{\pi(\rho(1))}, \ldots, \xi_{\pi(\rho(k))}) \, \sigma(\xi_{\pi(\rho(k+1))}, \ldots, \xi_{\pi(\rho(k+l))}).$$

Since $\operatorname{sgn}(\pi \circ \rho) = \operatorname{sgn}(\pi) \cdot (-1)^{kl}$, and the reindexed sum runs over all of $S_{k+l}$ exactly once, this gives
$$(\tau \wedge \sigma)(\xi_1, \ldots, \xi_{k+l}) = (-1)^{kl} \cdot \frac{1}{k! \, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi) \, \sigma(\xi_{\pi(1)}, \ldots, \xi_{\pi(l)}) \, \tau(\xi_{\pi(l+1)}, \ldots, \xi_{\pi(l+k)})$$
$$= (-1)^{kl} (\sigma \wedge \tau)(\xi_1, \ldots, \xi_{k+l}).$$

Thus $\tau \wedge \sigma = (-1)^{kl} \sigma \wedge \tau$. $\square$

**Remark.** In particular, for 1-forms $\omega, \eta \in \wedge^1(V) = V^*$, we have $\omega \wedge \eta = -\eta \wedge \omega$, and consequently $\omega \wedge \omega = 0$.
