---
locale: en
of_concept: with-the-above-notation-we-have-v-nzeta-u-v-n1zeta-u
role: proof
source_book: gtm020
source_chapter: 11. Bott Periodicity in the Complex Case
source_section: '2'
---

Using (4.8), we have the following relations in $K(X)$:

$$L^{2n+2}(\zeta, p_{n+1})_+ = L^{2n+2}(\zeta, zp_{n+1})_+ = L^{2n+1}(\zeta, zp_{n})_+ = L^{2n}(\zeta, p_n)_+ \oplus \zeta$$

From this we have

$$v_{n+1}(\zeta, u) = L^{2n+2}(\zeta, p_{n+1})_+ \otimes (\eta^n - \eta^{n+1}) + \zeta \otimes \eta^{n+1}$$

$$= L^{2n}(\zeta, p_n)_+ \otimes (1 - \eta) + \zeta \otimes (\eta^n - \eta^{n+1}) + \zeta \otimes \eta^{n+1}$$

$$= L^{2n}(\zeta, p_n)_+ \otimes (\eta^{n-1} - \eta^n) + \zeta \otimes \eta^n$$

$$= v_n(\zeta, u)$$

This proves the proposition.

5.3 Remarks. In view of (5.2), $v(\zeta, u)$ may be written for $v_n(\zeta, u)$, since $v$ is independent of $n$. If $u'$ is a second clutching map near $u$, the line segment joining $p_n = z^n f_n$ to $q_n = z^n g_n$ is a homotopy of clutching maps, where $f_n$ approximates $u$ and $g_n$ approximates $u'$. Consequently, we have $v(\zeta, u) = v(\zeta, u')$ and $v(\xi)$ equal to $v(\

$$\mu v(\xi) = [L^{2n}(\zeta, p_n)_+, z^{1-n}] - [L^{2n}(\zeta, p_n)_+, z^{-n}] + [\zeta, z^{-n}]$$
$$= [L^{2n}(\zeta), L^{2n}(p_n)] \otimes \eta^n - [L^{2n}(\zeta, p_n)_-, 1] \otimes \eta^n - [L^{2n}(\zeta, p_n)_+, 1] \otimes \eta^n$$
$$+ [\zeta, z^{-n}] \quad \text{by (a)}$$
$$= 2n(\zeta \otimes \eta^n) + [\zeta, z^{-n}p_n] - [L^{2n}(\zeta), 1] \otimes \eta^n + \zeta \otimes \eta^n \quad \text{by (b)}$$
$$= [\zeta, z^{-n}p_n(x, z)]$$
$$= \xi$$

This proves the complex periodicity theorem.

As a corollary of the periodicity theorem, we can calculate $\tilde{K}(S^m)$.
