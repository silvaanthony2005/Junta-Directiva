# Inicializacion

```
git init                        # inicializa un nuevo repo de git      
git clone <repo-url>            # clona un repocitorio desde una URl 
```

# Desarrollo diario

```
git status                      # muestra el estado de los cambios
git add  <archivo>              # añade cambios al área de preparacion
git commit -m "mensaje"         # confirma los cambios con un mensaje
```

# Gestion de ramas

```
git branch                      # lista las ramas
git branch <nombre-rama>        # crea una nueva rama
git switch <nombre-rama>        # cambia a una rama
git branch -d <nombre-rama>     # elimina una rama
```

# Integracion y colaboracion

```
git merge <rama>                # fusiona los cambios de una rama
git remote add <nombre> <url>   # añade un repositorio remoto
git push <remoto> <rama>        # envia los cambios a un repositorio
git pull <remoto> <rama>        # obtiene y fusiona los cambios de un repo remoto
```

# Recuperacion y limpieza

```
git fetch                       # recupera cambios sin fusionar
git reset --hard HEAD           # desecha todos los cambios locales
git revert <hash-commit>        # revierte los cambios de un commit
```

# avanzado y utilidades

```
git diff <a> <b>                # compara dos commits, ramas o archivos
git show <hash>                 # muestra detalles de un commit
git stash                       # guarda cambios temporales y limpia el working
git stash pop                   # restaura los cambios guardados del stash
git sherry-pick <hash>          # aplica un commit especifico en la rama actual
git rebase <base>               # replica commits sobre otra base
```