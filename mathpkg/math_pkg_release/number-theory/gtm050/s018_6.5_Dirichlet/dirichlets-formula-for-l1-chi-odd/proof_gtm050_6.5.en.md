role: proof
locale: en
of_concept: dirichlets-formula-for-l1-chi-odd
source_book: gtm050
source_chapter: "6. Determination of the Class Number"
source_section: "6.5 Dirichlet's evaluation of L(1,\\chi)"

Starting from the master formula

$$L(1, \chi_j) = (-1)^j m_j \sum_{k=0}^{\lambda-2} \beta^{-jk} \log \frac{1}{1-\sigma^k \alpha},$$

take $j = 2\nu+1$ to be odd, so $(-1)^j = -1$.

Choose the specific primitive root $\alpha = e^{2\pi i/\lambda}$. Then $\sigma^k \alpha = e^{2\pi i \gamma^k/\lambda}$, and the corresponding angle $\theta$ in $(0, 2\pi)$ is $\theta = 2\pi \gamma_k / \lambda$, where $\gamma_k$ is the integer with $0 < \gamma_k < \lambda$ and $\gamma_k \equiv \gamma^k \bmod \lambda$.

Compute the logarithm:

$$\frac{1}{1-\sigma^k \alpha} = \frac{1}{1-e^{i\theta}} = \frac{e^{-i\theta/2}}{e^{-i\theta/2} - e^{i\theta/2}} = \frac{e^{-i\theta/2}}{-2i \sin(\theta/2)} = \frac{e^{i(\pi-\theta)/2}}{2\sin(\theta/2)}.$$

Therefore

$$\log \frac{1}{1-\sigma^k \alpha} = -\log\left(2\sin\frac{\theta}{2}\right) + \frac{i}{2}(\pi - \theta),$$

where $\frac{1}{2}(\pi - \theta)$ lies between $-\pi/2$ and $\pi/2$ since $0 < \theta < 2\pi$.

Now substitute $\theta = 2\pi \gamma_k / \lambda$. The real part $-\log(2\sin(\theta/2))$ cancels in the full sum over $k = 0, 1, \dots, \lambda-2$ when multiplied by the character values, because the conjugate-pairing argument that worked for even $j$ does not apply here for odd $j$ (since $\beta^{-(2\nu+1)\mu} = -1$ rather than $+1$).

For the imaginary part, we have

$$\frac{i}{2}(\pi - \theta) = \frac{i\pi}{2} - i\frac{\pi \gamma_k}{\lambda}.$$

The constant term $\frac{i\pi}{2}$ multiplied by $\sum \beta^{-(2\nu+1)k}$ vanishes because the sum of a nonprincipal character over a complete set of residues is zero. Hence only the term proportional to $\gamma_k$ survives:

$$L(1, \chi_{2\nu+1}) = -m_{2\nu+1} \sum_{k=0}^{\lambda-2} \beta^{-(2\nu+1)k} \left(-i\frac{\pi \gamma_k}{\lambda}\right) = \frac{i\pi}{\lambda} m_{2\nu+1} \sum_{k=0}^{\lambda-2} \gamma_k \beta^{-(2\nu+1)k}.$$

This is the desired formula.
