FROM django

WORKDIR /aliyun

COPY . .

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 将 Django 静态文件收集到一个目录
# RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# NFD2=Whk$VK!EEf$R
# docker build -t aliyun .
# docker save -o danger_dtc.tar danger_dtc
# scp aliyun/settings.py root@47.121.137.79:aliyun/aliyun 
# docker load -i danger_dtc.tar
# docker run -d -p 8088:5000 aliyun
# docker run -it -p 5010:5000 aliyun bash

# docker exec -it django_app /bin/bash
# docker exec -it <e2545f0769ed> uname -m
# gunicorn -w 4 -b 0.0.0.0:5000 your_flask_app:app
# uwsgi --http :5000 --wsgi-file your_flask_app.py

#删除指定容器
#docker rm <container_id_or_name>
#删除所有停止的容器
#docker container prune
#删除指定镜像
#docker rmi <image_id_or_name>
#删除所有未被使用的镜像
#docker image prune
## 删除所有容器
#docker rm $(docker ps -aq)
## 删除所有镜像
#docker rmi $(docker images -q)
