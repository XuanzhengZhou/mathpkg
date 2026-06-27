---
role: proof
locale: en
of_concept: modular-function-equal-frequency
source_book: gtm041
source_chapter: "2"
source_section: "2.4"
---

Since $f$ is modular and not constant, the function $g(\tau) = f(\tau) - c$ is also modular for any complex number $c$: it is meromorphic in the upper half-plane $H$, it satisfies $g(A\tau) = f(A\tau) - c = f(\tau) - c = g(\tau)$ for every $A$ in the modular group $\Gamma$, and its Fourier expansion $g(\tau) = f(\tau) - c = \sum_{n=-m}^{\infty} a(n) e^{2\pi i n \tau} - c$ has the required form with at worst a pole at $i\infty$ (the constant term $-c$ simply modifies the coefficient $a(0)$).

Moreover, $g$ is not identically zero because $f$ is not constant. Applying Theorem 2.4 to $g$, the number of zeros of $g$ in the closure of $R_{\Gamma}$ equals the number of poles of $g$ in the closure of $R_{\Gamma}$. But the zeros of $g$ are precisely the solutions of $f(\tau) = c$, and the poles of $g$ are exactly the poles of $f$. Thus, for every $c$, the number of times $f$ takes the value $c$ in the closure of $R_{\Gamma}$ equals the number of poles of $f$ in the closure of $R_{\Gamma}$, which is a fixed number independent of $c$.
