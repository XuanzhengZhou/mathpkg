---
role: proof
locale: en
of_concept: stickelberger-ideal-congruence
source_book: gtm059
source_chapter: "2"
source_section: "Integral Stickelberger Ideals"
---

Let $\psi = \omega^{k-n}$. Choose $c$ to be a primitive root modulo $p$, so that $c^k \neq 1 \pmod{p}$. By Theorem 2.3 we have

$$\frac{1}{k} B_k \equiv \frac{1}{1-c^k} \int_{\mathbf{Z}_p^*} x^{k-1} \, dE_{1,c}(x) \pmod{p}.$$

By Theorem 2.4, with the character $\psi = \omega^{k-n}$, we have

$$\frac{1}{n} B_{n,\psi} = \frac{1}{1-\psi(c)c^n} \int_{\mathbf{Z}_p^*} \psi(a) a^{n-1} \, dE_{1,c}(a).$$

Now compute the difference:

$$\frac{1}{n} B_{n,\psi} - \frac{1}{k} B_k \equiv \int_{\mathbf{Z}_p^*} x^{k-1} \left[ \frac{1}{1-\psi(c)c^n} - \frac{1}{1-c^k} \right] dE_{1,c}(x) \pmod{p}$$

because $\psi(a)a^{n-1} \equiv a^{k-1} \pmod{p}$ when $\psi = \omega^{k-n}$.

Since both $1 - \psi(c)c^n$ and $1 - c^k$ are $p$-adic units (as $c$ is a primitive root and $\psi(c) = \omega^{k-n}(c) \equiv c^{k-n} \pmod{p}$), their difference in brackets is $\equiv 0 \pmod{p}$. Hence the integral is $\equiv 0 \pmod{p}$, and the congruence follows.
