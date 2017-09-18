注意事项：
1、.env文件，windows下加入配置：
COMPOSE_CONVERT_WINDOWS_PATHS=1
2、缺少hyperledger/fabric-baseimage:latest镜像：
pull最新的镜像x86_64-0.3.0，重新标签为latest