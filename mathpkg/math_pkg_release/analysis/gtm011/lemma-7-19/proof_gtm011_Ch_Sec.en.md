---
role: proof
locale: en
of_concept: lemma-7-19
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. (a) Let $K$ be a compact subset of the plane. Then $|z| < n$ for all $z$ in $K$ and $n$ sufficiently large. It suffices to show that

$$\lim_{n \to \infty} n \log \left(1 + \frac{z}{n}\right) = z$$

uniformly for $z$ in $K$ by Lemma 5.7. Recall that

$$\log (1 + w) = \sum_{k=1}^{\infty} (-1)^{k-1} \frac{w^k}{k}$$

for $|w| < 1$. Let $n > |z|$ for all $z$ in $K$; if $z$ is any point in $K$ then

$$n \log \left(1 + \frac{z}{n}\right) = z - \frac{1}{2} \frac{z^2}{n} + \frac{1}{3} \frac{z^3}{n^2} - \dots.$$

So

7.20 $n \log \left(1 + \frac{z}{n}\right) - z = z \left[ -\frac{1}{2} \left(\frac{z}{n}\right) + \frac{1}{3} \left(\frac{z}{n}\right)^2 - \dots \right]$;

taking absolute values gives that

$$\left| n \log \left(1 + \frac{z}{n}\right) - z \right| \leq |z| \sum_{k=2}^{\infty} \frac{1}{k} \left| \frac{z}{n} \right|^{k-

Thus

$$n \log \left( 1 - \frac{t}{n} \right) \leq -t;$$

and since exp is a monotone function part (b) is proved.

Proof of Theorem 7.15. Fix $x > 1$ and let $\epsilon > 0$. According to Lemma 7.16 (b) we can choose $\kappa > 0$ such that

$$\int_{\kappa}^{r} e^{-t} t^{x-1} dt < \frac{\epsilon}{4}$$

whenever $r > \kappa$. Let $n$ be any integer larger than $\kappa$ and let $f_n$ be the function defined in Proposition 7.17. Then

$$f_n(x) - \int_{0}^{n} \left( 1 - \frac{t}{n} \right)^n t^{x-1} dt = -\int_{0}^{1/n} \left( 1 - \frac{t}{n} \right)^n t^{x-1} dt + \int_{1/n}^{n} \left[ e^{-t} - \left( 1 + \frac{t}{n} \right)^n \right] t^{x-1} dt$$

Now by Lemma 7.19 (b) and Lemma 7.16 (a)

$$\int_{0}^{1/n} \left( 1 - \frac{t}{n} \right)^n t^{x-1} dt \leq \int_{0}^{1/n} e^{-t} t^{x-1} dt < \frac{\epsilon}{4}$$

for sufficiently large $n$. Also, if $n$ is sufficiently large, part (a) of the preceding lemma gives

$$\left| \left( 1 - \frac{t}{n} \right)^n - e^{-t} \right| \leq \frac{\epsilon}{4M\kappa}$$

for $t$ in $[0, \kappa]$ where $M = \int_{0}^{\kappa} t^{x-1} dt$. Thus

$$\left| \int_{1/n}^{n} \left[ e^{-t} - \left( 1 - \frac{t}{n} \right

for $n$ sufficiently large. That is

$$0 = \lim \left[ f_n(x) - \int_0^n \left( 1 - \frac{t}{n} \right)^n t^{x-1} dt \right]$$

$$= \lim \left[ f_n(x) - \frac{n! n^x}{x(x+1) \ldots (x+n)} \right]$$

$$= f(x) - \Gamma(x).$$

This completes the proof of Theorem 7.15.

As an application of Theorem 7.15 and the fact that $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$ (Exercise 2) notice that

$$\sqrt{\pi} = \int_0^\infty e^{-t} t^{-\frac{1}{2}} dt.$$

Performing a change of variables by putting $t = s^2$ gives

$$\sqrt{\pi} = \int_0^\infty e^{-s^2} s^{-1} (2s) ds$$

$$= 2 \int_0^\infty e^{-s^2} ds$$

That is,

$$\int_0^\infty e^{-s^2} ds = \frac{\sqrt{\pi}}{2}$$

This integral is often used in probability theory.

Exercises

1. Show that $0 < \gamma < 1$. (An approximation to $\gamma$ is .57722. It is unknown whether $\gamma$ is rational or irrational.)

2. Show that $\Gamma(z) \Gamma(1-z) = \pi csc \pi z$ for $z$ not an integer. Deduce from this that $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.

3. Show: $\sqrt{\pi} \Gamma(2z) = 2^{2z-1} \Gamma(z) \Gamma(z+\frac{1}{2})$. (Hint: Consider the function $\Gamma(z) \Gamma(z+\frac{1}{2}) \Gamma(2z)^{-1}$.)

4. Show that $\log \Gamma(z)$ is defined for $z$ in $\mathbb{C} - (-\infty, 0]$ and that

$$\log \Gamma(z) = -

6. Show that

$$\Gamma(z) = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!(z+n)} + \int_{1}^{\infty} e^{-t} t^{z-1} dt$$

for $z \neq 0, -1, -2, \ldots$ (not for $\text{Re } z > 0$ alone).

7. Show that

$$\int_{0}^{\infty} \sin(t^2) dt = \int_{0}^{\infty} \cos(t^2) dt = \frac{1}{2} \sqrt{\frac{1}{2}\pi}.$$

8. Let $u > 0$ and $v > 0$ and express $\Gamma(u) \Gamma(v)$ as a double integral over the first quadrant of the plane. By changing to polar coordinates show that

$$\Gamma(u) \Gamma(v) = 2\Gamma(u+v) \int_{0}^{\pi/2} (\cos \theta)^{2u-1} (\sin \theta)^{2v-1} d\theta.$$

The function

$$B(u, v) = \frac{\Gamma(u) \Gamma(v)}{\Gamma(u+v)}$$

is called the beta function. By changes of variables show that

$$B(u, v) = \int_{0}^{1} t^{u-1} (1-t)^{v-1} dt$$

$$= \int_{0}^{\infty} \frac{t^{u-1}}{(1+t)^{u+v}} dt$$

Can this be generalized to the case when $u$ and $v$ are complex numbers with positive real part?

9. Let $\alpha_n$ be the volume of the ball of radius one in $\mathbb{R}^n$ ($n \geq 1$). Prove by induction and iterated integrals that

$$\alpha_n = 2\alpha_{n-1} \int_{0}^{1} (1-t^2)^{(n-1)/2} dt$$

10. Show that

$$\alpha_n = \frac{\pi^{n/2}}{(n/2)\Gamma(n/2)}$$

where $\alpha_n$ is defined in problem 9. Show that if $n = 2k, k

The Riemann zeta function

(b) Show that $\Psi(1) = -\gamma$.

(c) Show that $\Psi(z+1) - \Psi(z) = \frac{1}{z}$.

(d) Show that $\Psi(z) - \Psi(1-z) = -\pi \cot \pi z$.

(e) State and prove a characterization of $\Psi$ analogous to the Bohr-Mollerup Theorem.

§8. The Riemann zeta function

Let $z$ be a complex number and $n$ a positive integer. Then $|n^z| = |\exp(z \log n)| = \exp(\text{Re } z \log n)$. Thus

$$\sum_{k=1}^{n} |k^{-z}| = \sum_{k=1}^{n} \exp(-\text{Re } z \log k)$$

$$= \sum_{k=1}^{n} k^{-\text{Re } z}$$

So if $\text{Re } z \geq 1 + \epsilon$ then

$$\sum_{k=1}^{n} |k^{-z}| \leq \sum_{k=1}^{n} k^{-(1+\epsilon)}$$;

that is, the series

$$\sum_{n=1}^{\infty} n^{-z}$$

converges uniformly and absolutely on $\{z: \text{Re } z \geq 1 + \epsilon\}$. In particular, this series converges in $H(\{z: \text{Re } z > 1\})$ to an analytic function $\zeta(z)$.
