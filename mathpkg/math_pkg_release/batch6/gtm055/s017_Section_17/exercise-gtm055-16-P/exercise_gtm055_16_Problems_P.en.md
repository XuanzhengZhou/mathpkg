---
role: exercise
locale: en
chapter: "16"
section: "Problems"
exercise_number: "P"
---

A net $\{f_{\lambda}\}_{\lambda \in \Lambda}$ in $\mathcal{E}^*$ is \textbf{weak$^*$ Cauchy} if the net $\{f_{\lambda}(x)\}$ is Cauchy in $\mathbb{C}$ for every $x \in \mathcal{E}$. Define $\mathcal{E}$ to be \textbf{weakly complete} if every weakly Cauchy net in $\mathcal{E}$ is weakly convergent. Define $\mathcal{E}^*$ to be \textbf{weak$^*$ complete} if every weak$^*$ Cauchy net in $\mathcal{E}^*$ is weak$^*$ convergent.

(i) Show that if $F$ is any linear functional on $\mathcal{E}$, then there exists a net $\{f_{\lambda}\}$ in $\mathcal{E}^*$ such that $f_{\lambda}(x) \rightarrow F(x)$ for every $x \in \mathcal{E}$, and verify that the net $\{f_{\lambda}\}$ is weak$^*$ Cauchy. Conclude that $\mathcal{E}^*$ is weak$^*$ complete if and only if $\mathcal{E}$ (and therefore $\mathcal{E}^*$) is finite dimensional.

\textit{Hint:} The restriction of $F$ to each finite dimensional subspace $\mathcal{F}$ of $\mathcal{E}$ is bounded on $\mathcal{F}$, and therefore possesses an extension $f_{\mathcal{F}}$ belonging to $\mathcal{E}^*$. Use the fact that the finite dimensional subspaces of $\mathcal{E}$ form a directed set in the inclusion ordering, and also the fact that there exist unbounded linear functionals on $\mathcal{E}$ if $\mathcal{E}$ is infinite dimensional.

(ii) Follow the line of argument used in (i) to show that if $\varphi$ is an arbitrary linear functional on $\mathcal{E}^*$, then there exists a net $\{x_{\lambda}\}$ in $\mathcal{E}$ such that $\lim_{\lambda} f(x_{\lambda}) = \varphi(f)$ for every $f$ in $\mathcal{E}^*$. Conclude that $j(\mathcal{E})$ is weak$^*$ dense in $\mathcal{E}^{**}$.
