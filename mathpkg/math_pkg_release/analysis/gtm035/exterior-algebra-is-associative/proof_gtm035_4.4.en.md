---
role: proof
locale: en
of_concept: exterior-algebra-is-associative
source_book: gtm035
source_chapter: "4"
source_section: "4.4"
---

# Proof of Exterior Algebra is Associative

**Lemma 4.4.** Under $\wedge$, $\mathcal{G}(V)$ is an associative algebra with identity.

## Proof

Recall that $\mathcal{G}(V) = \bigoplus_{k=0}^{N} \wedge^k(V)$ is the direct sum of the spaces of $k$-linear alternating forms on $V$, with $\wedge^0(V) = \mathbb{C}$ and $\wedge^1(V) = V^*$.

The wedge product $\wedge: \wedge^k(V) \times \wedge^l(V) \to \wedge^{k+l}(V)$ is defined as follows: for $\tau \in \wedge^k(V)$ and $\sigma \in \wedge^l(V)$,
$$(\tau \wedge \sigma)(\xi_1, \ldots, \xi_{k+l}) = \frac{1}{k! \, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi) \, \tau(\xi_{\pi(1)}, \ldots, \xi_{\pi(k)}) \, \sigma(\xi_{\pi(k+1)}, \ldots, \xi_{\pi(k+l)}),$$
where $S_{k+l}$ is the symmetric group on $k+l$ elements. This product extends bilinearly to all of $\mathcal{G}(V)$.

Let $\tau \in \wedge^k(V)$, $\sigma \in \wedge^l(V)$, $\rho \in \wedge^m(V)$. We must show
$$(\tau \wedge \sigma) \wedge \rho = \tau \wedge (\sigma \wedge \rho).$$

For vectors $\xi_1, \ldots, \xi_{k+l+m} \in V$, both sides evaluate to
$$\frac{1}{k! \, l! \, m!} \sum_{\pi \in S_{k+l+m}} \operatorname{sgn}(\pi) \, \tau(\xi_{\pi(1)}, \ldots, \xi_{\pi(k)}) \, \sigma(\xi_{\pi(k+1)}, \ldots, \xi_{\pi(k+l)}) \, \rho(\xi_{\pi(k+l+1)}, \ldots, \xi_{\pi(k+l+m)}).$$

This follows from the fact that in both cases the determinant-like expression first antisymmetrizes over each group of variables separately, and then the combined antisymmetrization is equivalent to antisymmetrizing over all $k+l+m$ variables at once.

**Equivalently**, one may verify associativity on a basis. Let $\{e_1^*, \ldots, e_N^*\}$ be a basis for $V^* = \wedge^1(V)$. Any element of $\mathcal{G}(V)$ is a linear combination of wedge products $e_{i_1}^* \wedge \cdots \wedge e_{i_k}^*$. It suffices to verify associativity for such basis elements:
$$(e_{i_1}^* \wedge \cdots \wedge e_{i_k}^*) \wedge (e_{j_1}^* \wedge \cdots \wedge e_{j_l}^*) \wedge (e_{m_1}^* \wedge \cdots \wedge e_{m_p}^*)$$
is unambiguous — by definition, the placement of parentheses does not affect the value of the iterated alternating product.

For $\wedge^0(V) = \mathbb{C}$, the element $1 \in \mathbb{C}$ acts as the identity: $1 \wedge \tau = \tau \wedge 1 = \tau$ for all $\tau \in \mathcal{G}(V)$, by the definition of scalar multiplication.

Therefore $\mathcal{G}(V)$ is an associative algebra with identity under the wedge product $\wedge$. $\square$
