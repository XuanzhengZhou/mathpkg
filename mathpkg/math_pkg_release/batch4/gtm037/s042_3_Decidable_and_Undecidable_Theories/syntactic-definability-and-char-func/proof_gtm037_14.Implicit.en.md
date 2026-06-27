---
role: proof
locale: en
of_concept: syntactic-definability-and-char-func
source_book: gtm037
source_chapter: "14"
source_section: "Implicit Definability in Number Theories"
---

$(i) \Rightarrow (ii)$. Let $\varphi$ syntactically define $R$ in $\Gamma$. Let $\psi$ be the formula
$$(\varphi(v_0, \ldots, v_{m-1}) \land v_m = \mathbf{0}) \lor (\neg \varphi(v_0, \ldots, v_{m-1}) \land v_m = \mathbf{1}).$$
We claim $\psi$ syntactically defines $\chi_R$ in $\Gamma$. Let $x_0, \ldots, x_{m-1} \in \omega$ and let $y = \chi_R(x_0, \ldots, x_{m-1})$.

If $\langle x_0, \ldots, x_{m-1} \rangle \in R$, then $y = 0$ and $\varphi(x_0, \ldots, x_{m-1}) \in \Gamma$. Hence $\varphi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}) \land \mathbf{0} = \mathbf{0} \in \Gamma$, so $\psi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{0}) \in \Gamma$ as desired.

If $\langle x_0, \ldots, x_{m-1} \rangle \notin R$, then $y = 1$ and $\neg \varphi(x_0, \ldots, x_{m-1}) \in \Gamma$. Hence $\neg \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}) \land \mathbf{1} = \mathbf{1} \in \Gamma$, so $\psi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{1}) \in \Gamma$.

Thus $\psi$ syntactically defines $\chi_R$.

$(ii) \Rightarrow (i)$. Let $\psi$ syntactically define $\chi_R$ in $\Gamma$. Let $\varphi$ be the formula $\psi(v_0, \ldots, v_{m-1}, \mathbf{0})$ (i.e., substituting $\mathbf{0}$ for $v_m$). We claim $\varphi$ syntactically defines $R$ in $\Gamma$.

If $\langle x_0, \ldots, x_{m-1} \rangle \in R$, then $\chi_R(x_0, \ldots, x_{m-1}) = 0$, so $\psi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{0}) \in \Gamma$. Hence $\varphi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}) \in \Gamma$.

If $\langle x_0, \ldots, x_{m-1} \rangle \notin R$, then $\chi_R(x_0, \ldots, x_{m-1}) = 1 \neq 0$. Since $\psi$ syntactically defines $\chi_R$, we have $\psi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{1}) \in \Gamma$. Now, since $\neg(\mathbf{0} = \mathbf{1}) \in \Gamma$, we have $\neg \psi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{0}) \in \Gamma$ (because $\psi$ defines a function, so $\Gamma \vdash \psi(\bar{x}, \mathbf{0}) \land \psi(\bar{x}, \mathbf{1}) \to \mathbf{0} = \mathbf{1}$, and with $\neg(\mathbf{0} = \mathbf{1})$ we get $\neg(\psi(\bar{x}, \mathbf{0}) \land \psi(\bar{x}, \mathbf{1}))$; together with $\psi(\bar{x}, \mathbf{1})$ this yields $\neg \psi(\bar{x}, \mathbf{0})$). Thus $\neg \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}) \in \Gamma$, completing the proof.
