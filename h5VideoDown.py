#!/usr/bin/python3
 
# In[1]:
 
 
import requests
import re
 
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
 
 
# In[2]:
 
 
headers = {
    'User-Agent': ua,
}
 
response = requests.get('https://apd-f7b9eff46dec7f445b83ad7ce66881e7.v.smtcdns.com/newsts.tc.qq.com/AxX2IVBFSKZKljuQlR16Q4Rtu1YM8yt4MCVVBpAU2qyc/5QSx4cOPVnrsEZoXel9kLPQqwzotq_YqO9mgVXJarwwHJ_lx_OfPdNcpa7aV3wnQiA1hoGX6T_rNTqBgcLjf-863H4xe50swNpbEPHPuaQ8vVuK7H-u6wNx8DTUocvYSMJDlKChZyKQF_zszSylZSZDfM235OXV0/q0023x6yiss.321002.ts.m3u8?ver=4', headers=headers)
 
 
# In[6]:
 
 
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://v.qq.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'User-Agent': ua,
    'Accept': '*/*',
    'Referer': 'https://v.qq.com/x/page/d0019qdukl5.html',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}
 
 
# In[8]:
 
 
result = re.findall(r'^\d+.*index=\d+.*$', response.text, re.M)
 
 
# In[10]:
 
 
fmp4 = open('0.mp4', 'wb')
for i,r in enumerate(result):
    print(i, end=', ', flush=True)   # 进度
    rsp = requests.get('https://apd-vliveachy.apdcdn.tc.qq.com/newsts.tc.qq.com/AxX2IVBFSKZKljuQlR16Q4Rtu1YM8yt4MCVVBpAU2qyc/5QSx4cOPVnrsEZoXel9kLPQqwzotq_YqO9mgVXJarwwHJ_lx_OfPdNcpa7aV3wnQiA1hoGX6T_rNTqBgcLjf-863H4xe50swNpbEPHPuaQ8vVuK7H-u6wNx8DTUocvYSMJDlKChZyKQF_zszSylZSZDfM235OXV0/'+r, headers=headers)
    fmp4.write(rsp.content)
    f = open('{0:0>8}.ts'.format(i), 'wb')
    f.write(rsp.content)
    f.close()
fmp4.close()