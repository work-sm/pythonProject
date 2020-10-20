用户目录下  
pip 文件夹  
pip.ini 
 
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com


pip freeze >requirements.txt

pip install -r requirements.txt

