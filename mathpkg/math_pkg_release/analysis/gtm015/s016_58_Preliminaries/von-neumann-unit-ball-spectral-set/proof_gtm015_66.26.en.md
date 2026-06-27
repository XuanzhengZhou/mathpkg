---
role: proof
locale: en
of_concept: von-neumann-unit-ball-spectral-set
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of Unit disk is a spectral set for contractions

Proof. {Note the analogy: in the ‘calculus’ of spectral sets, the closed unit ball $\{T : \|T\| \leq 1\}$ in $\mathcal{L}(H)$ corresponds to the closed unit disc $\Delta_1 = \{\lambda : |\lambda| \leq 1\}$ in $\mathbb{C}$.}

If $\Delta_1$ is a spectral set for $T$, then $\|T\| \leq 1$ results at once from the fact that $t \in \mathbb{C}(t; \Delta_1)$.

Conversely, suppose $\|T\| \leq 1$. Assuming $f \in \mathbb{C}(t)$ and $\|f\|_{\Delta_1} \leq 1$, it is to be shown that $\|f(T)\| \leq 1$ (66.6). Let $f_n$ be a sequence of polynomials such that $\|f_n(T) - f(T)\| \to 0$ (66.25). By (16.4) we have

$$\lim_{n \to \infty} \|f_n(T)\| = \|f(T)\|$$

and

$$\lim_{n \to \infty} \|f_n\|_{\Delta_1} = \|f\|_{\Delta_1} \leq 1;$$

since $\|f_n(T)\| \leq \|f_n\|_{\Delta_1}$ for all $n$ (66.24), passage to the

(iv) If $\sigma$ is a proper, closed subset of $\mathfrak{S}$, then there exists an LFT $f$ such that $f(\sigma)$ is a compact subset of $\mathbb{C}$.
