---
role: proof
locale: en
of_concept: complete-extensions-of-gamma3
source_book: gtm037
source_chapter: "13"
source_section: "Decidable Theories"
---

(i) By condition (1) in the proof of Theorem 13.12, $\varepsilon_m \land \neg \varepsilon_{m+1}$ holds in a set $A$ iff it holds in the set $m$. Hence
$$\Gamma_3^m = \{\varphi : \varphi \text{ holds in } m\},$$
so $\Gamma_3^m$ is complete and consistent (it is the theory of the structure $m$). Similarly,
$$\Gamma_3^\infty = \{\varphi : \varphi \text{ holds in every infinite set}\},$$
which is also complete and consistent. Decidability follows from the decision method for $\Gamma_3$ (Theorem 13.12): to decide whether $\varphi \in \Gamma_3^m$, one checks whether $\varphi$ holds in the finite set $m$; to decide whether $\varphi \in \Gamma_3^\infty$, one checks whether $\varphi$ holds in all sufficiently large finite sets.

(ii) Let $\Delta$ be any complete and consistent extension of $\Gamma_3$. By completeness, for each $m \in \omega \setminus \{1\}$, either $\varepsilon_m \in \Delta$ or $\neg \varepsilon_m \in \Delta$. If $\Delta$ contains $\varepsilon_m$ for arbitrarily large $m$, then $\Delta = \Gamma_3^\infty$. Otherwise, there is a largest $m$ such that $\varepsilon_m \in \Delta$; then $\Delta = \Gamma_3^m$. This exhausts all possibilities.
