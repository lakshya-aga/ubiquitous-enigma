
# Deriving $dx . dy = r. dr. d\theta$ via the Jacobian

## Setup

Using the convention from the board: $x = r\sin\theta$, $y = r\cos\theta$.

## Compute the partial derivatives

$$\frac{\partial x}{\partial r} = \sin\theta, \qquad \frac{\partial x}{\partial \theta} = r\cos\theta$$

$$\frac{\partial y}{\partial r} = \cos\theta, \qquad \frac{\partial y}{\partial \theta} = -r\sin\theta$$

## Form the Jacobian matrix

$$J = \begin{pmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta}  \\  \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{pmatrix} = \begin{pmatrix} \sin\theta & r\cos\theta \ \\  \cos\theta & -r\sin\theta \end{pmatrix}$$

## Take the determinant

$$\det(J) = (\sin\theta)(-r\sin\theta) - (r\cos\theta)(\cos\theta)$$

$$= -r\sin^2\theta - r\cos^2\theta$$

$$= -r(\sin^2\theta + \cos^2\theta) = -r$$

## Apply the change-of-variables formula

The area element transforms as $dx, dy = |\det(J)|, dr, d\theta$:

$$dx. dy = |-r|. dr. d\theta = r. dr. d\theta \qquad (r \geq 0)$$

$$\boxed{dx. dy = r. dr. d\theta}$$

The negative sign just reflects orientation (this convention swaps the usual roles of sine and cosine); taking the absolute value gives the standard area element.

---

Topics: [[Calculus, Bonds, Options, Finance, Math]]
Reference:
Type: #atom