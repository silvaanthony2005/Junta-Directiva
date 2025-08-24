# Comandos del sistema

```
pwd         muestra tu ubicacion
ls          lista archivos
mkdir       crea carpeta
rm          barra archivo/carpeta
cp          copia archivos
mv          mueve o renombra
touch       crea archivos vacio
cat         muestra archivo
nano        editor de texto
clear       limpiar terminal   
man         muestra ayuda/manual
```

# Gestion de usuarios

```
whoami      muestra usuario actual
adduser     crea usuario
passwd      cambia contraseña
deluser     elimina usuario
usermod     -aG grupo de usuar usuario
id          muestra UID y GiD
```

# Informacion del sistema

```
df -h             # uso del disco
free -h           # uso de RAM
top               # procesos
uname -a          # info del sistema
uptime            # tiempo encendido
```

# Busqueda (Debian/Ubutu)

```
apt update        # actualiza indices
aot upgrade       # actualiza paquetes
apt install       # instala
apt remove        # desinstala
```

# Permisos

```
ls -l             # ver permisos
chmod             # cambiar permisos
chown             # cambiar dueño
chgrp             # cambiar grupo
chmod +t          # stiky bit
chmod u+s         # SUID
```

# Estructura de linux

```
            / (raiz principal)
            |
            |--bin  (binarios esenciales)
      /etc--|
            |--/toc (configuraciones)
      /home--|
            |--mnt (contiene los usuarios)
      /mnt--|
            |--/opt (programas opcionales)
      /rm--|
            |--/srv (servicios del sistema)
      /lib--|
            |--/tmp (arranque del sistema)
      /usr--|
            |--/var (programas y datos de usuarios)
            |
```