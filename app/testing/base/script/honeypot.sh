#!/bin/bash
# 生成并提交用例
cd /var/lib/jenkins/workspace/build_jobs/fortress/app/testing/base/test
git pull origin dev
python3 honeypot.py
