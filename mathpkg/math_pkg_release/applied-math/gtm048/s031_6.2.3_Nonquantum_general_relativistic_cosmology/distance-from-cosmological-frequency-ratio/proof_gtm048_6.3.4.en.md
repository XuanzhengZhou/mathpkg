---
role: proof
locale: en
of_concept: distance-from-cosmological-frequency-ratio
source_book: gtm048
source_chapter: "6"
source_section: "6.3.4"
---

By Section 6.0.3, we have $d = (u^4 z)^{2/3} \delta(x, z)$, where $\delta$ is the notation of Section 6.0.12. For any isometry $\psi$ we know that $u^4 \circ \psi = u^4$, $\delta(\psi x, \psi z) = \delta(x, z)$, and $\iota(\psi x, \psi z) = \iota(x, z)$ (Section 6.0). It thus suffices to prove the proposition for the case where $x$ and $z$ lie on the standard light signal of Example 5.2.2.

In that case we determine the quantities via:

\begin{itemize}
\item[(d)] $u^4 z = 2t/3$ (Section 6.3.3).
\item[(e)] $u^4 x = \iota^{-3/2} u^4 z$ (Proposition 6.0.8).
\item[(f)] $\delta(x, z) = 3\bigl[(u^4 z)^{1/3} - (u^4 x)^{1/3}\bigr]$ (Exercise 5.4.5a).
\end{itemize}

Thus
\begin{align*}
d &= (u^4 z)^{2/3} \delta(x, z) \\
  &= (2t/3)^{2/3} \cdot 3\bigl[(2t/3)^{1/3} - \iota^{-1/2}(2t/3)^{1/3}\bigr] \\
  &= 2t\bigl(1 - \iota^{-1/2}\bigr),
\end{align*}
as claimed in (a).

The image of $\iota$ is $(1, \infty)$ by Lemma 6.0.10. The function $d(\iota) = 2t(1 - \iota^{-1/2})$ is increasing on $(1, \infty)$ with $\lim_{\iota \to 1^+} d(\iota) = 0$ and $\lim_{\iota \to \infty} d(\iota) = 2t$. Thus $\operatorname{range}(d) = (0, 2t)$.

Part (b) follows directly from (d) and (e):
$$u^4 z - u^4 x = u^4 z - \iota^{-3/2} u^4 z = \frac{2t}{3}\bigl(1 - \iota^{-3/2}\bigr).$$

Part (c) follows from the fact that the functions of $\iota$ in (a) and (b) are analytic for $\iota \in (0, \infty)$ and can therefore be approximated by Taylor series. For $\iota - 1 \ll 1$, expanding $1 - \iota^{-1/2} \approx \frac{1}{2}(\iota - 1)$ and $1 - \iota^{-3/2} \approx \frac{3}{2}(\iota - 1)$ gives $d \approx t(\iota - 1)$ and $u^4 z - u^4 x \approx t(\iota - 1)$.
