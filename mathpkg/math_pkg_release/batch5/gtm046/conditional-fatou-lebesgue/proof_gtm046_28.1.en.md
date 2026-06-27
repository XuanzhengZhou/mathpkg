---
role: proof
locale: en
of_concept: conditional-fatou-lebesgue
source_book: gtm046
source_chapter: "VIII"
source_section: "28.1"
---

**Proof.** Let $Y$ and $Z$ be integrable random variables. Assume $Y \leq X_n$ a.s. for all $n$ (or $X_n \leq Z$ a.s. for all $n$). Define

$$Y_n = \inf_{k \geq n} X_k, \quad Z_n = \sup_{k \geq n} X_k.$$

Then $Y_n \uparrow \liminf X_n$ and $Z_n \downarrow \limsup X_n$. By the conditional monotone convergence theorem applied to $Y_n - Y \geq 0$ (respectively $Z - Z_n \geq 0$), we obtain

$$E^\mathfrak{B}(\liminf X_n) = \lim_n E^\mathfrak{B}Y_n \leq \liminf_n E^\mathfrak{B}X_n \quad \text{a.s.},$$

and similarly for the upper bound,

$$\limsup_n E^\mathfrak{B}X_n \leq E^\mathfrak{B}(\limsup X_n) \quad \text{a.s.}$$

In the case where $|X_n| \leq Z$ a.s. with $Z$ integrable, the conditional dominated convergence theorem follows: since $-Z \leq X_n \leq Z$ a.s., the conditional Fatou-Lebesgue bounds combine to give $E^\mathfrak{B}X_n \to E^\mathfrak{B}X$ a.s. whenever $X_n \to X$ a.s. The proof follows from the monotone convergence assertion exactly as in the nonconditional case.
