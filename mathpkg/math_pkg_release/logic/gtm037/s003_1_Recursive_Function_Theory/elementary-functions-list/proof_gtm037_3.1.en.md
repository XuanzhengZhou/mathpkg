---
role: proof
locale: en
of_concept: elementary-functions-list
source_book: gtm037
source_chapter: "3"
source_section: "1"
---
\begin{proof}
(1) $C_0^1$ is elementary: $C_0^1 x = |x - x|$ for all $x \in \omega$, using the absolute difference which is elementary.

(2) $\overline{\text{sg}}$ is elementary: $\overline{\text{sg}}\, x = \prod_{y < x} C_0^1 y$ for all $x \in \omega$, using bounded multiplication of the constant zero function.

(3) $\text{sg}$ is elementary: $\text{sg}\, x = \overline{\text{sg}}\;\overline{\text{sg}}\, x$ for all $x \in \omega$, since $\text{sg}$ is obtained by composing $\overline{\text{sg}}$ with itself.

(4) $C_1^1$ is elementary: $C_1^1 x = \overline{\text{sg}}\, C_0^1 x$ for all $x \in \omega$.

(5) $C_m^1$ is elementary by induction on $m$: $C_{m+1}^1 x = C_m^1 x + C_1^1 x$ for all $x \in \omega$. Using addition and the induction hypothesis, each constant unary function is elementary. The $n$-ary constant functions $C_m^n$ for $n \neq 0$ are then obtained by composing $C_m^1$ with projection functions.

(6) $\sigma$ is elementary by definition as one of the initial functions 2.1(2).

(7) $\mu$ is elementary: the predecessor function can be defined using bounded summation and the sign function.

(8) Exponentiation and factorial are elementary using bounded multiplication and the already-established elementary functions.
\end{proof}
