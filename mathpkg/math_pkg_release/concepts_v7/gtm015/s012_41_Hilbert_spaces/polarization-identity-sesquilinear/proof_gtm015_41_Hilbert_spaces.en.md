---
role: proof
locale: en
of_concept: polarization-identity-sesquilinear
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Polarization identity and Cauchy–Schwarz for positive sesquilinear forms

Let $\varphi$ be a sesquilinear form on a complex vector space $E$ satisfying $\varphi(x, x) \geq 0$ for all $x \in E$.

---

**Preliminary expansions.**  Expanding by sesquilinearity, for any $x, y \in E$ we have

$$
\begin{aligned}
\text{(a)}&\quad \varphi(x + y, \; x + y) = \varphi(x, x) + \varphi(x, y) + \varphi(y, x) + \varphi(y, y), \\[4pt]
\text{(b)}&\quad \varphi(x - y, \; x - y) = \varphi(x, x) - \varphi(x, y) - \varphi(y, x) + \varphi(y, y), \\[4pt]
\text{(c)}&\quad \varphi(x + iy, \; x + iy) = \varphi(x, x) - i\varphi(x, y) + i\varphi(y, x) + \varphi(y, y), \\[4pt]
\text{(d)}&\quad \varphi(x - iy, \; x - iy) = \varphi(x, x) + i\varphi(x, y) - i\varphi(y, x) + \varphi(y, y).
\end{aligned}
$$

Formulas (b)–(d) are obtained from (a) by replacing $y$ with $-y$, $iy$, and $-iy$ respectively.

---

**(i) Polarization identity — real part.**  Subtract (b) from (a):

$$
\varphi(x+y, x+y) - \varphi(x-y, x-y) = 2\bigl[\varphi(x, y) + \varphi(y, x)\bigr].
$$

Hence

$$
\varphi(x, y) + \varphi(y, x) = \frac{1}{2}\Bigl[\varphi(x+y,\; x+y) - \varphi(x-y,\; x-y)\Bigr].
$$

---

**(ii) Polarization identity — imaginary part.**  Subtract (c) from (d):

$$
\varphi(x-iy, x-iy) - \varphi(x+iy, x+iy) = 2i\bigl[\varphi(x, y) - \varphi(y, x)\bigr].
$$

Hence

$$
\varphi(x, y) - \varphi(y, x) = \frac{i}{2}\Bigl[\varphi(x-iy,\; x-iy) - \varphi(x+iy,\; x+iy)\Bigr].
$$

---

**(iii) Cauchy–Schwarz inequality.**  We prove $|\varphi(x, y)|^2 \leq \varphi(x, x)\,\varphi(y, y)$.

For any $\lambda \in \mathbb{C}$, positivity gives

$$
0 \leq \varphi(x + \lambda y,\; x + \lambda y)
= \varphi(x, x) + \lambda\varphi(x, y) + \lambda^*\varphi(y, x) + |\lambda|^2\varphi(y, y). \tag{1}
$$

If $\varphi(y, y) = 0$, choose $\lambda = \alpha\,\varphi(x, y)^*$ with $\alpha \in \mathbb{R}$.  Then (1) becomes

$$
0 \leq \varphi(x, x) + 2\alpha\,|\varphi(x, y)|^2.
$$

Since this holds for all real $\alpha$, letting $\alpha \to -\infty$ forces $\varphi(x, y) = 0$, and the inequality holds trivially.

If $\varphi(y, y) > 0$, set $\lambda = -\varphi(x, y)/\varphi(y, y)$ in (1).  Then

$$
\begin{aligned}
0 &\leq \varphi(x, x) - \frac{\varphi(x, y)\,\varphi(x, y)^*}{\varphi(y, y)}
      - \frac{\varphi(x, y)^*\,\varphi(y, x)}{\varphi(y, y)}
      + \frac{|\varphi(x, y)|^2}{\varphi(y, y)^2}\,\varphi(y, y) \\[4pt]
  &= \varphi(x, x) - \frac{|\varphi(x, y)|^2}{\varphi(y, y)}
      - \frac{|\varphi(x, y)|^2}{\varphi(y, y)}
      + \frac{|\varphi(x, y)|^2}{\varphi(y, y)} \\[4pt]
  &= \varphi(x, x) - \frac{|\varphi(x, y)|^2}{\varphi(y, y)}.
\end{aligned}
$$

Rearranging gives $|\varphi(x, y)|^2 \leq \varphi(x, x)\,\varphi(y, y)$, as desired.

---

**(iv) Hermiticity criterion.**  Define $\psi(x, y) = \varphi(x, y) - \varphi(y, x)^*$.  Then $\psi$ is again a sesquilinear form.  Observe:

- $\varphi$ is Hermitian $\iff$ $\psi \equiv 0$ $\iff$ $\psi(z, z) = 0$ for all $z \in E$ (since a sesquilinear form vanishing on the diagonal vanishes identically, by polarization).  
- $\psi(z, z) = \varphi(z, z) - \varphi(z, z)^* = 2i\,\mathrm{Im}\,\varphi(z, z)$.

Thus $\psi(z, z) = 0$ for all $z$ precisely when $\varphi(z, z) \in \mathbb{R}$ for all $z$.  Hence $\varphi$ is Hermitian if and only if $\varphi(x, x)$ is real for every $x \in E$.

---

**(v) Positive Hermitian case.**  If $\varphi$ is both positive ($\varphi(x, x) \geq 0$) and Hermitian ($\varphi(y, x) = \varphi(x, y)^*$), then the Cauchy–Schwarz inequality of part (iii) applies directly (the proof of (iii) used only positivity and sesquilinearity; Hermiticity is not required for the inequality itself).  Hence for all $x, y \in E$,

$$|\varphi(x, y)|^2 \leq \varphi(x, x)\,\varphi(y, y).$$

$\square$
