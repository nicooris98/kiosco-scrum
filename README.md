# Proyecto Kiosco
Este es el repositorio del proyecto de kiosco.

# Flujo Git

## Creamos la rama en base a develop
```
git checkout -b nombre-rama
```

## Trabajamos sobre esa rama
```
git add .
git commit -m "some changes"
git push
```

## Actualizamos la rama con develop
En la rama develop ejecutar:
```
git pull
```

En nuestra rama ejecutar:
```
git merge develop
```
Resolvemos conflictos si los hubiese.

## Pusheamos la rama con los cambios
```
git push
```

## Crear merge request dentro del repositorio