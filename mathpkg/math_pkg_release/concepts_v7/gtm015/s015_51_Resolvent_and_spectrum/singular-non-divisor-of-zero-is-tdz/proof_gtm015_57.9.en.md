---
role: proof
locale: en
of_concept: singular-non-divisor-of-zero-is-tdz
source_book: gtm015
source_chapter: "57"
source_section: "57.9"
---

# Proof of Singular non-divisor of zero is a TDZ

**Proof.** Let $T \in \mathcal{L}(E)$ be singular but not a divisor of zero. By (57.1), $T$ is injective and $T(E)$ is dense in $E$. Since $T$ is not invertible, $T(E) \neq E$ (otherwise $T$ would be bijective, hence invertible by the open mapping theorem when $E$ is a Banach space).

Thus $T$ is injective with dense, proper range. For a Banach space $E$, this implies $T$ is a left TDZ. Indeed, if not, $T$ would be bounded below (57.4), making $T(E)$ closed (40.28), contradicting $T(E) \subsetneq E = \overline{T(E)}$.
