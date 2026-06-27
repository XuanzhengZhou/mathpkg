---
role: proof
locale: en
of_concept: ramification-groups-commutator
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

Let $y \in \mathfrak{P}^r$ be of the form $y = x_1 \cdots x_r$ with $x_i \in \mathfrak{P}$, since every element in $\mathfrak{P}^r$ is a finite sum of such products. Then

$$s(y) - y = s(x_1 \cdots x_r) - x_1 \cdots x_r = \sum_{j=1}^{r} s(x_1) \cdots s(x_{j-1}) \cdot [s(x_j) - x_j] \cdot x_{j+1} \cdots x_r$$

is an element of $\mathfrak{P}^{q+r-1}$ since $s(x_i) \in \mathfrak{P}$, $x_k \in \mathfrak{P}$, and $s(x_j) - x_j \in \mathfrak{P}^q$.

Similarly, we have $t(z) - z \in \mathfrak{P}^{q+r-1}$ for $z \in \mathfrak{P}^q$.

Now take any $x \in R'$ and set $y = t(x) - x$ and $z = s(x) - x$. Since $y \in \mathfrak{P}^r$ and $z \in \mathfrak{P}^q$, we have

$$s(y) - y = st(x) - s(x) - t(x) + x \in \mathfrak{P}^{q+r-1},$$
$$t(z) - z = ts(x) - t(x) - s(x) + x \in \mathfrak{P}^{q+r-1};$$

whence, by subtraction, $st(x) - ts(x) \in \mathfrak{P}^{q+r-1}$. Replacing $x$ by $s^{-1}t^{-1}(x)$, we get $sts^{-1}t^{-1}(x) - x \in \mathfrak{P}^{q+r-1}$.

Thus the commutator $sts^{-1}t^{-1}$ belongs to $G_{V_{q+r-1}}$.
