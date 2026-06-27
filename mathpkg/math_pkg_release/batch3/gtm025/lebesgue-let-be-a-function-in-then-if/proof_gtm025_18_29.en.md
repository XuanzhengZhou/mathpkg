---
role: proof
locale: en
of_concept: "lebesgue-let-be-a-function-in-then-if"
source_book: gtm025
source_chapter: "Differentiation"
source_section: "18.29"
---

For brevity we write $f(x + t) + f(x - t) - 2f(x)$ as $\varphi(x, t)$. We also define

$$\Phi(x, t) = \int_0^t |\varphi(x, u)| du$$

and we write the number $\Phi(x, \pi)$ as $a$. Theorem (18.5) shows that $\frac{1}{t} \Phi(x, t) \to 0$ as $t \to 0$ [$x$ is in the Lebesgue set of $f!$]. Consider any $\varepsilon > 0$ and choose $\alpha > 0$ so that $\left| \frac{1}{t} \Phi(x, t) \right| < \varepsilon$ for $|t| \leq \alpha$. Next use (18.27.xi) to choose an integer $n_0 > \frac{1}{\alpha}$ so that

$$n \geq n_0 \text{ and } \alpha \leq t \leq \pi \text{ imply } |K_n(t)| < \frac{\varepsilon}{a + 1

Now suppose that $n \geq n_0$. For $S_3$, (1) implies that

$$S_3 \leq \int_0^\pi |\varphi(x, t)| \frac{\varepsilon}{a+1} dt \leq \frac{\varepsilon}{a+1} a < \varepsilon.$$  (4)

By (18.27.ix) and (2), we have

$$S_1 \leq \int_0^{1/n} |\varphi(x, t)| (n+1) dt = (n+1) \Phi\left(\frac{1}{n}\right) \leq 2n \Phi\left(\frac{1}{n}\right) < 2\varepsilon.$$  (5)

Using (18.27.xi), we have

$$S_2 = \int_1/n^\alpha |\varphi(x, t)| K_n(t) dt \leq \int_1/n^\alpha |\varphi(x, t)| \frac{\pi^2}{n+1} \frac{1}{t^2} dt.$$

We now apply (18.19), with

$$g(t) = -2t^{-3} \text{ and } G(t) = n^2 + \int_1/n^t g(u) du = t^{-2}$$

This yields

$$\int_1/n^\alpha |\varphi(x, t)| t^{-2} dt = \Phi(x, \alpha) \alpha^{-2} - \Phi\left(x, \frac{1}{n}\right) n^2 + 2\int_1/n^\alpha \Phi(x, t) t^{-3} dt.$$

Hence

$$S_2 \leq \frac{\pi^2}{n+1} \Phi(x, \alpha) \frac{1}{\alpha^2} + \frac{2\pi^2}{n+1} \int_1/n^\alpha \Phi(x, t) t^{-3} dt$$

$$\leq \frac{\pi^2}{n+1} \frac{\varepsilon}{\alpha} + \frac{2\pi^2}{n+1} \int_1/n^\alpha \Phi(x, t) t^{-3} dt$$

$$<

(18.31) Exercise. Find a real-valued, absolutely continuous function on $[0, 1]$ that is monotone on no interval. Construct a measurable set $A \subset [0, 1]$ such that $\lambda(A \cap I) > 0$ and $\lambda(A' \cap I) > 0$ for every interval $I \subset [0, 1]$. This can be done by using Cantor-like sets (6.62). Now integrate $\xi_A - \xi_{A'}$.

(18.32) Exercise. Consider a positive real number $\alpha$, and define a function $f_\alpha$ on $[0, 1]$ by

$$f_\alpha(0) = 0,$$

$$f_\alpha(x) = x^\alpha \cos(x^{-1}) \text{ for } 0 < x \leq 1.$$

[Define $x^\alpha$ as $\exp(\alpha \log(x))$ with $\log(x)$ real.]

(a) For what $\alpha$'s does $f_\alpha$ have finite variation?

(b) For what $\alpha$'s is $f_\alpha$ absolutely continuous?

(c) For what $\alpha$'s does $f_\alpha$ have a finite derivative in $]0, 1[$ and a finite right derivative at $0$?

(18.33) Exercise. (a) Let $f$ be a continuous complex-valued function of finite variation on $[a, b]$ and suppose that $f$ is absolutely continuous on $[a, c]$ for all $c$ such that $a < c < b$. Prove that $f$ is absolutely continuous on $[a, b]$.

(b) Show that part (a) fails for some continuous functions on $[a, b]$ having infinite variation on $[a, b]$.

(18.34) Exercise. Prove the following. A complex-valued function on $[a, b]$ is in $\text{Lip}_1([a, b])$ [see the definition in (17.31)] if and only if for every $\varepsilon > 0$ there is a $\delta > 0$ such that for all sequences $([a_k, b_k])_{k=1}^n$ of

(18.37) Exercise. Let $g$ be absolutely continuous on $[a, b]$, let $[\alpha, \beta] = \text{rng} g$, and let $f$ be absolutely continuous on $[\alpha, \beta]$.

(a) Prove that $f \circ g$ is absolutely continuous on $[a, b]$ if and only if $f \circ g$ is of finite variation on $[a, b]$. [Use (18.25).]

(b) Give an example to show that $f \circ g$ need not be absolutely continuous on $[a, b]$.

(18.38) Exercise. Let $f$ be a complex-valued function defined on a closed interval $[\alpha, \beta]$. Prove that $f \in \text{Lip}_1([\alpha, \beta])$ if and only if $f \circ g$ is absolutely continuous on $[a, b]$ for all closed intervals $[a, b]$ and absolutely continuous functions $g$ with $\text{dom} g = [a, b]$ and $\text{rng} g \subset [\alpha, \beta]$.

(18.39) Exercise. (a) Find a strictly increasing function $f \in \mathfrak{C}^r([0, 1])$ for which there is a subset $A$ of $[0, 1]$ such that $\lambda(A) = 0$ and $\lambda(f(A)) = 1$. [Use (18.8).]

(b) Show that a function in $\mathfrak{C}^r([a, b])$ maps every measurable set onto a measurable set if and only if $f$ is an $N$-function. [Hints. If $f$ is an $N$-function and $A$ is a measurable set, write $A$ as a $\sigma$-compact set plus a set of measure zero. If $f$ is not an $N$-function, apply (10.28).]

(18.40) Exercise. By a particular choice of the numbers $t_n$ in (18.26), functions with quite extraordinary properties can be found.

(a) [Ruziewicz-Saks] Let $F$ be as in (

which shows that either $D^+ g(x) \geq 1$ or $D_- g(x) \leq -1$. Thus $g$ is differentiable nowhere on $F$.

(b) Suppose that $\lambda(F) > 0$. Prove that $\sum_{k=1}^{\infty} \varrho_k = \infty$. If $\sum_{k=1}^{\infty} \varrho_k$ were finite, then $g$ would have finite variation and would be differentiable almost everywhere.

(c) Consider Cantor's ternary set $P \subset [0, 1]$, with the notation of (6.62). Write its complementary intervals in the order

$$I_{1,1}, I_{2,1}, I_{2,2}, I_{3,1}, I_{3,2}, I_{3,3}, I_{3,4}, \dots, I_{n,1}, \dots, I_{n,2^{n-1}}, \dots.$$

Compute the sum $\sum_{k=1}^{\infty} \varrho_k$, where $\varrho_k$ is defined as in (a). Why does this not conflict with (b)?

(18.41) Exercise. This exercise is somewhat demanding, but its part (d) is so elegant a result that we hope all readers will work through it. The closed interval $[a, b]$ is fixed throughout.

(a) Let $A$ be a subset of $[a, b]$ of measure 0. There is an absolutely continuous nondecreasing function $\psi$ on $[a, b]$ such that $\psi'(x) = \infty$ for all $x \in A$. [Hints. Let $(U_n)_{n=1}^{\infty}$ be a decreasing sequence of open supersets of $A$ such that $\lambda(U_n) < 2^{-n}$. Let $\varphi_n = \sum_{k=1}^{n} \xi_{U_k}$, and $\varphi = \lim_{n \to \infty} \varphi_n$. Verify that $\varphi \in \mathfrak{L}_1^+([a, b])$ and that $\int_a^b \varphi(t) dt < 1$. Let $\psi(x) = \int_a^x \varphi(t) dt$,

where $\varepsilon$ is a positive number. Show that $D^+ g(x) = \infty$ for $x \in A$ and that $D^+ g(x)$ is positive for $x \in A' \cap B'$. Hence the set $E = \{x : D^+ g(x) \leq 0\}$ is contained in the countable set $B$ and $g(E)$ can accordingly contain no interval. By part (b), $g$ is nondecreasing. As $\varepsilon$ is arbitrary, $f$ too must be nondecreasing.]

(d) [Main result]. Let $f$ be a function in $\mathfrak{C}([a, b])$. Suppose that $f'(x)$ exists and is finite for all but a countable set of $x$ in $]a, b[$ and that $f' \in \mathfrak{L}_1([a, b])$. Then

$$f(x) - f(a) = \int_a^x f'(t) dt \quad \text{for} \quad a \leq x \leq b,$$

and in particular $f$ is absolutely continuous. [A sketch of the proof follows. Consider $f \in \mathfrak{C}^r([a, b])$, the complex case being a trivial extension of this. For each positive integer $n$, define

$$g_n = \max\{f', -n\} \quad \text{and} \quad f_n(x) = \int_a^x g_n(t) dt.$$

Apply (12.24) to prove that

$$\lim_{n \to \infty} f_n(x) = \int_a^x f'(t) dt.$$

Next show that

$$D_+ (f_n - f)(x) = f'_n(x) - f'(x) = g_n(x) - f'(x) \geq 0$$

for almost all $x \in ]a, b[$. Since

$$\frac{f_n(x + h) - f_n(x)}{h} \geq \frac{1}{h} \int_x^{x+h} (-n) dt = -n,$$

one sees that $D_+ (f_n - f)(x)$

other integrals more general than that of Lebesgue is referred to S. Saks, Theory of the Integral, 2nd Ed., Monografie Matematyczne, Warszawa-Lwow, 1937].

(18.43) Exercise: Integral representation of convex functions. Prove the following. Let $I$ be an open interval in $R$ and $f$ a real-valued function on $I$. The function $f$ is convex if and only if there are a nondecreasing function $\varphi$ on $I$ and a point $c \in I$ such that

$$f(x) = \begin{cases} f(c) + \int_{c}^{x} \varphi(t) dt & \text{for } x \geq c, \\ f(c) - \int_{x}^{c} \varphi(t) dt & \text{for } x < c. \end{cases}$$

[The "if" part is a tiny extension of (13.35). For the "only if" part, combine (17.37.b), (18.16), and (17.37.a).]

(18.44) Exercise. Let $f$ be a complex-valued function of period $2\pi$ defined on $R$ such that $f \in \mathfrak{L}_1([-\pi, \pi])$. Suppose that $f$ is continuous at every point of $[a, b]$. Prove that $(\sigma_n f)_{n=1}^{\infty}$ converges to $f$ uniformly on $[a, b]$. [Use uniform continuity and the Fejér kernel as in (18.29).]

(18.45) Exercise. Use the uniform boundedness principle to prove that there exists a real-valued continuous function of period $2\pi$ defined on $R$ whose Fourier series diverges at 0. [Let

$$\mathfrak{P} = \{f \in \mathfrak{C}^r([-\pi, \pi]): f(-\pi) = f(\pi)\}.$$

Then $\mathfrak{P}$, with the uniform norm, is a real Banach space. For each $n \

conclude that $\chi$ is absolutely continuous. These facts imply that $f$, and therefore $\chi$, has a continuous derivative on $R$. Differentiate (iii) with respect to $y$ and then set $y = 0$ to obtain $\chi'(x) = \chi(x)\chi'(0)$. Next set $\chi'(0) = i\alpha$, where $\alpha \in K$. Verify that $\frac{d}{dx}[\chi(x)\exp(-i\alpha x)] = 0$ for all $x \in R$. Conclude that there exists a $\beta \in K$ such that $\chi(x) = \beta\exp(i\alpha x)$ and show that $\chi(0) = 1$ so that $\beta = 1$. Finally, use (i) to prove that $\alpha \in R$. Functions $\chi$ satisfying (i)—(iii) are called characters of $R$.

(b) Let $\psi$ be a real-valued Lebesgue measurable function on $R$ that satisfies (ii) and (iii) above [naturally with $\chi$ replaced by $\psi$]. Prove that $\psi(x) = \exp(\beta x)$ for a real number $\beta$. [It is elementary to show that $\psi(x) > 0$ for all $x$. Use (10.43) to show that $\psi$ is continuous at 0 and use (iii) to show that $\psi$ is continuous everywhere. Now integrate as in part (a).]

(c) Let $\omega$ be a complex-valued Lebesgue measurable function on $R$ that satisfies (ii) and (iii). Prove that $\omega(x) = \exp(\gamma x)$ for some $\gamma \in K$. [Use part (a) on $\omega|\omega|^{-1}$ and part (b) on $\omega| \omega|$.]

(d) Construct examples to show parts (a) and (b) fail if the hypothesis of measurability is dropped. [Use a Hamel basis for $R$ over $Q$ as in (5.46), and note that a discontinuous $\chi$ as in part (a) cannot be Lebesgue measurable; similarly for $\psi$'s as in part (b).]

(18.47)

(v) $\frac{1-r}{1+r} \leq P(r,t) \leq \frac{1+r}{1-r},$

(vi) $\frac{1}{2\pi} \int_{-\pi}^{\pi} P(r,t) dt = 1,$

(vii) $P'(r,t) = -\frac{(1-r^2)2r\sin(t)}{(1+r^2-2r\cos(t))^2}$

[differentiation with respect to $t$].

Consider the function $F(x) = \frac{1}{2\pi} \int_{-\pi}^{x} f(t) dt$, and consider any $x \in ]-\pi, \pi[$ at which the symmetric derivative

$$\lim_{k \downarrow 0} \frac{F(x+h) - F(x-h)}{2h} = D_1 F(x)$$

exists and is finite [see (17.36)]. We wish to prove that

(viii) $\lim_{r \uparrow 1} \alpha_r f(x) = D_1 F(x)$.

In view of (17.36.a) and (18.3), this will prove that $\lim_{r \uparrow 1} \alpha_r f(x) = f(x)$ a.e. on $[-\pi, \pi]$ [note that the set where this occurs contains, perhaps properly, the Lebesgue set for $f(18.5)$]. By adding a constant to $f$ [which disturbs nothing] we may suppose that $F(\pi) = 0$. Applying (18.19) to (ii), we see that

(ix) $\alpha_r f(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P'(r,x-t) dt$

$$= \frac{1}{2\pi} \int_{-\pi}^{x} F(x-t) P'(r,t) dt$$

$$= -\frac{1}{2\pi} \int_{-\pi}^{x} F(x+t) P'(r,t) dt$$

$$= \frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{F(x+t)

so that

(xi) $\frac{1}{2\pi} \int_{-\pi}^{\pi} M(r, t) dt = r$.

Since $1 + r^2 - 2r \cos(t) = |1 - r \exp(it)|^2$, it is easy to see from (x) that for every $\delta \in ]0, \pi[$, the equality

(xii) $\lim_{r \to 1} \left[ \max\{M(r, t): \delta \leq |t| \leq \pi \} \right] = 0$

holds. Finally, for $|t|$ sufficiently small, $\left| \frac{F(x + t) - F(x - t)}{2 \sin t} - D_1 F(x) \right|$ is arbitrarily small. Combining this with (xii), (xi), and (ix), we obtain (viii) forthwith.

(18.48) Exercise: More on $N$-Functions. Let $[a, b]$ be a compact interval in $R$ and let $f$ be a real-valued function defined on $]a, b[$.

(a) Suppose that $E \subset ]a, b[$ and $\beta \geq 0$ are such that $D^+ f(x) \leq \beta$ and $D_- f(x) \geq -\beta$ for every $x \in E$. Prove that $\lambda(f(E)) \leq \beta \lambda(E)$. [Hints. For $\varepsilon > 0$ and $n \in N$, define $E_n = \left\{ x \in E : f(t) - f(x) < (\beta + \varepsilon) |t - x| \text{ for all } t \in ]a, b[ \text{ for which } |t - x| < \frac{1}{n} \right\}$. Then $E_1 \subset E_2 \subset \cdots$ and $\bigcup_{n=1}^{\infty} E_n = E$. For each $n$, let $\{I_{n,k}\}_{k=1}^{\infty}$ be a cover of $E_n$ by intervals of length $< \frac{1}{n}$ such that $\sum

[a, b]. [Hints. For $[c, d] \subset [a, b]$, let $B = \{x \in ]c, d[:f'(x) \text{ exists and is finite}\}$, and let $A = [c, d] \cap B'$. Then $|f(d) - f(c)| \leq \lambda(f([c, d])) = \lambda(f(B)) + \lambda(f(A)) = \lambda(f(B)) \leq \int_{c} |f'(x)| dx$. Recall that $f' \in \mathfrak{L}_1([a, b])$.]1

§ 19. Complex measures and the LEBESGUE-RADON-NIKODYM theorem

In this section we make a further study of the measure-theoretic significance of absolutely continuous functions and functions of finite variation. We begin by examining abstract analogues of some of the classical notions of §§ 17 and 18. We will then use our abstract results to obtain further information about the classical case.

The most useful generalization of the notion of indefinite integral seems to be the following. Let $(X, \mathcal{A}, \mu)$ be an arbitrary measure space and let $f$ be any function in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$. Define $v$ on $\mathcal{A}$ by

$$v(E) = \int_{E} f d\mu$$

for $E \in \mathcal{A}$. Clearly $v$ is complex-valued, $v(\emptyset) = 0$, and $v$ is countably additive (12.32). Thus $v$ enjoys two essential properties of a measure. Since $v$ can assume arbitrary complex values, it is not always a measure in the sense of (10.3). This leads us to define and study signed measures and complex measures.
