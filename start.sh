#!/bin/bash


# Preguntar al usuario por la dirección IP o el nombre del host

read -p "Introduce la dirección IP o el nombre del host para comenzar el escaneo: " host

# Crear el directorio con el nombre de la IP
ip_directory="$host"
mkdir "$ip_directory"

# Crear el directorio nmap dentro del directorio de la IP
nmap_directory="$ip_directory/nmap"
mkdir "$nmap_directory"


# Ejecutar el comando ping y filtrar la salida para obtener el valor de TTL
ttl=$(ping -c 1 "$host" | grep -oP 'ttl=\K\d+')


# Mostrar el valor TTL

echo "TTL: $ttl"

# Compara el valor de TTL y mostrar si es Linux o Windows
if [ "$ttl" -le 64 ]; then
    echo "Sistema operativo: Linux"
else
    echo "Sistema operativo: Windows"
fi


# Llamar al script de Python pasando la dirección IP como argumento
python3 /ruta/completa/script/autoscan.py "$host" > "$nmap_directory/nmap_result.txt"
