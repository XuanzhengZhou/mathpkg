---
role: exercise
locale: en
chapter: "4"
section: "3"
exercise_number: 4
---

Given $n$ complex numbers $\alpha_v$, prove that

$$\det \begin{bmatrix}
\alpha_{1} & \alpha_{2} & \cdots & \alpha_{n-1} & \alpha_{n} \\
\alpha_{2} & \alpha_{3} & \cdots & \alpha_{n} & \alpha_{1} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\alpha_{n} & \alpha_{1} & \cdots & \alpha_{n-2} & \alpha_{n-1}
\end{bmatrix} = (-1)^{\frac{n(n-1)}{2}} \beta_{1} \beta_{2} \cdots \beta_{n}$$

where the numbers $\beta_k$ are defined by

$$\beta_k = \sum_{v} \varepsilon_k^v \alpha_v, \quad \varepsilon_k = \cos \frac{2\pi k}{n} + i \sin \frac{2\pi k}{n} \quad (k = 1, \ldots, n).$$

Hint: Multiply the above matrix by the matrix

$$\begin{bmatrix}
\varepsilon_{1} & \varepsilon_{2} & \cdots & \varepsilon_{n} \\
\varepsilon_{1}^{2} & \varepsilon_{2}^{2} & \cdots & \varepsilon_{n}^{2} \\
\vdots & \vdots & \ddots & \vdots \\
\varepsilon_{1}^{n} & \varepsilon_{2}^{n} & \cdots & \varepsilon_{n}^{n}
\end{bmatrix}.$$
