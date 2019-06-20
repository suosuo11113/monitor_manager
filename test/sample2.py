#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  dns.resolver
if __name__ == '__main__':
    domain = input('Please input an domain: ')

    A = dns.resolver.query(domain, 'A')


    for i in A.response.answer:
        for j in i.items:
            print (j.address)

