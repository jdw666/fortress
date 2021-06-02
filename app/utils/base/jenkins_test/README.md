# build_jobs

```shell
#!/bin/bash
for job in {sharp_spear,fort,assistant,auxiliary}
#job=sharp_spear
do 
    if [ -d "/var/lib/jenkins/workspace/build_jobs/$job" ];then 
        cd $job
        git checkout dev
        git pull
        php think worker:server stop
        php think worker:server -d
    else
        git clone git@code.yixzm.cn:ares/$job.git 
        cd $job
        /usr/local/bin/composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
        /usr/local/bin/composer update topthink/framework
	fi
    cd /var/lib/jenkins/workspace/build_jobs
done
```
# create_case

```shell
#!/bin/bash
# 生成并提交用例
if [ ! -d "./fort" ]; then
  git clone gogs@ci.yixzm.cn:ares/fort.git
fi
cd ./fort && git pull origin dev
rm test/auto/ -rf
/usr/local/bin/pytest -k test_create_case
git config --global user.name "jenkins"
git config --global user.email jenkins@yixzm.cn
git add .
git commit -m "jenkins update testcase"
git push origin dev
```
# create_mock_data

```shell
curl http://dev.www.yixzm.cn/sdk/IpRegion/buildData
```
# test_auto_api_note_test

```shell
rm fort -rf
git clone gogs@ci.yixzm.cn:ares/fort.git
cd fort
git checkout dev
/usr/local/bin/pytest -k test_auto_api_note_test
```

# test_auto_code_200_test

```shell
rm fort -rf
git clone gogs@ci.yixzm.cn:ares/fort.git
cd ./fort && /usr/local/bin/pytest -k test_auto_code_200_test
#git checkout dev

# test_auto_href_title_test

#!/bin/sh
rm fort -rf
git clone gogs@ci.yixzm.cn:ares/fort.git
cd fort
/usr/local/bin/pytest -k test_auto_href_title_test
```
# test_yblog_sitemap_href_browser_open

```shell
rm fort -rf
git clone gogs@ci.yixzm.cn:ares/fort.git
cd fort
git checkout dev
/usr/local/bin/pytest -k test_auto_href_browser_open
```