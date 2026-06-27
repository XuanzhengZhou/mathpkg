---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 8
---

# Exercise 8

Show that $P_n \xrightarrow{w} P$ if and only if every subsequence $\{P_{n'}\}$ of $\{P_n\}$ contains a subsequence $\{P_{n''}\}$ such that $P_{n''} \xrightarrow{w} P$.

*Hint.* The forward direction is immediate: if the full sequence converges weakly, then every subsequence converges weakly to the same limit. For the reverse direction, suppose $P_n$ does not converge weakly to $P$. Then there exists a bounded continuous function $f$ such that $\int f \, dP_n \not\to \int f \, dP$. Extract a subsequence $\{P_{n'}\}$ for which $|\int f \, dP_{n'} - \int f \, dP| \geq \varepsilon > 0$ for all $n'$. By hypothesis, this subsequence contains a further subsequence converging weakly to $P$, which contradicts the choice of $\varepsilon$. Conclude by contradiction.
