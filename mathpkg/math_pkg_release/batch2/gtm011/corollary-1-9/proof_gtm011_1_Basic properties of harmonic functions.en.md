---
role: proof
locale: en
of_concept: corollary-1-9
source_book: gtm011
source_chapter: "Harmonic Functions"
source_section: "1. Basic properties of harmonic functions"
---

Proof. First take $w = u$ and $v = 0$ in Theorem 1.7. So $w(z) < 0$ for all $z$ or $w(z) \equiv 0$. Now take $w = v$ and $u = 0$ in (1.7); so either $w(z) > 0$ for all $z$ or $w(z) \equiv 0$. Since both of these hold, $w \equiv 0$.

Even though Theorem 1.7 is called the Maximum Principle, it is also a Minimum Principle. For the sake of completeness, a Minimum Principle corresponding to Theorem 1.6 is stated below. It can be proved either by appealing to (1.7) or by considering the function $-u$ and appealing to (1.6).

1.10 Minimum Principle. Let $G$ be a region and suppose that $u$ is a continuous real valued function on $G$ with the MVP. If there is a point $a$ in $G$ such that $u(a) \leq u(z)$ for all $z$ in $G$ then $u$ is a constant function.

Exercises

1. Show that if $u$ is harmonic then so are $u_x = \frac{\partial u}{\partial x}$ and $u_y = \frac{\partial u}{\partial y}$.

2. If $u$ is harmonic, show that $f = u_x - iu_y$ is analytic.

3. Let $p(x, y) = \sum_{k, l=0}^{n} a_{kl} x^k y^l$ for all $x, y$ in $\mathbb{R}$.

Show that $p$ is harmonic iff:

(a) $k(k-1)a_{k, l-2

$$r^2 \left[ \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right] = r^2 \frac{\partial^2 U}{\partial r^2} + r \frac{\partial U}{\partial r} + \frac{\partial^2 U}{\partial \theta^2}$$

$$= r \frac{\partial}{\partial r} \left( r \frac{\partial U}{\partial r} \right) + \frac{\partial^2 U}{\partial \theta^2}.$$

So if $0 \notin G$ then $u$ is harmonic iff

$$r \frac{\partial}{\partial r} \left( r \frac{\partial U}{\partial r} \right) + \frac{\partial^2 U}{\partial \theta^2} = 0.$$

(b) Let $u$ have the property that it depends only on $|z|$ and not arg $z$. That is, $u(z) = \varphi(|z|)$. Show that $u$ is harmonic iff $u(z) = a \log |z| + b$ for some constants $a$ and $b$.

9. Let $u: G \to \mathbb{R}$ be harmonic and let $A = \{z \in G: u_x(z) = u_y(z) = 0\}$; that is, $A$ is the set of zeros of the gradient of $u$. Can $A$ have a limit point in $G$?

10. State and prove a Schwarz Reflection Principle for harmonic functions.

11. Deduce the Maximum Principle for analytic functions from Theorem 1.6.

§2. Harmonic functions on a disk

Before studying harmonic functions in the large it is necessary to study them locally. That is, we must study these functions on disks. The plan is to study harmonic functions on the open unit disk $\{z: |z| < 1\}$ and then interpret the results for arbitrary disks. Of basic importance is the Poisson kernel.
