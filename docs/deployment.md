# Cloud Deployment Guide

## 1. Server
- Alibaba Cloud / Huawei Cloud ECS
- Ubuntu 22.04 recommended

## 2. Setup
sudo apt update
sudo apt install python3 python3-pip

## 3. Upload project
git clone <your repo>

## 4. Install dependencies
pip3 install -r requirements.txt

## 5. Run
nohup python3 app.py &

## 6. Expose port 5000 in security group
