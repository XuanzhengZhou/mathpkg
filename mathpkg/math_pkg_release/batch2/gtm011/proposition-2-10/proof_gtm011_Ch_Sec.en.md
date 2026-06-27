---
role: proof
locale: en
of_concept: proposition-2-10
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Fix $z_0$ in $G$ and let $\omega_0 = f(z_0)$. Put $A = \{z \in G: f(z) = \omega_0\}$; we will show that $A = G$ by showing that $A$ is both open and closed in $G$. Let $z \in G$ and let $\{z_n\} \subset A$ be such that $z = \lim z_n$. Since $f(z_n) = \omega_0$ for each $n

Put $g(z) = e^z e^{a-z}$ for some fixed $a$ in $\mathbb{C}$; then $g'(z) = e^z e^{a-z} + e^z (-e^{a-z}) = 0$. Hence $g(z) = \omega$ for all $z$ in $\mathbb{C}$ and some constant $\omega$. In particular, using $e^0 = 1$ we get $\omega = g(0) = e^a$. Then $e^z e^{a-z} = e^a$ for all $z$. Thus $e^{a+b} = e^a e^b$ for all $a$ and $b$ in $\mathbb{C}$. This also gives $1 = e^z e^{-z}$ which implies that $e^z \neq 0$ for any $z$ and $e^{-z} = 1/e^z$. Returning to the power series expansion of $e^z$, since all the coefficients of this series are real we have $\exp \bar{z} = \overline{\exp z}$. In particular, for $\theta$ a real number we get $|e^{i\theta}|^2 = e^{i\theta} e^{-i\theta} = e^0 = 1$. More generally, $|e^z|^2 = e^z e^{\bar{z}} = e^{z+\bar{z}} = \exp (2 \text{ Re } z)$. Thus,

2.13 $|\exp z| = \exp (\text{Re } z)$.

We see, therefore, that $e^z$ has the same properties that the real function $e^x$ has. Again by analogy with the real power series we define the functions $\cos z$ and $\sin z$ by the power series

$$\cos z = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} + \ldots + (-1)^n \frac{z^{2n}}{(2n)!} + \ldots$$

$$\sin z = z - \frac{z^3}{3!} + \frac{z^5}{5!} + \ldots + (-1)^n \frac{z^{2n-1}}{(2

Now let us define log $z$. We could adopt the same procedure as before and let log $z$ be the power series expansion of the real logarithm about some point. But this only gives log $z$ in some disk. The method of defining the logarithm as the integral of $t^{-1}$ from 1 to $x$, $x > 0$, is a possibility, but proves to be risky and unsatisfying in the complex case. Also, since $e^z$ is not a one-one map as in the real case, log $z$ cannot be defined as the inverse of $e^z$. We can, however, do something similar.

We want to define log $w$ so that it satisfies $w = e^z$ when $z = \log w$. Now since $e^z \neq 0$ for any $z$ we cannot define log 0. Therefore, suppose $e^z = w$ and $w \neq 0$; if $z = x + iy$ then $|w| = e^x$ and $y = \arg w + 2\pi k$, for some $k$. Hence

2.17 $\{ \log |w| + i(\arg w + 2\pi k) : k \text{ is any integer} \}$

is the solution set for $e^z = w$. (Note that log $|w|$ is the usual real logarithm.)
