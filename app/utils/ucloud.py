from django.http import HttpResponse
from django.shortcuts import render
import requests
from ucloud.core import auth
import time


def get_signature(data):
    # 签名算法，输出签名
    public_key  = "6YlP63feZp8F9C3kC31jn728Lnj4Lgmmm17Pz3hSq4"  # 公私钥 https://console.ucloud.cn/uapi/apikey
    private_key = "5bF9YyssKGw9HwAd8FmGWzDizrlytA59j9AkOqNOijVHFymiHtoMQLr7bR5QLkpR5Q"
    cred = auth.Credential(
        public_key,
        private_key,
    )
    signation = cred.verify_ac(data)
    return signation

def post_data(request):
    
    if request.GET:
        URL = 'https://api.ucloud.cn'
        if request.GET['Action'] == 'CreateUHostInstance' :
            data = {
                "Action": 'CreateUHostInstance',  
                # "ProjectId": 'org-t4xam1',  
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
                "Name":  request.GET['Name'],  
                "ImageId":request.GET['ImageId'],
                "Password":request.GET['Password'],
                "Disks.0.IsBoot":request.GET['IsBoot0'],
                "Disks.0.Type":request.GET['Type0'],
                "Disks.0.Size":request.GET['Size0'],
                "CPU":request.GET['Cpu'],
                "CharGEType":request.GET['ChargeTypes'],
                "LoginMode":"Password",
                "NetworkInterface.0.EIP.OperatorName":request.GET['peratorName0'],
                "NetworkInterface.0.EIP.Bandwidth":request.GET['Bandwidth0'],
                "NetworkInterface.0.EIP.PayMode":request.GET['PayMode0'],
                "Memory":request.GET['Memory'],
            } 
        elif request.GET['Action'] == 'StartUHostInstance':
            data = {
                "Action": 'StartUHostInstance', 
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
                "UHostId": request.GET['UHostId']
            } 
        elif request.GET['Action'] == 'StopUHostInstance':
            data = {
                "Action": 'StopUHostInstance',  
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
                "UHostId": request.GET['UHostId']
            } 
        elif request.GET['Action'] == 'TerminateUHostInstance':
            data = {
                "Action": 'TerminateUHostInstance',  
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
                "UHostId": request.GET['UHostId']
            } 
        elif request.GET['Action'] == 'DescribeUHostInstance':
            data = {
                "Action": 'DescribeUHostInstance',  
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
            } 
        elif request.GET['Action'] == 'DescribeImage':
            data = {
                "Action": 'DescribeImage',  
                "Region": request.GET['Region'],  
                "Zone":  request.GET['Zone'],  
            } 
        signation = get_signature(data)
        data.update({"Signature": signation})
        resp = requests.post(url=URL, data=data)
        return HttpResponse(resp.text) 
        
    else:
        return HttpResponse('Incomplete request parameters!')