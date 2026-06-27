---
role: proof
locale: en
of_concept: thm-1
source_book: gtm095
source_chapter: "3"
source_section: "6"
---

# Proof of Theorem 1 (Equivalent Characterizations of Weak Convergence)

**Theorem 1.** Let $P, P_1, P_2, \ldots$ be probability measures on a metric space $(E, \mathcal{E}, \rho)$. The following statements are equivalent:

(I) $P_n \xrightarrow{w} P$ (weak convergence),

(II) $\limsup_n P_n(F) \leq P(F)$ for every closed set $F$,

(III) $\liminf_n P_n(G) \geq P(G)$ for every open set $G$,

(IV) $P_n \Rightarrow P$ (convergence in general: $P_n(A) \to P(A)$ for every Borel set $A$ with $P(\partial A) = 0$).

*Proof.* We establish the chain of implications (I) $\Rightarrow$ (II) $\Leftrightarrow$ (III) $\Rightarrow$ (IV) $\Rightarrow$ (I).

---

### (I) $\Rightarrow$ (II)

Let $F$ be a closed set. For $\varepsilon > 0$, define the bounded continuous function

$$f_F^\varepsilon(x) = \left[\,1 - \frac{\rho(x, F)}{\varepsilon}\,\right]^+,$$

where $\rho(x, F) = \inf\{\rho(x, y) : y \in F\}$ and $[t]^+ = \max(0, t)$. Observe that $f_F^\varepsilon$ takes values in $[0, 1]$, equals $1$ on $F$, and vanishes outside the $\varepsilon$-neighborhood $F^\varepsilon = \{x : \rho(x, F) < \varepsilon\}$. Moreover, $f_F^\varepsilon$ is continuous because the distance function $\rho(\cdot, F)$ is continuous.

Since $f_F^\varepsilon$ is bounded and continuous, by (I) we have

$$\lim_{n \to \infty} \int_E f_F^\varepsilon \, dP_n = \int_E f_F^\varepsilon \, dP.$$

Now $I_F(x) \leq f_F^\varepsilon(x)$ for all $x$, so

$$P_n(F) = \int_E I_F \, dP_n \leq \int_E f_F^\varepsilon \, dP_n.$$

Taking $\limsup$ on both sides,

$$\limsup_n P_n(F) \leq \limsup_n \int_E f_F^\varepsilon \, dP_n = \int_E f_F^\varepsilon \, dP \leq P(F^\varepsilon).$$

As $\varepsilon \downarrow 0$, we have $F^\varepsilon \downarrow F$ (since $F$ is closed), and therefore $P(F^\varepsilon) \downarrow P(F)$. Hence

$$\limsup_n P_n(F) \leq P(F),$$

which proves (II).

---

### (II) $\Leftrightarrow$ (III)

These are equivalent by taking complements. If $G$ is open, then $G^c$ is closed, and

$$\liminf_n P_n(G) = 1 - \limsup_n P_n(G^c) \geq 1 - P(G^c) = P(G),$$

using (II) for the closed set $G^c$. Conversely, (III) $\Rightarrow$ (II) follows by the same complement argument.

---

### (III) $\Rightarrow$ (IV)

Let $A$ be a Borel set with $P(\partial A) = 0$. Denote the interior of $A$ by $A^\circ$ and the closure by $\overline{A}$. Clearly $A^\circ \subseteq A \subseteq \overline{A}$ and $\overline{A} = A^\circ \cup \partial A$ (disjoint up to $P$-null sets). Since $P(\partial A) = 0$, we have $P(A^\circ) = P(\overline{A}) = P(A)$.

Now $A^\circ$ is open and $\overline{A}$ is closed. Applying (III) to $A^\circ$ and (II) to $\overline{A}$,

$$P(A^\circ) \leq \liminf_n P_n(A^\circ) \leq \liminf_n P_n(A) \leq \limsup_n P_n(A) \leq \limsup_n P_n(\overline{A}) \leq P(\overline{A}).$$

Since $P(A^\circ) = P(\overline{A}) = P(A)$, it follows that

$$\lim_{n \to \infty} P_n(A) = P(A),$$

which is (IV).

---

### (IV) $\Rightarrow$ (I)

Let $f : E \to \mathbb{R}$ be bounded and continuous. We must show $\int_E f \, dP_n \to \int_E f \, dP$. Since $f$ is bounded, there exists $M > 0$ such that $|f(x)| \leq M$ for all $x \in E$.

For a probability measure $Q$ on $E$, the set $D_Q = \{t \in \mathbb{R} : Q(f^{-1}\{t\}) > 0\}$ is at most countable (the sets $f^{-1}\{t\}$ are disjoint Borel sets of total $Q$-mass at most $1$). Hence for $P$ and all $P_n$, the union $D = \bigcup_{n=1}^{\infty} D_{P_n} \cup D_P$ is still at most countable, so we can choose a decomposition of $[-M, M]$ avoiding $D$.

Choose $k \geq 1$ and points $-M = t_0 < t_1 < \cdots < t_k = M$ with $t_i \notin D$ for $i = 0, 1, \ldots, k$. Define the sets

$$B_i = \{x \in E : t_i \leq f(x) < t_{i+1}\}, \qquad 0 \leq i \leq k-1.$$

The function $f$ is continuous, and the preimage under a continuous map of an open interval is open; therefore $B_i$ is contained in an open set. More precisely, $\partial B_i \subseteq f^{-1}\{t_i\} \cup f^{-1}\{t_{i+1}\}$. Since $t_i, t_{i+1} \notin D$, we have $P(\partial B_i) = 0$ and $P_n(\partial B_i) = 0$ for all $n$. By (IV),

$$\lim_{n \to \infty} P_n(B_i) = P(B_i) \qquad \text{for each } i = 0, \ldots, k-1.$$

Now estimate the difference between integrals of $f$ and Riemann sums:

$$\left| \int_E f \, dP_n - \int_E f \, dP \right| \leq \underbrace{\left| \int_E f \, dP_n - \sum_{i=0}^{k-1} t_i P_n(B_i) \right|}_{\text{(A)}} + \underbrace{\left| \sum_{i=0}^{k-1} t_i P_n(B_i) - \sum_{i=0}^{k-1} t_i P(B_i) \right|}_{\text{(B)}} + \underbrace{\left| \sum_{i=0}^{k-1} t_i P(B_i) - \int_E f \, dP \right|}_{\text{(C)}}.$$

Each of (A) and (C) is bounded by $\max_{0 \leq i \leq k-1} (t_{i+1} - t_i)$, because on each $B_i$, $|f(x) - t_i| \leq t_{i+1} - t_i$. Thus

$$\left| \int_E f \, dP_n - \int_E f \, dP \right| \leq 2 \cdot \max_i (t_{i+1} - t_i) + \left| \sum_{i=0}^{k-1} t_i P_n(B_i) - \sum_{i=0}^{k-1} t_i P(B_i) \right|.$$

By (12), the term (B) tends to $0$ as $n \to \infty$. Hence

$$\limsup_n \left| \int_E f \, dP_n - \int_E f \, dP \right| \leq 2 \cdot \max_i (t_{i+1} - t_i).$$

Since the partition can be made arbitrarily fine (the mesh $\max_i (t_{i+1} - t_i)$ can be chosen arbitrarily small while keeping the $t_i$ outside the countable set $D$), we conclude

$$\lim_{n \to \infty} \left| \int_E f \, dP_n - \int_E f \, dP \right| = 0,$$

that is, $\int_E f \, dP_n \to \int_E f \, dP$. Since $f$ was an arbitrary bounded continuous function, $P_n \xrightarrow{w} P$. $\square$

---

**Remark 1.** Theorem 1 holds more generally for arbitrary finite measures $\mu, \mu_n$ (not necessarily probability measures), provided the total masses converge: $\mu_n(E) \to \mu(E)$. The equivalent statements become $(\text{I}^*)$–$(\text{IV}^*)$, where $(\text{II}^*)$ and $(\text{III}^*)$ additionally require $\mu_n(E) \to \mu(E)$.

**Remark 2.** The proof of (IV) $\Rightarrow$ (I) uses the fact that $D$ is at most countable, which is specific to finite measures on a metric space. For arbitrary measures, additional care is needed.
