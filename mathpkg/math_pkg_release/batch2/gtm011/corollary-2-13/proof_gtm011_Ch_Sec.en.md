---
role: proof
locale: en
of_concept: corollary-2-13
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Since Corollary 2.13 applies with $r < R$, Proposition 1.17 implies that

$$|f^{(n)}(a)| \leq \left( \frac{n!}{2\pi} \right) \frac{M}{r^{n+1}} \cdot 2\pi r = \frac{n!M}{r^n}$$

Since $r < R$ is arbitrary, the result follows by letting $r \rightarrow R-.$

We will conclude this section by proving a proposition which is a special case of a more general result which will be presented later in this chapter

frequently used in the later sections.) Let $G$ be an open set and let $\gamma$ be a rectifiable curve in $\mathbb{C}$. Suppose that $\varphi: \{\gamma\} \times G \to \mathbb{C}$ is a continuous function and define $g: G \to \mathbb{C}$ by

$$g(z) = \int_{\gamma} \varphi(w, z) \, dw$$

then $g$ is continuous. If $\frac{\partial \varphi}{\partial z}$ exists for each $(w, z)$ in $\{\gamma\} \times G$ and is continuous then $g$ is analytic and

$$g'(z) = \int_{\gamma} \frac{\partial \varphi}{\partial z}(w, z) \, dw.$$

3. Suppose that $\gamma$ is a rectifiable curve in $\mathbb{C}$ and $\varphi$ is defined and continuous on $\{\gamma\}$. Use Exercise 2 to show that

$$g(z) = \int_{\gamma} \frac{\varphi(w)}{w - z} \, dw$$

is analytic on $\mathbb{C} - \{\gamma\}$ and

$$g^{(n)}(z) = n! \int_{\gamma} \frac{\varphi(w)}{(w - z)^{n+1}} \, dw.$$

4. (a) Prove Abel's Theorem: Let $\sum a_n (z - a)^n$ have radius of convergence 1 and suppose that $\sum a_n$ converges to $A$. Prove that

$$\lim_{r \to 1-} \sum a_n r^n = A.$$

(Hint: Find a summation formula which is the analogue of integration by parts.)

(b) Use Abel's Theorem to prove that $\log 2 = 1 - \frac{1}{2} + \frac{1}{3} - \ldots.$

5. Give the power series expansion of $\log z$ about $z = i$ and find its radius of convergence.

6. Give the power series expansion of $\sqrt{z}$ about $z = 1$ and find its radius of convergence.

7. Use the results of this section to evaluate the following integrals:

(a) $\int_{\gamma} \frac{e^{

8. Use a Möbius transformation to show that Proposition 2.15 holds if the disk $B(a; R)$ is replaced by a half plane.

9. Evaluate the following integrals:

(a) $\int_{\gamma} \frac{e^z - e^{-z}}{z^n} \, dz$ where $n$ is a positive integer and $\gamma(t) = e^{it}, 0 \leq t \leq 2\pi$;

(b) $\int_{\gamma} \frac{dz}{(z - \frac{1}{2})^n}$ where $n$ is a positive integer and $\gamma(t) = \frac{1}{2} + e^{it}, 0 \leq t \leq 2\pi$;

(c) $\int_{\gamma} \frac{dz}{z^2 + 1}$ where $\gamma(t) = 2e^{it}, 0 \leq t \leq 2\pi$. (Hint: expand $(z^2 + 1)^{-1}$ by means of partial fractions);

(d) $\int_{\gamma} \frac{\sin z}{z} \, dz$ where $\gamma(t) = e^{it}, 0 \leq t \leq 2\pi$;

(e) $\int_{\gamma} \frac{z^{1/m}}{(z - 1)^m} \, dz$ where $\gamma(t) = 1 + \frac{1}{2}e^{it}, 0 \leq t \leq 2\pi$.

10. Evaluate $\int_{\gamma} \frac{z^2 + 1}{z(z^2 + 4)} \, dz$ where $\gamma(t) = re^{it}, 0 \leq t \leq 2\pi$, for all possible values of $r, 0 < r < 2$ and $2 < r < \infty$.

11. Find the domain of analyticity of

$$f(z) = \frac{1}{2i} \log \left( \frac{1 + iz}{1 - iz} \right);$$

also, show that $\
