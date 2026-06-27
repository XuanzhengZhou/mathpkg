---
role: proof
locale: en
of_concept: stably-equivalent-bundles-equal-characteristic-classes
source_book: gtm020
source_chapter: "16"
source_section: "4.3"
---

For some $n$ and $m$, there is an isomorphism between $\xi \oplus \theta^n$ and $\eta \oplus \theta^m$. From this we have the following equalities in the real case:

$$w(\xi) = w(\xi) \cup w(\theta^n) = w(\xi \oplus \theta^n) = w(\eta \oplus \theta^m) = w(\eta) \cup w(\theta^m) = w(\eta) \cup 1 = w(\eta),$$

where we use the Whitney sum formula $w(\xi \oplus \eta) = w(\xi) \cup w(\eta)$, the fact that $w(\theta^n) = 1 = w(\theta^m)$ for trivial bundles, and the isomorphism $\xi \oplus \theta^n \cong \eta \oplus \theta^m$ which implies $w(\xi \oplus \theta^n) = w(\eta \oplus \theta^m)$ by naturality.

Similarly, in the complex case we obtain $c(\xi) = c(\eta)$ using the same argument with the total Chern class and the Whitney sum formula $c(\xi \oplus \eta) = c(\xi) \cup c(\eta)$.
