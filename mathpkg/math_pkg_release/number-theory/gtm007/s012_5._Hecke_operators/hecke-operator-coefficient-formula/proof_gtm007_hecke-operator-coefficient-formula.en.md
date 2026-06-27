---
role: proof
locale: en
of_concept: hecke-operator-coefficient-formula
source_book: gtm007
source_chapter: "VII"
source_section: "5.3"
---
By definition,
$$T(n)f(z) = n^{2k-1} \sum_{\substack{ad = n, a \geq 1 \\ 0 \leq b < d}} d^{-2k} \sum_{m \in \mathbf{Z}} c(m) e^{2\pi i m(az + b)/d}.$$
Interchanging the sums and using that $\sum_{0 \leq b < d} e^{2\pi i m b/d}$ equals $d$ if $d \mid m$ and $0$ otherwise, we obtain
$$T(n)f(z) = n^{2k-1} \sum_{\substack{ad = n, a \geq 1}} d^{-2k} \sum_{m \in \mathbf{Z}, d \mid m} d \cdot c(m) e^{2\pi i m a z/d}.$$
Writing $m = d m'$, the sum over $m$ becomes $\sum_{m' \in \mathbf{Z}} d \cdot c(d m') e^{2\pi i a m' z}$. Since $ad = n$, we have $n^{2k-1} = (ad)^{2k-1}$. The power of $d$ simplifies: $n^{2k-1} d^{-2k} d = a^{2k-1} d^{2k-1} d^{-2k+1} = a^{2k-1}$. Thus
$$T(n)f(z) = \sum_{\substack{ad = n, a \geq 1}} a^{2k-1} \sum_{m' \in \mathbf{Z}} c(d m') e^{2\pi i a m' z}.$$
Now group terms by the index $m = a m'$ in the $q$-expansion. The coefficient $\gamma(m)$ of $q^m$ receives a contribution $a^{2k-1} c(d m')$ whenever $a m' = m$ and $ad = n$. With $m' = m/a$ and $d = n/a$, this is non-zero only when $a \mid m$ and $a \mid n$, i.e. $a \mid (n,m)$. Substituting $d = n/a$, we have $c(d m') = c((n/a)(m/a)) = c(mn/a^2)$. Hence
$$\gamma(m) = \sum_{\substack{a \mid (n,m) \\ a \geq 1}} a^{2k-1} c\left(\frac{mn}{a^2}\right).$$
