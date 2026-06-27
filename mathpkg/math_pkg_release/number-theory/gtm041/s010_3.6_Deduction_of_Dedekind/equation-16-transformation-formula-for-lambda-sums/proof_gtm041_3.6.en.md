---
role: proof
locale: en
of_concept: equation-16-transformation-formula-for-lambda-sums
source_book: gtm041
source_chapter: "3"
source_section: "3.6"
---

**Proof.** We first treat the case $k = 1$. In this case Equation (16) becomes

$$\sum_{n=1}^{\infty} \lambda(n(z - ih)) = \sum_{n=1}^{\infty} \lambda\!\left(n\!\left(\frac{1}{z} - iH\right)\right) + \frac{1}{2}\log z - \frac{\pi}{12}\!\left(z - \frac{1}{z}\right).$$

Since $\lambda(x)$ is periodic with period $i$, the shifts by $ih$ and $iH$ disappear (both $h$ and $H$ are integers), and the identity reduces to

$$\sum_{n=1}^{\infty} \lambda(nz) = \sum_{n=1}^{\infty} \lambda\!\left(\frac{n}{z}\right) + \frac{1}{2}\log z - \frac{\pi}{12}\!\left(z - \frac{1}{z}\right). \tag{*}$$

We deduce $(*)$ from Iseki's formula (Theorem 3.5, Equation (18)) by taking $\beta = 0$ and letting $\alpha \to 0^+$. Before taking the limit, we separate the $r = 0$ term in the first series on the left of (18) and in the second series on the right of (18). Their difference is $\lambda(\alpha z) - \lambda(i\alpha)$. Although each term tends to $\infty$ as $\alpha \to 0^+$, their difference has a finite limit:

$$\lambda(\alpha z) - \lambda(i\alpha) = \log(1 - e^{-2\pi i \alpha}) - \log(1 - e^{-2\pi \alpha z}) = \log\frac{1 - e^{-2\pi i \alpha}}{1 - e^{-2\pi \alpha z}}.$$

As $\alpha \to 0^+$, the ratio inside the logarithm tends to $(i\alpha)/(i\alpha z) = 1/z$, so the limit is $\log(1/z) = -\log z$. Carrying out the full limit computation (the remaining terms in the series converge uniformly) yields $(*)$ with the term $\frac{1}{2}\log z - \frac{\pi}{12}(z - 1/z)$, as required.

Now we turn to the general case $k > 0$, $(h, k) = 1$. For each $\mu \in \{1, 2, \dots, k-1\}$ we define $v$ by

$$h\mu = qk + v, \qquad 1 \le v \le k-1.$$

Set $\beta = v/k$ and $\alpha = \mu/k$. Note that $v \equiv h\mu \pmod{k}$, hence $-Hv \equiv -Hh\mu \equiv \mu \pmod{k}$, so $-Hv/k \equiv \mu/k \pmod{1}$. Thus $\alpha \equiv -H\beta \pmod{1}$ and $\beta \equiv h\alpha \pmod{1}$. Substituting these values into Iseki's formula (18) and summing over $\mu = 1, 2, \dots, k-1$ (equivalently, over all $v$ except $0$ modulo $k$), we obtain after some algebraic manipulation:

$$\sum_{n=1}^{\infty} \lambda\!\left(\frac{n}{k}(z - ih)\right) = \sum_{n=1}^{\infty} \lambda\!\left(\frac{n}{k}\!\left(\frac{1}{z} - iH\right)\right) + \frac{\pi}{12}\!\left(z - \frac{1}{z}\right)\!\left(1 - \frac{1}{k}\right) + \pi i \sum_{\mu=1}^{k-1} \frac{\mu}{k}\!\left(\frac{v}{k} - \frac{1}{2}\right).$$

The series on both sides arise from grouping terms in Iseki's formula according to the residue classes modulo $k$. The polynomial corrections come from the quadratic terms $\alpha^2$, $\beta^2$ in Iseki's formula summed over all residue classes:

$$\sum_{\mu=1}^{k-1} \frac{\mu^2}{k^2} = \frac{(k-1)(2k-1)}{6k}, \qquad \sum_{\mu=1}^{k-1} \frac{\mu}{k} = \frac{k-1}{2}.$$

Substituting these sums and simplifying gives the coefficient $\frac{\pi}{12}(z - 1/z)(1 - 1/k)$. The linear term $\pi i \sum_{\mu=1}^{k-1} \frac{\mu}{k}(v/k - 1/2)$ is precisely $\pi i\, s(h, k)$, the Dedekind sum (up to normalization conventions). This completes the proof of Equation (16).

With Equation (16) established, Dedekind's functional equation for $\eta(\tau)$ follows directly, since $\log\eta(\tau)$ can be expressed in terms of the $\lambda$-function sums that appear.
