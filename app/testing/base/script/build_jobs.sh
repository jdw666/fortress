#!/bin/bash
# 生成并提交用例
cd /var/lib/jenkins/workspace/build_jobs/
cp -r /var/lib/jenkins/workspace/build_jobs/sharp_spear/runtime/storage  /opt
for job in {sharp_spear,landscape,fortress}
do
    if [ -d "/var/lib/jenkins/workspace/build_jobs/$job" ];then 
        cd $job
        git checkout . 
        git pull origin dev
        if [ $job = sharp_spear ] ;then   
          php think worker:server stop
          php think worker:server -d
        fi
        if [ $job = landscape ] ;then
         	npm run serve &
         	npm run build
         	npm run lint
        fi
        # if [ $job = fortress ] ;then
        #     sudo python3 manage.py runserver &
        # fi
    else
        git clone git@code.yixzm.cn:ares/$job.git
        cd $job
        if [ $job = sharp_spear ] ;then   
         	/usr/local/bin/composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
        	/usr/local/bin/composer update topthink/framework
            chmod g+w runtime -R
        	cp .example.test.env .env
            cp ./install/mongodb/Mongo.php ./vendor/topthink/think-orm/src/db/connector/Mongo.php
        fi
        if [ $job = landscape ] ;then
        	npm install
        fi
    fi
    cd /var/lib/jenkins/workspace/build_jobs
done
# python3 ucloud.py &
