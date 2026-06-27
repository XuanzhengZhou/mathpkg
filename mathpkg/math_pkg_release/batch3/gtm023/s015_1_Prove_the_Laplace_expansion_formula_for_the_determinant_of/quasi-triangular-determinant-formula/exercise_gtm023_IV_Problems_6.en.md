---
role: exercise
locale: en
chapter: "IV"
section: "Problems"
exercise_number: 6
---

Verify the following formula for a quasi-triangular determinant:

$$\det \begin{pmatrix}
x_{11} & \ldots & x_{1p} & 0 & \ldots & 0 \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
x_{p1} & \ldots & x_{pp} & 0 & \ldots & 0 \\
x_{p+1,1} & \ldots & x_{p+1,p} & x_{p+1,p+1} & \ldots & x_{p+1,n} \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
x_{n1} & \ldots & x_{np} & x_{n,p+1} & \ldots & x_{nn}
\end{pmatrix} = \det \begin{pmatrix}
x_{11} & \ldots & x_{1p} \\
\vdots & \ddots & \vdots \\
x_{p1} & \ldots & x_{pp}
\end{pmatrix} \cdot \det \begin{pmatrix}
x_{p+1,p+1} & \ldots & x_{p+1,n} \\
\vdots & \ddots & \vdots \\
x_{n,p+1} & \ldots & x_{nn}
\end{pmatrix}.$$
