#! /bin/bash
file="/home/Spider_task2_DevOps"

cd $file

cd Server_arch
export FLASK_APP=Server_arch
export FLASK_ENV=development
echo $SHELL
gnome-terminal -e "bash -c 'flask run -p 8000;exec $SHELL'"
cd ..
cd Server_debian
export FLASK_APP=Server_debian
export FLASK_ENV=development
gnome-terminal -e "bash -c 'flask run -p 8001;exec $SHELL'"
cd ..
cd Server_kali
export FLASK_APP=Server_kali
export FLASK_ENV=development
gnome-terminal -e "bash -c 'flask run -p 8002;exec $SHELL'"
cd ..
cd Server_secrets
export FLASK_APP=Server_secrets
export FLASK_ENV=development
gnome-terminal -e "bash -c 'flask run -p 8003;exec $SHELL'"
cd ..
