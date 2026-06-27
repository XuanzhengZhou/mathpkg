---
role: proof
locale: en
of_concept: theorem-hilberts-basis-theorem
source_book: gtm029
source_chapter: "VII"
source_section: "1-2"
---

For every power series $P(X_1, \cdots, X_n)$ denote by $r(P)$ the sum of all terms in $P$ which do not have $X_n^s$ as a factor, and by $h(P)$ the factor of $X_n^s$ in $P-r(P)$. In other words we have

(12) $P = r(P) + X_n^s h(P),$

where $r(P), h(P) \in k[[X_1, X_2, \cdots, X_n]]$ and where, furthermore, $r(P)$ is a polynomial in $X_n$, of degree $\leq s-1$, with coefficients in $k[[X_1, X_2, \cdots, X_{n-1}]]$. Note that if the power series ring $k[[X_1, X_2, \cdots, X_n]]$ is thought of as a vector space over the field $k$, then both operations $r$ and $h$ are linear transformations in that vector space. By the definition of the integer $s$, $h(F)$ is a unit in $k[[X_1, X_2, \cdots, X_n]]$ (see Theorem 2), and $r(F)$, regarded as a polynomial in $X_n$, has all its coefficients in the maximal ideal of the ring $k[[X_1, X_2, \cdots, X_{n-1}]]$. We shall denote this maximal ideal by $m$.

The problem of finding power

We set

(14) $M = -r(F)[h(F)]^{-1}$.

Then, by (13), $Ur(F) = -MV$, and (11b) is equivalent to

(11c) $h(G) = -h(MV) + V$.

For every power series $P$, denote by $m(P)$ the power series $h(MP)$. Notice that $m$ is again a linear operation on power series. Furthermore, if $P$, considered as a power series in $X_n$ over $k[[X_1, \cdots, X_{n-1}]]$, has all its coefficients in some power $m^j$ of the maximal ideal $m$, then $m(P)$ has all its coefficients in $m^{j+1}$. For convenience we set $H = h(G)$. With these notations condition (11c) may be written as follows:

(11d) $V = H + m(V)$.

Since $m$ is linear, condition (11d) implies that $V = H + m(H + m(V)) = H + m(H) + m^2(V)$, and, by successive applications:

(11e) $V = H + m(H) + m^2(H) + \cdots + m^q(H) + m^{q+1}(V)$,

for any integer $q \geq 0$.

The property of the operation $m$ which we have just pointed out above shows that $m^j(H)$ is at least of order $j$, and $m^{q+1}(V)$ is at least of order $q+1$. Thus the infinite sum $H + m(H) + m^2(H) + \cdots + m^q(H) + \cdots$ converges, and, if a power series $V$ satisfying (11d) exists, it must therefore be the series

(15) $V = H + m(H) + m^2(H) + \cdots + m^q(H) + \cdots$,

and this proves the uniqueness of $V$, whence of $U$ and of the $R_i$.

We now prove that the series $V$ given by (15) satisfies condition (11d). Let us write $V = H

substantial advantage is that the method of majorants is easily applicable to the resolving formula (11e), with the result that if $F$ and $G$ are convergent power series over the field of real or complex numbers, then the series $V, U$ and the $R_i$ are also convergent. To show this we open now a brief digression on the preparation theorem for convergent power series.

In the case of convergent power series over the field $k$ of real or complex numbers, the proof of the Weierstrass preparation theorem runs as follows. We recall† that a power series

$$F(X_1, \cdots, X_n) = \sum_q a_{q_1, \cdots, q_n} X_1^{q_1} \cdots X_n^{q_n}$$

is said to be convergent if there exists a neighborhood $N$ of the origin in $k^n$ such that the series $\sum_q a_{q_1, \cdots, q_n} z_1^{q_1} \cdots z_n^{q_n}$ is absolutely convergent for every $(z_1, \cdots, z_n) \in N$. Then there exist positive real numbers $\mu$ and $\rho$ such that $|a_{q_1, \cdots, q_n}| \leq \mu \rho^{-(q_1 + \cdots + q_n)}$. Conversely, the existence of two such real numbers implies that $\sum_q a_{q_1, \cdots, q_n} z_1^{q_1} \cdots z_n^{q_n}$ converges in the neighborhood $N$ of 0 defined by $|z_i| < \rho$ ($i = 1, \cdots, n$). It is easily seen that the convergent power series in $k[[X_1, \cdots, X_n]]$ form a subring of $k[[X_1, \cdots, X_n]]$, and that a convergent power series with a constant term $\neq 0$ admits as inverse a convergent power series. A series $\sum_q a_{q_1, \cdots, q_n} X_1^{q_1} \cdots X_n^{q_n}$ with real positive coefficients is said to be a

H by majorants $M'$ and $H'$, and assuming that $M'$ is of positive order, then the power series

$$V' = H' + m'(H') + \cdots + m'^q(H') + \cdots$$

(where the operation $m'$ is defined by $m'(P) = h(M'P)$) is a majorant of $V$. We may take

$$H'_1 = \frac{\mu}{\left(1 - \frac{X_1}{\rho}\right) \cdots \left(1 - \frac{X_n}{\rho}\right)},$$

$$M' = \frac{\mu(X_1 + \cdots + X_{n-1})}{\left(1 - \frac{X_1}{\rho}\right) \cdots \left(1 - \frac{X_n}{\rho}\right)}.$$

(For the second one we write $M = N_1X_1 + \cdots + N_{n-1}X_{n-1}$ and we major separately each one of the series $N_i$.) Instead of $H'_1$, we take as majorant of $H$ the series

$$H' = \frac{\mu}{\left(1 - \frac{X_1}{\rho}\right) \cdots \left(1 - \frac{X_{n-1}}{\rho}\right)} \varphi\left(\frac{X_n}{\rho}\right),$$

where $\varphi(X)$ is a series in one variable, majoring $\frac{1}{1-X}$ and enjoying properties which we are going to describe.

We notice that the operation $m'$ is not only additive, but linear over $k[[X_1, \cdots, X_{n-1}]].$ We thus have

$$m'(H') = \frac{\mu^2(X_1 + \cdots + X_{n-1})}{\left(1 - \frac{X_1}{\rho}\right)^2 \cdots \left(1 - \frac{X_{n-1}}{\rho}\right)^2} h\left(\varphi\left(\frac{X_n}{\rho}\right)\right)/\left(1 - \frac{X_n}{\rho}\right).$$

We set $X = \frac{

We take $\lambda = 2^{s+1}$, and notice that the denominator $1 - 2^{s+1}X^s + 2^{s+1}X^{s+1}$ factors into $(1 - 2X)(1 + 2X + 2^2X^2 + \cdots + 2^{s-1}X^{s-1} - 2^sX^s)$. The second factor takes the value 1 for $X = 0$ and $-1$ for $X = 1$. Therefore it admits a positive root $1/\alpha$ ($\alpha > 1$). Thus the denominator $1 - 2^{s+1}X^s + 2^{s+1}X^{s+1}$ may be written in the form $(1 - 2X)(1 - \alpha X)$ $\bar{P}_{s-1}(X)$, where $\bar{P}_{s-1}(X)$ is a polynomial of degree $s-1$. We choose $P_{s-1}(X)$ to be just this polynomial $\bar{P}_{s-1}(X)$. We then have

$$\varphi(X) = \frac{1-X}{1-2X} \cdot \frac{1}{1-\alpha X},$$

and thus for this choice of $\varphi(X)$ we will have $h(\varphi(X)/(1-X)) = 2^{s+1}\varphi(X)$. As it is a rational function, this power series $\varphi(X)$ is convergent. Since

$$\frac{1-X}{1-2X} = \frac{1}{2} + \frac{1}{2} \frac{1}{1-2X}$$

the power series expansion of $\varphi(X)$ is

$$\frac{1}{2}(2 + 2X + 4X^2 + \cdots + 2^nX^n + \cdots)(1 + \alpha X + \cdots + \alpha^nX^n + \cdots).$$

Except for the constant term (which is equal to 1), the coefficient of $X^n$ is $\alpha^n + \alpha^{n-1} + 2\alpha^{n-2} + \cdots + 2^{n-1

Hence

$$V' = A\varphi(X) \frac{1}{1-2^{s+1}B}$$

$$= \frac{\mu\varphi(X_n/\rho)}{\left(1-\frac{X_1}{\rho}\right) \cdots \left(1-\frac{X_{n-1}}{\rho}\right) \left(1-\frac{2^{s+1}\mu(X_1+\cdots+X_{n-1})}{(1-X_1/\rho) \cdots (1-X_{n-1}/\rho)}\right)}$$

$$= \frac{\mu \cdot \left(1-\frac{X_n}{\rho}\right)}{\left(1-2\frac{X_n}{\rho}\right) \left(1-\alpha\frac{X_n}{\rho}\right) \left[ \left(1-\frac{X_1}{\rho}\right) \cdots \left(1-\frac{X_{n-1}}{\rho}\right) - 2^{s+1}\mu(X_1+\cdots+X_{n-1}) \right]}.$$

Since $V'$ is a rational function, this is a convergent power series. This proves the preparation theorem in the case of convergent power series.

A power series $F(X_1, X_2, \cdots, X_n)$ which contains a term $cX_n^s$ which is a power of $X_n$, with non-zero coefficient $c$, is said to be regular in $X_n$. To say that $F(X_1, X_2, \cdots, X_n)$ is regular in $X_n$ is equivalent to saying that $F(0, 0, \cdots, 0, X_n)$ is different from zero.
