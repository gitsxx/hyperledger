# -*- coding:UTF-8 -*-

from hyperledger.client import Client
import base64
import requests
import json
import time

url = "http://222.28.78.243:7050"

c = Client(base_url=url)


#-----------------查询chaincodeID--------------------#
def blockInfo(index):
    block = c.block_get(str(index))
    print 'stateHash:', block["stateHash"]
    print 'previousBlockHash:', block["previousBlockHash"]
    print 'nonHashData:', block["nonHashData"]
    print 'transactions:', block["transactions"]
    # print 'stateHash:', block["stateHash"]
    # print 'stateHash:', block["stateHash"]


#-----------------查询blockchain哈希以及块的高度--------------------#
def chainInfo():
    #查询blockchain哈希以及块的高度: 1,查询当前块Hash 2，查询前一个块hash，其他值，返回块高度
    chain=c.chain_list()
    print "currentBlockHash:", chain['currentBlockHash']
    print "previousBlockHash:", chain['previousBlockHash']
    print "height:", chain['height']


if __name__=="__main__":

    # chainInfo()

    #blockInfo("1")

    # print c.chaincode_deploy(
    #     chaincode_path="https://github.com/ug1y/learn-chaincode/archive",
    #     function="init",
    #     args=None
    # )

    code="67c2baeda53c09d6a702a25025e59c6f54fdd1b63b8da912698248f1a331418375d92e58f85b5395c2fb4d5fa0e84fc0dd8b018d8aa4f7cadaaa29581e750a1e"

    print c.chaincode_invoke(
        chaincode_name=code,
        function="append",
        args=[
        "Vogelstein B, Lane D, Levine A J",
        "Surfing the p53 network[J]",
        "Nature",
        "2000",
        "408(6)",
        "307-1003"]
    )

    # print c.chaincode_query(
    #     chaincode_name="gg",
    #     function="total",
    #     args=[""]
    # )