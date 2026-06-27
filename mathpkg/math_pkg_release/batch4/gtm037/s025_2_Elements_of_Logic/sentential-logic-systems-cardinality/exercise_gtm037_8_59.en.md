---
role: exercise
locale: en
chapter: "8"
section: "Part 2: Elements of Logic"
exercise_number: 59
---
We have considered several different systems of sentential logic: two-valued, three-valued, and intuitionistic logic. How many different systems are there altogether? Here is a "best possible" answer: Let $\mathcal{P} = (n, c, \{s\})$ be a sentential language. Given any set $\Gamma \subseteq \text{Sent}_{\mathcal{P}}$, let $S_\Gamma$ be the intersection of all classes including $\Gamma$ and closed under detachment. Let $\mathcal{S} = \{S_\Gamma : \Gamma \subseteq \text{Sent}_{\mathcal{P}}\}$. Show that $|\mathcal{S}| = \exp \aleph_0$. Hint: define $\varphi_n$ recursively:

$$\varphi_0 = \langle s \rangle \rightarrow \langle s \rangle;$$
$$\varphi_{n+1} = \varphi_n \rightarrow \langle s \rangle.$$

For each subset $M$ of $\omega$ let $\Gamma_M = \{\varphi_{3n} : n \in M\} \cup \{\varphi_{3n+1} : n \notin M\}$. Show that $M \neq N \Rightarrow S_{\Gamma_M} \neq S_{\Gamma_N}$.
