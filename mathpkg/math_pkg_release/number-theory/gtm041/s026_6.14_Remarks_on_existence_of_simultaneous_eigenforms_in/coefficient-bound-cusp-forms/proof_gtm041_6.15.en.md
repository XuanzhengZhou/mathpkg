---
role: proof
locale: en
of_concept: coefficient-bound-cusp-forms
source_book: gtm041
source_chapter: "6"
source_section: "6.15"
---

**Proof.** Write $\tau = u + iv$ with $u, v \in \mathbb{R}$, $v > 0$, so that $x = e^{2\pi i \tau} = e^{-2\pi v} e^{2\pi i u}$ and $|x| = e^{-2\pi v} < 1$. By Cauchy's residue theorem the Fourier coefficients admit the integral representation

$$c(n) = \frac{1}{2\pi i} \int_{C(v)} \frac{f(\tau)}{x^{n+1}} \, dx = \int_0^1 f(u + iv) x^{-n} \, du,$$

where $C(v)$ is the circle of radius $e^{-2\pi v}$ centered at $0$.

The series $f(\tau) = \sum_{n=1}^{\infty} c(n) x^n$ converges absolutely for $|x| < 1$. Since $c(0) = 0$ (because $f$ is a cusp form), we may factor out one power of $x$ and estimate

$$|f(\tau)| = |x| \left| \sum_{n=1}^{\infty} c(n) x^{n-1} \right| \leq |x| \sum_{n=1}^{\infty} |c(n)| |x|^{n-1} \leq C |x|$$

for some constant $C$, whenever $\tau \in H$. In particular $|f(\tau)| \to 0$ as $v \to +\infty$.

Now let $g(\tau) = \operatorname{Im}(\tau) = v$. For any $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma = \mathrm{SL}(2, \mathbb{Z})$ one has the well-known transformation law

$$g(A\tau) = \frac{g(\tau)}{|c\tau + d|^2},$$

hence $g^k(A\tau) = |c\tau + d|^{-2k} g^k(\tau)$. Therefore the function

$$\varphi(\tau) = |f(\tau)| \, g^k(\tau) = |f(\tau)| \, v^k$$

is invariant under the action of $\Gamma$ on $H$. Moreover, $\varphi$ is continuous on the fundamental domain $R_\Gamma$, and the estimate $|f(\tau)| \leq C|x|$ together with $|x| = e^{-2\pi v}$ shows that $\varphi(\tau) = |f(\tau)| v^k \leq C e^{-2\pi v} v^k \to 0$ as $v \to +\infty$. Consequently $\varphi$ is bounded on $R_\Gamma$, and by $\Gamma$-invariance $\varphi$ is bounded on all of $H$; write

$$|\varphi(\tau)| = |f(\tau)| v^k \leq M$$

for all $\tau \in H$. Equivalently,

$$|f(\tau)| \leq M v^{-k}, \qquad \tau \in H.$$

Insert this bound into the integral representation for $c(n)$:

$$|c(n)| \leq \int_0^1 |f(u + iv)| \, |x|^{-n} \, du \leq M v^{-k} |x|^{-n} = M v^{-k} e^{2\pi n v}.$$

This inequality holds for every $v > 0$. Choosing $v = 1/n$ yields

$$|c(n)| \leq M n^k e^{2\pi} = O(n^k),$$

which completes the proof.
