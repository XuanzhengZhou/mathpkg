---
role: proof
locale: en
of_concept: ramification-groups-commutator
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

Let $s \in G_{V_q}$ and $t \in G_{V_r}$. Take any $x \in R'$. Since $t \in G_{V_r}$, we have $y = t(x) - x \in \mathfrak{P}^r$. Then
$$s(y) - y = s(t(x)-x) - (t(x)-x) = st(x) - s(x) - t(x) + x.$$
Since $s \in G_{V_q}$ and $y \in \mathfrak{P}^r$, we have $s(y) - y \in \mathfrak{P}^{q+r-1}$ (because $s$ acts as identity modulo $\mathfrak{P}^{q+1}$ on elements of $\mathfrak{P}^r$). Similarly, with $z = s(x) - x \in \mathfrak{P}^q$, we have $t(z) - z = ts(x) - t(x) - s(x) + x \in \mathfrak{P}^{q+r-1}$.

Subtracting these two expressions yields $st(x) - ts(x) \in \mathfrak{P}^{q+r-1}$. Replacing $x$ by $s^{-1}t^{-1}(x)$, we obtain $sts^{-1}t^{-1}(x) - x \in \mathfrak{P}^{q+r-1}$ for every $x \in R'$. Hence $sts^{-1}t^{-1} \in G_{V_{q+r-1}}$.

For the special case $q = r = n$, any commutator of elements in $G_{V_n}$ lies in $G_{V_{2n-1}}$, so the commutator subgroup $[G_{V_n}, G_{V_n}] \subset G_{V_{2n-1}}$.
