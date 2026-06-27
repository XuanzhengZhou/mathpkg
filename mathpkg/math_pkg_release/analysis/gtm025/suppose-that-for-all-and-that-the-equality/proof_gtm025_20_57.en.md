---
role: proof
locale: en
of_concept: "suppose-that-for-all-and-that-the-equality"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.57"
---

For each fixed $k \in N$ and every $E \in M_k$, we have

$$\eta(E) = \eta_k(E) = (\eta_k)_a(E) = \int_E f_k d\mu = \int_E f_k d\mu .$$

(1)

For $n > k$, $E$ is also in $M_n$, and so (1) can be extended to

$$\eta(E) = \eta_n(E) = (\eta_n)_a(E) = \int_E f_n d\mu .$$

(2)

Take the limit as $n \to \infty$ in (2) and apply (i). This yields

$$\eta(E) = \lim_{n \to \infty} \int_E f_n d\mu = \int_E f_\omega d\mu .$$

(3)

Since $f_\omega$ is a derivative of $\eta_\omega$ with respect to $\mu_\omega$, we have

$$(\eta_\omega)_a(E) = \int_E f_\omega d\mu ,$$

and from (3) we infer that

$$\eta(E) = \eta_\omega(E) = (\eta_\omega)_a(E)$$

(4)

for all $E \in M_k$. Since $k$ is arbitrary, we have proved that $\eta_\omega$ and $(\eta_\omega)_a$ agree on $\bigcup_{k=1}^{\infty} M_k$. By (10.39.c), $\eta_\omega$ is equal to $(\eta_\omega)_a$ on the entire $\sigma$-algebra $M_\omega$.

(20.58) Remark. Condition (20.57.i) is of course just the condition that $\int_E \left( \lim_{n \to \infty} f_n

Proof. We note first that $f$ and $\bar{f}$ are $M_0$-measurable. To see this, write

$$h_n = \lim_{k \to \infty} \left[ \min \{f_n, f_{n+1}, \ldots, f_{n+k}\} \right].$$

It is plain that $h_n$ is $M_n$-measurable, and also that $\lim_{n \to \infty} h_n = f$ [cf. (6.83)].

By (i), all of the functions $h_m, h_{m+1}, \ldots$ are $M_n$-measurable, and since $f = \lim_{n \to \infty} h_{n+m}$, we infer that $f$ is $M_n$-measurable for all $m$, i.e., $f$ is $M_0$-measurable. The proof for $\bar{f}$ is similar.

We borrow the notation $L_\alpha$ and $G_\alpha$ from the proof of (20.56). It is clear that $L_\alpha$ and $G_\alpha$ are in $M_0$. As in the proof of (20.56), it is sufficient to prove (20.56.1) and (20.56.2) for all $A \in M_0$. For each real number $\alpha$, let

$$M_\alpha = \{x \in X : \inf \{f_1(x), f_2(x), \ldots\} < \alpha\}$$

and

$$H_\alpha = \{x \in X : \sup \{f_1(x), f_2(x), \ldots\} > \alpha\}.$$

The sets $M_\alpha$ and $H_\alpha$ are in $M_1$, but need not be in $M_0$. Suppose that the inequalities

$$\eta(M_\alpha \cap A) \leq \alpha \mu(M_\alpha \cap A)$$

and

$$\eta(H_\alpha \cap A) \geq \alpha \mu(H_\alpha \cap A)$$

obtain for all $A \in M_0$. For all $\varepsilon > 0$,

From the definition of $f_p$ and (20.54), we infer that

$$\eta(J_n \cap A) = \sum_{p=1}^{n} \eta(J_{n,p} \cap A)$$

$$= \sum_{p=1}^{n} \eta\left(\{x \in X : f_p(x) \leq \alpha\} \cap J_{n,p} \cap A\right)$$

$$\leq \sum_{p=1}^{n} \alpha \mu\left(\{x \in X : f_p(x) \leq \alpha\} \cap J_{n,p} \cap A\right)$$

$$= \alpha \mu(J_n \cap A).$$

(4)

It is clear that $J_1 \subset J_2 \subset \cdots$ and that $\bigcup_{n=1}^{\infty} J_n = M_\alpha$. Formula (4) and countable additivity imply that

$$\eta(M_\alpha \cap A) \leq \alpha \mu(M_\alpha \cap A),$$

i.e., (1) is verified. The inequality (2) is proved in like manner; we leave it to the reader.

(20.60) Remarks. The limit theorems (20.56) and (20.59) are versions of what probabilists call martingale theorems. Our treatment is taken from a paper of SPARRE ANDERSEN and JESSEN [Danske Vid. Selsk. Mat.-Fys. Medd. 25 (1948), Nr. 5]. The interested reader may also consult J. L. Doob's treatise Stochastic Processes [John Wiley and Sons, New York, 1953], Ch. VII. We have included these limit theorems primarily for their applications to infinite products of measure spaces [see §22]. Several interesting and unexpected results follow immediately from them, however, and we shall now point out a few of these in the form of exercises with copious hints.

(20.61) Exercise: Differentiation on a net. Let $(X, \mathcal{A}, \mu)$ be a $\sigma$-finite measure space. Consider a sequence $(\mathcal{N}_n)_{n

derivative of $\eta_n$ with respect to $\mu_n$. Now apply (20.56) and the definition of derivative in (20.53).]

(b) Let $\varphi$ be a Lebesgue measurable function on $R$ such that $\int_{-a}^{a} |\varphi| d\lambda < \infty$ for all $a > 0$. For every $x \in R$, let $J(n, x)$ be the interval $[k \cdot 2^{-n}, (k + 1) \cdot 2^{-n}]$ that contains $x$ ($n \in N, k \in Z$). Prove that $\lim_{n \to \infty} 2^n \int_{J(n, x)} \varphi d\lambda = \varphi(x)$ for $\lambda$-almost all $x \in R$. [Hint. Apply part (a) with $X = R$, $\mathcal{A} = \mathcal{M}_{\lambda}$, $\mathcal{N}_n = \{[k 2^{-n}, (k + 1) 2^{-n}]\}_{k=-\infty}^{\infty}$, $\eta(A) = \int_{A} \varphi d\lambda$.] Compare this result with (18.3).

(c) Let $\eta$ be a $\sigma$-finite signed measure or a complex measure on $\mathcal{B}(R)$ such that $|\eta|$ and $\lambda$ are mutually singular. Prove that $\lim_{n \to \infty} 2^n \eta(J(n, x)) = 0$ for $\lambda$-almost all $x \in R$. For $\eta$ a signed measure, prove that $\lim_{n \to \infty} 2^n \eta(J(n, x)) = \pm \infty$ on a set $B$ such that $|\eta| (B') = 0$. [Apply part (b), (20.56), and (20.53.iv).] Compare this with the behavior of $\alpha$'s described in (19.60).

(20.62) Exercise: Densities. Notation is as in (20.61). Let $E$ be any set in $\mathcal{A}$. Let $\eta$ be the measure on $\

(a) Prove that $\lim_{n \to \infty} f_n$ is a constant $\mu$-almost everywhere. [Hints. Consider the Lebesgue decomposition $\eta_0 = \eta_{0a} + \eta_{0s}$. Let $B_0 \in \mathcal{M}_0$ be a set such that $\mu_0(B_0) = 0$ and $|\eta_{0s}|(B_0') = 0$. Let $g$ be a Lebesgue-Radon-Nikodým derivative of $\eta_{0a}$ with respect to $\mu_0$. Then for every $E \in \mathcal{M}_0$, we have

$$\eta_{0a}(E) = \int_E g \, d\mu_0 = \int_E \bigcap B_{s'} \, d\mu_0.$$

Since $\mu_0$ assumes only the values 0 and 1, it follows from (12.60) that there is a number $\alpha$ for which $\mu_0\left(\{x \in X : g(x) = \alpha\}\right) = 1$ and so $\lim_{n \to \infty} f_n = \alpha \mu_0$-almost everywhere on $B'_0$ and so $\mu_0$-almost everywhere on $X$.

(b) Prove that the $\alpha$ of part (a) is equal to $\int_X f_1(x) \, d\mu_1(x) = \eta_{1a}(X)$, where $\eta_{1a}$ is the $\mu_1$-absolutely continuous part of $\eta_1$.

(20.64) Exercise. Let $X = [0, 1[$. For each $n \in N$, let $\mathcal{M}_n = \{A \subset X :$ there is an $\mathcal{M}_\lambda$-measurable set $B \subset [0, 2^{-n}[$ such that $A = \bigcup_{k=0}^{2^{n-1}} (B + k2^{-n})$.

Note that $\mathcal{M}_n$ is a $\sigma$-algebra and that $\mathcal{M}_1 \supset \mathcal{M}_2 \

(ii) $\int_A f_n d\mu = \int_A f_{n+1} d\mu$ for all $A \in \mathcal{M}_n$ and all $n \in N$;

(iii) $\int_X f_n d\mu = 1$ for all $n \in N$.

(a) Prove that there is a finitely additive measure $\eta$ on $\bigcup_{n=1}^{\infty} \mathcal{M}_n$ such that

(iv) $\eta(A) = \int_A f_n d\mu$ for all $A \in \mathcal{M}_n$ and all $n \in N$.

(b) Prove by giving an example that $\eta$ need not be countably additive on $\bigcup_{n=1}^{\infty} \mathcal{M}_n$.

(c) Prove that $\lim_{n \to \infty} f_n$ exists and is finite $\mu$-almost everywhere on $X$.

[Hints. Consider the set $\Omega$ of all finitely additive measures $\omega$ on $\bigcup_{n=1}^{\infty} \mathcal{M}_n$ that assume the values 0 and 1 and no other values and vanish for $\mu$-null sets. Make $\Omega$ into a topological space by neighborhoods $\Delta_A = \{\omega \in \Omega : \omega(A) = 1\}$, for $A \in \bigcup_{n=1}^{\infty} \mathcal{M}_n$. Then $\Omega$ is a compact Hausdorff space, and $\mu$ and $\eta$ can be transferred to $\Omega$. Apply (20.56) appropriately and go back to $X$.]

CHAPTER SIX

Integration on Product Spaces

§ 21. The product of two measure spaces

(21.1) Remarks. Suppose that $(X, \mathcal{M}, \mu)$ and $(Y, \mathcal{N}, \nu)$ are two measure spaces. We wish to define a product measure space

$$(X \times Y, \mathcal{M} \times \mathcal{N}, \mu \times \nu),$$

where $\mathcal{M} \times \mathcal{N}$ is an appropriate $\sigma$-algebra of subsets of $X \times Y$ and $\mu \times \nu$ is a measure on $\mathcal{M} \times \mathcal{N}$ for which

$$\mu \times \nu(A \times B) = \mu(A) \cdot \nu(B)$$

whenever $A \in \mathcal{M}$ and $B \in \mathcal{N}$. That is, we wish to generalize the usual geometric notion of the area of a rectangle. We also wish it to be true that

$$\int_{X \times Y} f d\mu \times \nu = \int_{X} \int_{Y} f d\nu d\mu = \int_{Y} \int_{X} f d\mu d\nu,$$

(1)

for a reasonably large class of functions $f$ on $X \times Y$. Thus we want a generalization of the classical formula

$$\int_{[a,b] \times [c,d]} f(x,y) dS = \int_{a}^{b} \int_{c}^{d} f(x,y) dy dx = \int_{c}^{d} \int_{a}^{b} f(x,y) dx dy,$$

which, as we know from elementary analysis, is valid for all functions $f \in \mathfrak{C}([a,b] \times [c,d])$.

In the case that $X$ and $Y$ are locally compact Hausdorff spaces and $\mu$ and $\nu$ are measures constructed as in § 9 from nonnegative linear functionals $I$ and $J$ on $\mathfrak{C}_{00}(X)$ and $\mathfrak{C}_{00}(Y)$ respectively, this program can be carried out by first constructing

and $\beta$ for which

$$|I(\varphi)| \leq \alpha \| \varphi \|_u$$

for all $\varphi \in \mathfrak{C}_{00}(X)$ such that $\varphi(U') \subset \{0\}$ and

$$|J(\psi)| \leq \beta \| \psi \|_u$$

for all $\psi \in \mathfrak{C}_{00}(Y)$ such that $\psi(V') \subset \{0\}$. Consider any $\varepsilon > 0$ and use the Stone-Weierstrass theorem (7.30) to find a function $g$ on $X \times Y$ of the form

$$g(x, y) = \sum_{j=1}^{n} \varphi_j(x) \psi_j(y),$$

where the $\varphi$'s and $\psi$'s satisfy the conditions of the preceding sentence, such that $\|f - g\|_u < \varepsilon$. Since $f^{[y]} - g^{[y]}$ is in $\mathfrak{C}_{00}(X)$ and vanishes on $U'$ for every $y \in Y$, we deduce from (2) that

$$|I_x(f)(y) - \sum_{j=1}^{n} I(\varphi_j) \psi_j(y)| = |I(f^{[y]}) - I(g^{[y]})|$$

$$\leq \alpha \cdot \sup \{|f(x, y) - g(x, y)| : x \in X\}$$

$$\leq \alpha \| f - g \|_u < \alpha \varepsilon$$

for all $y \in Y$. Thus $I_x(f)$ is the uniform limit of a sequence of functions in $\mathfrak{C}_{00}(Y)$ all of which vanish on $V'$; hence $I_x(f) \in \mathfrak{C}_{00}(Y)$ and $I_x(f)$ vanishes on $V'$. Combining this fact with (4), we infer from (3) that

$$|J(I_x(f)) - \sum_{j=1}^{n} I(\varphi_j) J(\psi_j)| = |J(I_x(f) - \sum_{j=1}^{n}

measure spaces include most of those that arise in classical analysis. The subject exhibits several technicalities, which can be an annoyance or a source of fascination: depending upon one's point of view. We proceed to some exact definitions.

(21.2) Definitions. Let $(X, \mathcal{M})$ and $(Y, \mathcal{N})$ be any two measurable spaces. For $A \in \mathcal{M}$ and $B \in \mathcal{N}$, the set $A \times B \subset X \times Y$ is called a measurable rectangle. The smallest $\sigma$-algebra of subsets of $X \times Y$ containing all of the measurable rectangles is denoted by $\mathcal{M} \times \mathcal{N}^1$ and is called the product $\sigma$-algebra. For $E \subset X \times Y$ and $x \in X$, let

$$E_x = \{y \in Y : (x, y) \in E\};$$

similarly, for $y \in Y$ let

$$E^y = \{x \in X : (x, y) \in E\}.$$

These sets are called $X$- and $Y$-sections of $E$, respectively. For a function $f$ on $X \times Y$ and a fixed $x \in X$, let $f[x]$ be the function defined on $Y$ by

$$f[x](y) = f(x, y);$$

similarly, for each $y \in Y$ define $f^{[y]}$ on $X$ by

$$f^{[y]}(x) = f(x, y).$$

These functions are called $X$- and $Y$-sections of $f$, respectively.
