---
role: proof
locale: en
of_concept: prop-if-is-the-transition-function-of-1
source_book: gtm034
source_chapter: "1"
source_section: "004"
---

Proof: If

$$F_n(t) = \sum_{z < \sqrt{n}\sigma t} P_n(0,x),$$

which clearly is a sequence of distribution functions, the proof of P8 will follow from the Lévy continuity theorem, provided we can show that

$$\lim_{n \to \infty} \int_{-\infty}^{\infty} e^{i\lambda t} dF_n(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i\lambda t} e^{-t^2/2} dt = e^{-\lambda^2/2},$$

for all real $\lambda$. To this end let

$$\phi(\theta) = \sum P(0,x) e^{i x\theta}, \quad -\infty < \theta < \infty,$$

be the characteristic function of the random walk, defined in D2. Then a simple calculation yields

$$\phi_n(\lambda) = \int_{-\infty}^{\infty} e^{i\lambda t} dF_n(t) = \phi^n \left( \frac{\lambda}{\sigma \sqrt{n}} \right).$$

In view of P4,

$$\phi \left( \frac{\lambda}{\sigma \sqrt{n}} \right) = 1 - \frac{\lambda^2}{2n} + \frac{\epsilon(\lambda,n)}{n},$$

where, for every fixed $\lambda$, the error term $\epsilon(\lambda,n)$ tends to zero as $n$ tends to infinity. Consequently

$$\lim_{n \to \infty} \int_{-\infty}^{\infty} e^{i\lambda t} dF_n(t) = \lim_{n \to \infty} \left

group. Of course, given any transition function we could artificially increase the dimension of $R$ (by imbedding $R$ in a space of higher dimension) and then extend $P(0,x)$ by defining it to be zero, where it was not previously defined. Therefore it is important to make our terminology absolutely unambiguous. We shall speak of a $d$-dimensional random walk only when $R$ has dimension $d$, and when $P(0,x)$ is defined for all $x$ in $R$. This random walk is then said to be aperiodic if $\bar{R} = R$.

Having pointed out how one can trivially make an aperiodic random walk periodic, by artificially enlarging its state space, we shall now show that it is almost as easy to replace a periodic random walk by an aperiodic one, which retains all properties which could possibly be of any interest. This possibility depends on a simple lemma from linear algebra.
