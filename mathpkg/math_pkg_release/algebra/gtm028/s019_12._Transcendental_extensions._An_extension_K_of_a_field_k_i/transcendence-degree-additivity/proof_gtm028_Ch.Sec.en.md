---
role: proof
locale: en
of_concept: transcendence-degree-additivity
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

Let $L$ and $M$ be transcendence bases of $K/k$ and $\Delta/K$ respectively. It will be sufficient to prove that $L \cup M$ is a transcendence basis of $\Delta/k$.

Let $\{x_1, x_2, \dots, x_m, y_1, y_2, \dots, y_n\}$ be any finite subset of $L \cup M$, where we assume that the $x_i$ are in $L$ and the $y_j$ are in $M$. Let $f(\{X\}, \{Y\}) = f(X_1, X_2, \dots, X_m, Y_1, Y_2, \dots, Y_n)$ be a polynomial in $m + n$ indeterminates, with coefficients in $k$, such that $f(\{x\}, \{y\}) = 0$. The polynomial $f(\{x\}, Y)$ in the $n$ indeterminates $Y_j$ has coefficients in $K$ and must be zero since the $y_j$ are algebraically independent over $K$. Since the $x_i$ are algebraically independent over $k$, it follows that $f(\{X\}, \{Y\})$, regarded as a polynomial in $\{Y\}$ with coefficients in $k[\{X\}]$, must be zero. Hence $f$ is the zero polynomial, proving $L \cup M$ is a transcendence set.

Now, $\Delta$ is algebraic over $K(M)$ (since $M$ is a transcendence basis of $\Delta/K$), and $K$ is algebraic over $k(L)$ (since $L$ is a transcendence basis of $K/k$). Thus every element of $\Delta$ is algebraic over $k(L \cup M)$. Hence $L \cup M$ is a transcendence basis of $\Delta/k$, and the additivity formula follows by cardinal arithmetic.
