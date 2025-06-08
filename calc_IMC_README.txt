Calculadora de IMC en Python

Este programa permite al usuario ingresar sus datos personales (nombre, apellidos, edad, peso y estatura), y calcula su IMC para clasificarlo según los rangos establecidos como saludables con la idea de ayudar a mejorar la salud.

¿Cómo funciona mi programa?

1. Crear una validación de datos: 
	- Solo permite uno o dos nombres.
	- No permite campos vacíos ni valores no numéricos.
	- Además indica que la estatura debe estar en metros
	- La edad debe ser un número entero y la estatura/peso deben ser mayores a cero.

2. Cálculo del IMC:
	- Se calcula con la fórmula:  
     \[IMC = \frac{\text{peso (kg)}}{\text{estatura (m)}^2}\]

3. Clasificación:
El programa clasifica al usuario según su IMC en estos tipos:

	- Delgadez severa
	- Delgadez moderada
	- Delgadez leve
	- Normal
	- Sobrepeso
	- Obesidad leve, media o mórbida

Además quise incluir un pequeño mensaje respecto al IMC con esperanzas de alentar al usuario a cuidarse

4. Bucle interactivo:

	- Al final, pregunta si deseas ingresar los datos de otra persona. Si respondes "No", termina con un mensaje de despedida, aunque en realidad por el tema del código termina con cualquier palabra distinta a Si.

Reflexiones del Bootcamp

Hasta ahora, el bootcamp me ha permitido reforzar mis habilidades en Python, especialmente en:
- Estructuras de control (`while`, `if`, `else`), aquí batalle bastante buscando errores
- Validación de entradas del usuario
- Manejo de errores con `try/except`
- Dividir el código en funciones reutilizables, lo cual también me ha permitido trabajar mi lógica porque me tuve que poner a trabajar en "pedacitos" para poder hacer funcionar las cosas sin "romperlas" lo cual fue algo desafiante pero me ha servido mucho. Y no solo me ha ayudado a mejorar mi lógica, sino también me ha ayudado a mejorar mi comprensión de cómo estructurar programas más limpios y fáciles de mantener.

Este aprendizaje ha sido muy enriquecedor y motivador, sobretodo me agrada mucho que no he podido tomar las clases en sincronía por temas laborales, pero siempre puedo ver las sesiones grabadas, lo que de verdad, agradezco muchísimo y aprecio aún más.

