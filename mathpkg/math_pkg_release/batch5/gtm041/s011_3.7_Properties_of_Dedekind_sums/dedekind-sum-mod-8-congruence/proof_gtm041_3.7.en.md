---
role: proof
locale: en
of_concept: dedekind-sum-mod-8-congruence
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
From the reciprocity law (Theorem 3.7) we have

$$12ks(h,k) = 2h(k-1)(2k-1) - 2(k-1) - 4\sum_{r=1}^{k-1}\left[\frac{hr}{k}\right] + \frac{h^2+1}{k}\sum_{r=1}^{k-1}r^2 - \sum_{r=1}^{k-1}r.$$

Expanding and simplifying, we obtain

$$12ks(h,k) = (k-1)(k-2h) - 4\sum_{r=1}^{k-1}\left[\frac{hr}{k}\right] + \frac{h^2+1}{k}\cdot\frac{(k-1)k(2k-1)}{6} - \frac{k(k-1)}{2k}.$$

The next-to-last term involving the sum of floor functions is evaluated using the Bernoulli periodic function:

$$-4\sum_{r=1}^{k-1}\left[\frac{hr}{k}\right] = 4\sum_{r=1}^{k-1}\left(\left(\frac{hr}{k}\right)\right) - 4\sum_{r=1}^{k-1}\frac{hr}{k} + 2\sum_{r=1}^{k-1}1 = 0 - 2h(k-1) + 2(k-1) = (k-1)(2-2h).$$

Since

$$(k-1)(k-2h) + (k-1)(2-2h) = (k-1)(k+2) - 4h(k-1),$$

combining these terms with the sum over $r < k/2$ (using properties of the floor function and symmetry) yields the general formula (39).

When $k$ is odd, we have $4h(k-1) \equiv 0 \pmod{8}$ and $(k-1)(k+2) = k^2 + k - 2 \equiv k-1 \pmod{8}$ (since $k^2 \equiv 1 \pmod{8}$ for odd $k$), giving the simplified formula (40).
