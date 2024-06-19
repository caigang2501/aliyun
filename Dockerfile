FROM django

WORKDIR /aliyun

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=aliyun.settings
ENV PYTHONUNBUFFERED 1

# 如果使用 MySQL，安装 MySQL 客户端库
# RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# 收集静态文件（如果有需要）
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]



# docker build -t danger_dtc1 .
# docker save -o danger_dtc.tar danger_dtc
# scp danger_dtc.tar root@10.83.40.175:caigang
# docker load -i danger_dtc.tar
# docker run -d -p 8088:5000 danger_dtc1
# docker run -it -p 5010:5000 danger_dtc bash

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
