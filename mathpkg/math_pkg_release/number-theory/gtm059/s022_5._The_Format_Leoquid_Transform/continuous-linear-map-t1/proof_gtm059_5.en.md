---
role: proof
locale: en
of_concept: continuous-linear-map-t1
source_book: gtm059
source_chapter: ""
source_section: "5"
---

Any continuous linear map on the space of polynomials (with Leopold norm) extends uniquely by continuity to the Leopold Banach algebra. We shall prove that the linear map

$$\Gamma_a: K[X] \to C(\mathbb{Z}_p, K)$$

with values

$$\Gamma_a\left(\frac{X}{n}\right)(k) = \sum_{j=1}^{n} (-1)^{j-1} \binom{n}{j} \frac{k^{a+j}}{j!}$$

is continuous, and has the required properties. Uniqueness is obvious.

To prove continuity, it suffices to prove that the values $\Gamma_a(\frac{X}{n})(k)$ are bounded. In fact, we shall show that $\Gamma_a(\frac{X}{n})(k)$ is $p$-integral. This will also prove that $\|\Gamma_a(f)\| \le \|f\|_p$.

Fix an integer $n$. Let $m$ range over positive integers satisfying $m \equiv a \pmod{p-1}$. Such integers are dense in $\mathbb{Z}_p$, so it suffices to prove that $\Gamma_a(\frac{X}{n})(m)$ is $p$-integral for such $m$.

If $a \equiv 0 \pmod{p}$, then $m^a$ is $p$-integral for large $m$. If $a \not\equiv 0 \pmod{p}$, write $m = \omega(m) \langle m \rangle$ with the Teichmuller decomposition. Then for $m$ close to $a$ $p$-adically, $|\Gamma_a(\frac{X}{n})(m)|_p \le 1$, establishing the required boundedness and completing the proof.
