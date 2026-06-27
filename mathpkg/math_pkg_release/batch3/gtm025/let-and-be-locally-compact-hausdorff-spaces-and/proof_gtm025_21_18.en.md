---
role: proof
locale: en
of_concept: "let-and-be-locally-compact-hausdorff-spaces-and"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.18"
---

Let $\mathcal{R}$ be the family of all sets $E \in M_\mu \times M_\nu$ for which (i) and (ii) hold. We will prove that $\mathcal{R} = M_\mu \times M_\nu$. Suppose that $(E_n)_{n=1}^{\infty} \subset \mathcal{R}$ and write $E = \bigcup_{n=1}^{\infty} E_n$. If $\mu \times \nu(E_{n_0}) = \infty$ for some $n_0$, then (i) is trivial for $E$ and, by (ii), $E_{n_0}$ has compact subsets of arbitrarily large [finite!] measure; hence $E$ is in $\mathcal{R}$. Thus suppose that $\mu \times \nu(E_n) < \infty$ for all $n \in N$. For arbitrary $\varepsilon > 0$ and for each $n \in N$, choose a compact set $F_n \in M_\mu \times M_\nu$ and an open set $U_n \in M_\mu \times M_\nu$ such that $F_n \subset E_n \subset U_n$ and $\mu \times \nu(U_n \cap F_n') < \frac{\vare

regularity of $\mu$ and $\nu$ to select ascending sequences $(C_n)_{n=1}^{\infty}$ and $(D_n)_{n=1}^{\infty}$ of compact sets and descending sequences $(U_n)_{n=1}^{\infty}$ and $(V_n)_{n=1}^{\infty}$ of open sets such that:

$$C_n \subset A \subset U_n \subset X;$$

$$D_n \subset B \subset V_n \subset Y;$$

$$\mu(U_n) - \mu(C_n) < \frac{1}{n};$$

and

$$\nu(V_n) - \nu(D_n) < \frac{1}{n}.$$

Then for each $n \in N$, $U_n \times V_n$ is open, $C_n \times D_n$ is compact, and $C_n \times D_n \subset A \times B \subset U_n \times V_n$. Also we have

$$\mu \times \nu(A \times B) = \mu(A) \cdot \nu(B)$$

$$= \lim_{n \to \infty} [\mu(U_n) \cdot \nu(V_n)] = \lim_{n \to \infty} \mu \times \nu(U_n \times V_n)$$

and

$$\mu \times \nu(A \times B) = \mu(A) \cdot \nu(B)$$

$$= \lim_{n \to \infty} [\mu(C_n) \cdot \nu(D_n)] = \lim_{n \to \infty} \mu \times \nu(C_n \times D_n).$$

Thus $A \times B \in \mathcal{R}$, and so $\mathcal{R}$ contains all measurable rectangles.

To finish the proof that $\mathcal{R} = \mathcal{M}_\mu \times \mathcal{M}_\nu$, we need only to show that $\mathcal{R}$ is closed under complementation. Let $(A_n \times B_n)_{n=1}^{\infty}$ be as above. Define $\mathcal{R}_n = \{E \in \mathcal{R}: E \subset A_n \times B_n\}$. Clearly $\mathcal{R}_n$ is closed under the formation of countable unions. Let $E$ be in $\mathcal

all $n$, and so $E' = \bigcup_{n=1}^{\infty} [E' \cap (A_n \times B_n)] \in \mathcal{R}$. Therefore $\mathcal{R}$ is closed under complementation. Altogether we have proved that $\mathcal{R} = \mathcal{M}_{\mu} \times \mathcal{M}_{\nu}$.

Finally, let $H$ be any set in $\mathcal{M}_{\mu} \times \mathcal{M}_{\nu}$. Then $H = G \cup F$ where $G \in \mathcal{M}_{\mu} \times \mathcal{M}_{\nu}$ and $F \subset E$ for some $E \in \mathcal{M}_{\mu} \times \mathcal{M}_{\nu}$ for which $\mu \times \nu(E) = 0$. If $\mu \times \nu(G) = \infty$, it is clear that (i) and (ii) hold for $H$; thus suppose that $\mu \times \nu(G) < \infty$. Given $\varepsilon > 0$, choose open sets $U$ and $V$ and a compact set $C$ [all in $\mathcal{M}_{\mu} \times \mathcal{M}_{\nu}$] such that $C \subset G \subset U$, $E \subset V$, $\mu \times \nu(U \cap C') < \varepsilon$, and $\mu \times \nu(V) < \varepsilon$. Then we have

$$C \subset H \subset U \cup V$$

and

$$\mu \times \nu(U \cup V) - \mu \times \nu(C) \leq \mu \times \nu(V) + \mu \times \nu(U \cap C') < 2\varepsilon.$$

It follows that

$$\mu \times \nu(U \cup V) < \overline{\mu \times \nu}(H) + 2\varepsilon$$

and

$$\overline{\mu \times \nu}(H) < \mu \times \nu(C) + 2\varepsilon,$$

and so again (i) and (ii) hold for $H$. $\square$

In the following exercises (21.19) and (21.20), the reader

(21.21) Exercise. (a) Let $(X, \mathcal{M}, \mu)$ and $(Y, \mathcal{N}, \nu)$ be $\sigma$-finite measure spaces. Suppose that there exists a set $A \subset X$ such that $A \notin \mathcal{M}$ and suppose that there exists a nonvoid set $B \in \mathcal{N}$ such that $\nu(B) = 0$. Prove that $(X \times Y, \mathcal{M} \times \mathcal{N}, \mu \times \nu)$ is incomplete.

(b) Prove that $(R^2, \mathcal{M}_\lambda \times \mathcal{M}_\lambda, \lambda \times \lambda)$ is an incomplete measure space.

(21.22) Exercise. For each of the functions $f$ on $R \times R$ defined by the following formulas, compute $\int_0^1 \int_0^1 f(x,y) dx dy, \int_0^1 \int_0^1 f(x,y) dy dx, \int_0^1 \int_0^1 |f(x,y)| dx dy,$ and $\int_0^1 \int_0^1 |f(x,y)| dy dx$:

(a) $f(x,y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$;

(b) $f(x,y) = \begin{cases} \frac{1}{(x - \frac{1}{2})^3} & \text{for } 0 < y < \left|x - \frac{1}{2}\right|, \\ 0 & \text{otherwise}; \end{cases}$

(c) $f(x,y) = \frac{x - y}{(x^2 + y^2)^{3/2}}$;

(d) $f(x,y) = \frac{1}{(1 - xy)^p}$, where $p > 0$.

Compare your findings with (21.13).

(21.23) Exercise. Let $(X, \mathcal{M}, \mu)$ be a $\sigma$-finite measure space. Let $f$ be a nonnegative, extended real-valued, $\mathcal{M}$-measurable function

(21.26) Exercise. (a) Let $I = [0, 1]$. Suppose that $E \subset I \times I$ is such that $\lambda(E_x) = \lambda(I \cap (E^y)') = 0$ for all $x, y \in I$. Prove that $E$ is not $\mathcal{M}_\lambda \times \mathcal{M}_\alpha$-measurable.

(b) Prove that sets $E$ as described in part (a) exist. [Let $\Delta$ be the least ordinal number such that $\bar{P}_\Delta = \mathbb{c}$ [see (4.47) and (4.48)]. Let $\alpha \rightarrow x_\alpha$ be any one-to-one mapping of $P_\Delta$ onto $I$. Define $E = \{(x_\alpha, x_\beta) : \beta < \alpha < \Delta\}$. Then $\bar{E}_x < \mathbb{c}$ and $\overline{I \cap (E^y)'} < \mathbb{c}$ for all $x, y \in I$. If we accept the continuum hypothesis (4.50), then all of these sets are countable. In any case, it follows from (10.30), (6.66), and (6.65) that if these sets are measurable, then they have measure zero.]

(21.27) Exercise. Prove that there exists a subset $S$ of $I \times I$ $[I = [0, 1]]$ such that $\bar{S}_x \leq 1$ and $\bar{S}^y \leq 1$ for all $x, y \in I$, but $S \notin \mathcal{M}_\lambda \times \mathcal{M}_\alpha$. [Supply the many missing details in the following outline. Let $\mathcal{F}$ be the family of all compact sets $F \subset I \times I$ such that $\lambda \times \lambda(F) > 0$. Let $\Delta$ be as in (21.26) and let $\alpha \rightarrow F_\alpha$ be a one-to-one mapping of $P_\Delta$ onto $\mathcal{F}$. Choose $(x_0,

The following theorem describes the behavior of absolute continuity and singularity under the formation of product measures.
