---
role: exercise
locale: en
chapter: "2"
section: "Exercises"
exercise_number: 18
---

Let $T$ be an arbitrary theory in $\mathbf{Set}$, let $S$ be the subsets theory and let $P$ be the double power-set theory. Define $A\sigma: AT \longrightarrow AP$, $p \mapsto$ set of supports of $p$ (as in 1.5.10).

(a) Prove that $\sigma: T \longrightarrow P$ is a theory map if and only if for every $f: A \longrightarrow B$ and mono $i: I \longrightarrow B$ the squares

$$\begin{CD}
IT @>>> AT \\
@VVV @VVV \\
BT @>>> BT
\end{CD}$$

are pullbacks.

(b) Prove that $\sigma: T \longrightarrow P$ is a theory map if and only if $T$ preserves the pullback for each $I \subset B$ and $\chi_{1T}: 2T \longrightarrow 2$ is a $T$-algebra. [Hint: use exercise 8.]

(c) Show that $S$ is a subtheory of $P$ in two ways:

$$AS \xrightarrow{A(\mathrm{prin})} AP, \quad B \mapsto \{S : S \supset B\}$$

$$AS \longrightarrow AP, \quad B \mapsto \{S : S \cap B \neq \emptyset\}$$

[Hint: a complete atomic Boolean algebra is a complete semilattice in two ways.]

(d) Say that $T$ is variabled if $\sigma: T \longrightarrow P$ is a theory map which factors through $\mathrm{prin}$. Show that $\mathrm{var}: T \longrightarrow S$ is a theory map if $T$ is variabled. For finitary $T$, prove that $T$ is variabled if and only if $T$ admits an equational presentation such that, in each equation, the same set of variables appear in each term (cf. exercise 1.3.8).

(e) If $T$ is variabled, show that $(A, \xi)$ is a compact $T$-model [exercise 2.3.9(d)] if $\xi = \{(p, x) : x \in \mathrm{var}(p)\}$ for all sets $A$.
