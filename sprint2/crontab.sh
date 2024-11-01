#!/bin/bash

# Script para programar un trabajo de cron que ejecute un script cada lunes

# Define la ruta al script de Python que deseas ejecutar
SCRIPT="enviarcorreo.py"

# Define el trabajo de cron que quieres añadir
CRON_JOB="0 9 * * * /usr/bin/python3 $SCRIPT >> /ruta/al/logs/salida.log 2>&1"

# Agregar el trabajo al crontab actual
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

# Mensaje de confirmación
echo "Trabajo de cron programado para ejecutar '$SCRIPT' cada lunes a las 9:00 AM."
